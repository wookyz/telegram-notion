from dateutil.parser import parse
from typing import Any, List, Dict
from datetime import datetime

from notion_client import Client


class Notionpy():

    def __init__(
        self,
        api_key: str
    ) -> None:

        self.notion = Client(auth=api_key)
        self.databases = []
        self.pages = []

    def search_all_databases(self) -> List:
        """Returns a list of all databases that are shared with application."""
        return self.notion.search(filter={"property": "object", "value": "database"}).get("results")

    def search_all_pages(self) -> List:
        """Search for all pages that are shared with application."""
        return self.notion.search(filter={"property": "object", "value": "page"}).get("results")

    def list_all_pages(self, database_id: str) -> List:
        """Returns a list of all pages in a given database."""
        return self.notion.databases.query(database_id=database_id).get("results")
    
    def get_database_by_name(self, title: str) -> Dict[str, Any]:
        """Return a database given a name."""
        try:
            return next((db for db in self.databases if title == db["title"]), None)
        except IndexError:
            print("Failed to access database list.")
            raise

    def get_first_page(self) -> Dict[str,Any]:
        today = datetime.today().date() 
        return next((pg for pg in self.pages if today.strftime("%d/%m/%y") == pg["title"]), None)
        
    def get_last_block(self,page: str) -> Dict[str,Any]:
        id = page["id"]
        last_block = self.notion.blocks.children.list(id).get("results")
        return last_block[-1]

    def has_today_page(self, today: datetime, database_id: str) -> bool:
        pages = self.list_all_pages(database_id)
        pages = self.parse_pages(pages)

        for pg in pages:
            pg_date = parse(pg["created"])
            if today.date() == pg_date.date():
                return True
        return False

    def parse_databases(self, databases: List) -> List[Dict[str, str]]:
        """Parses a database objects into a dictionary within a list."""
        object = {}

        for db in databases:
            object = db.copy()
            self.databases.append(
                {"id": object["id"], "title": object["title"][0]["plain_text"]})
        return self.databases

    def parse_pages(self, pages: List) -> List[Dict[str, Any]]:
        """Parses a page objects into a dictionary within a list."""

        for pg in pages:
            object = pg.copy()
            title = object["properties"]["Name"]["title"][0]["text"]["content"]
            self.pages.append(
                {"id": object["id"], "created": object["created_time"], "title": title})
        return self.pages

    def parse(self) -> List[Dict[str, Any]]:
        databases = self.search_all_databases()
        databases = self.parse_data(databases)

        pages = self.list_all_pages()
        pages = self.parse_pages(pages)

        return databases, pages

    def create_page(self, today: str, database_id: str) -> None:
        new_page = {
            "Name": {"title": [{"text": {"content": today}}]}
        }
        block = [{
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "text": [{"type": "text", "text": {
                    "content": "Dear Diary..."
                }}]
            }
        }]
        self.notion.pages.create(
            parent={"database_id": database_id}, properties=new_page, children=block)
        return

    def append_block(self,message: List):
        page_id = self.get_first_page()["id"]
        self.notion.blocks.children.append(page_id,children=message)
        