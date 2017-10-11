import os
import pytest


@pytest.fixture(params=['normal', 'MixedCase'])
def mix(request):
    return request.param


@pytest.fixture
def bin(tmpdir, mix):
    return tmpdir.ensure(mix, 'bin', dir=1)


@pytest.fixture
def home(tmpdir, mix):
    return tmpdir.ensure(mix, 'venvs', dir=1)


@pytest.fixture
def pkgindex(monkeypatch):
    index = os.path.abspath(os.path.join(os.path.dirname(__file__), 'packages'))
    monkeypatch.setenv('PIP_NO_INDEX', '1')
    monkeypatch.setenv('PIP_FIND_LINKS', index)

