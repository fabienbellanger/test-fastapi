from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """
    ItemBase model

    @author Fabien Bellanger
    """

    name: str = Field(..., description="Name of the item")
    price: float = Field(..., description="Price of the item")
    is_offer: bool | None = Field(None, description="Is the item an offer?")


class ItemEdit(ItemBase):
    """
    ItemBase model

    For creation and edition of an item

    @author Fabien Bellanger
    """

    pass


class Item(ItemBase):
    """
    Item model

    @author Fabien Bellanger
    """

    id: int = Field(..., description="Item ID")

    def display(self) -> str:
        """
        Display item

        Display the name and the price of an item.
        """

        return self.name + " at " + str(self.price)

    class ConfigDict:
        from_attributes = True
