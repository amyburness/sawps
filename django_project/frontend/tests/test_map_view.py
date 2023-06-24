from frontend.views.map import MapView
from django_project.frontend.tests.base_view import RegisteredBaseViewTestBase


class TestHomeView(RegisteredBaseViewTestBase):
    view_name = 'map'
    view_cls = MapView

    def test_organisation_selector(self):
        self.do_test_anonymous_user()
        self.do_test_superuser()
        self.do_test_user_with_organisations()
        self.do_test_user_without_organisation()