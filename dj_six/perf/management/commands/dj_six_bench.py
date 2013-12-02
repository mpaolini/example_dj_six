'''
Benchmark django
'''
import time
from optparse import make_option

from django.core.management.base import NoArgsCommand, CommandError
from dj_six.perf.client import delete_items, post_item, get_item


class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('--n-items',
            type=int,
            default=100,
            help='number of items created in the benchmark'),
        make_option('--url',
            help='base url'),
        )

    def handle_noargs(self, **opts):
        url = opts.get('url')
        if not url:
            raise CommandError('url parameter is required')
        # Delete all items
        delete_items(url)
        n_items = opts['n_items']
        # Post item
        start = time.time()
        for i in range(n_items):
            post_item(url, i, 'item {}'.format(i))
        dur_post = time.time() - start
        # Get item
        start = time.time()
        for i in range(n_items):
            get_item(url, i)
        dur_get = time.time() - start
        return 'POST: {} GET: {}'.format(dur_post * 1000 / n_items,
                                         dur_get * 1000 / n_items)
