from fastapi import FastAPI, HTTPException, Query

from models import MenuResponse, MenuItem

from data import menu_items

app = FastAPI(
    title="Backend API",
    version="1.1.0",
    description="This is a backend API for the project."
)

@app.get('/')
def index():
    return "Hi there!"

@app.get('/menu', response_model = MenuResponse)
def get_menu(category: str | None = Query(None, description = "Filter by category cahi or snacks or cold drinks")):
    """ All items or category wise item filter"""
    if category:
        filter_items = [item for item in menu_items if item["category"] == category.lower()]
        if not filter_items : 
            raise HTTPException(status_code=404, detail=f"No item found in category :  {category}")
        return MenuResponse(count = len(filter_items), items = filter_items)
    return MenuResponse(count = len(menu_items), items = menu_items)

@app.get('/menu/{item_id}', tags=['Menu'], response_model=MenuItem)
def get_item(item_id: int):
    """ return single item from menu item """
    for item in menu_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Menu item with id {item_id} not found")
    
