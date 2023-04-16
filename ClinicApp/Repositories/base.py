from ClinicApp.helpers.model_search import get_or_none, filter_or_none


class BaseRepository:
    item = None
    item_list = None
    model = None

    def __init__(
            self, *args, model=None, item=None, many=False, item_list=None, **kwargs
    ):
        self.model = model
        if not model:
            raise ReferenceError("Model Instance Not Defined")
        # Get a single Object
        if not item and not many:
            item = get_or_none(self.model, *args, **kwargs)
        self.item = item

        # Get a list or queryset of objects
        # FIXME: if we get an empty queryset here like so:
        #   # some_existing_queryset: <QuerySet: []>
        #   some_repo = SomeRepo(item_list=some_existing_queryset, many=True)
        #   it will select all model items like SELECT *
        if many and not item_list:
            item_list = filter_or_none(self.model, *args, **kwargs)
        self.item_list = item_list
        # if not item and not item_list:
        #     raise ValueError(f"No {self.model} or {self.model} List Found")

    ### TODO prefetch related and select related is not working for now, find a solution for later
    # def prefetch_related(self, *args):
    #     """Extension of the default prefetch_related method to use on item and item_list."""
    #     if self.item:
    #         self.item = self.item.prefetch_related(*args)
    #     if self.item_list:
    #         self.item_list = self.item_list.objects.prefetch_related(*args)

    # def select_related(self, *args):
    #     """Extension of the default select_related method to use on item and item_list."""
    #     if self.item:
    #         self.item = self.item.select_related(*args)
    #     if self.item_list:
    #         self.item_list = self.item_list.select_related(*args)