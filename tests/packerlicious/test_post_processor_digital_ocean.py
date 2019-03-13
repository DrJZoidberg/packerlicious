import pytest

import packerlicious.post_processor as post_processor


class TestDigitalOceanImporterPostProcessor(object):

    def test_required_fields_missing(self):
        b = post_processor.DigitalOceanImporter()

        with pytest.raises(ValueError) as excinfo:
            b.to_dict()
        assert 'required' in str(excinfo.value)
