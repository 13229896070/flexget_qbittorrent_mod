from ..schema.site_base import SignState, Work
from ..schema.unit3d import Unit3D


class MainClass(Unit3D):
    URL = 'https://jptv.club/'
    USER_CLASSES = {
        'uploaded': [10995116277760],
        'days': [365]
    }

    @classmethod
    def build_workflow(cls):
        return [
            Work(
                url='/',
                method='get',
                succeed_regex='<title>JPTVclub - JPTV for everyone!</title>',
                fail_regex=None,
                check_state=('final', SignState.SUCCEED),
                is_base_content=True
            )
        ]

    def build_selector(self):
        selector = super(MainClass, self).build_selector()
        return selector
