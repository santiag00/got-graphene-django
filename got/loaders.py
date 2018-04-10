from promise.dataloader import DataLoader as BaseDataLoader


def get_data_loader(data_loader_class, request):
    """
    Inspects the data_loaders dict attribute on the request
    and the keys contained within data_loaders to get or created
    the instance of the data_loader_class called.
    It then retuns the data_loader instance.
    """
    if not hasattr(request, 'data_loaders'):
        request.data_loaders = {}

    key = data_loader_class.__name__
    if key in request.data_loaders:
        return request.data_loaders[key]

    data_loader = data_loader_class(request)
    request.data_loaders[key] = data_loader
    return data_loader


class DataLoader(BaseDataLoader):
    """
    "JOOR" data loader with access to the request object as
     many of the fields are calculated from the request
    """

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
