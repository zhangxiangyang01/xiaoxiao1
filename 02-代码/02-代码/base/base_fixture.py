def deal_fixture(self, em):
    for fixture_case_id in em.fixture.split():
        if fixture_case_id.startswith("add"):
            self.test_case_add(fixture_case_id)
        elif fixture_case_id.startswith("query"):
            self.test_case_query(fixture_case_id)
        elif fixture_case_id.startswith("update"):
            self.test_case_update(fixture_case_id)
