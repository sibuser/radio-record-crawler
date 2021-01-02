import os
import re

from scrapy.pipelines.files import FilesPipeline
import urllib.parse


class Mp3FilePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name: str = re.sub(r"\d\d:\d\d:\d\d - ", '',
                                urllib.parse.unquote(request.url.split("/")[-1])).replace("\'", "")
        folder: str = request.url.split("/")[-3]

        return os.path.join(folder, file_name)
