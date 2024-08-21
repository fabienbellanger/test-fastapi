from pydantic import BaseModel


class ItemBase(BaseModel):
    """
    ItemBase model

    @author Fabien Bellanger
    """

    name: str
    price: float
    is_offer: bool | None = None


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

    id: int

    def display(self) -> str:
        """
        Display item

        Display the name and the price of an item.
        """

        return self.name + " at " + str(self.price)

    class ConfigDict:
        from_attributes = True
