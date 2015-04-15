from haystack.forms import SearchForm


class CamSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()