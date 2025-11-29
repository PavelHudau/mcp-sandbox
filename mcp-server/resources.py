from mcp.server.fastmcp import FastMCP

mcp = FastMCP("lResources")

inventory_id_to_price = {
    "item_001": 19.99,
    "item_002": 29.99,
    "item_003": 9.99,
    "item_004": 49.99,
}

inventory_name_to_id = {
    "Item One": "item_001",
    "Item Two": "item_002",
    "Item Three": "item_003",
    "Item Four": "item_004",
}


@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Provides an overview of the current inventory items (names only).
    """
    return "\n".join(inventory_name_to_id.keys())


@mcp.resource("inventory://{inventory_id}/price", name="get price by item id")
def get_inventory_price_by_id(inventory_id: str) -> float:
    """
    Retrieves the price of an inventory item by its ID.

    Args:
        item_id (str): The ID of the inventory item.

    Returns:
        float: The price of the inventory item.
    """
    return inventory_id_to_price.get(inventory_id, 0.0)


@mcp.resource("inventory://{inventory_name}/id")
def get_inventory_id_by_name(inventory_name: str) -> str:
    """
    Retrieves the ID of an inventory item by its name.

    Args:
        item_name (str): The name of the inventory item.

    Returns:
        str: The ID of the inventory item.
    """
    return inventory_name_to_id.get(inventory_name, "")


if __name__ == "__main__":
    mcp.run()
