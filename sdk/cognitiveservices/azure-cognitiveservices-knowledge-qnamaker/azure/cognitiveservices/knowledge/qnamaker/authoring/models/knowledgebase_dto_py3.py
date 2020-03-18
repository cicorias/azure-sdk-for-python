# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class KnowledgebaseDTO(Model):
    """Response schema for CreateKb operation.

    :param id: Unique id that identifies a knowledgebase.
    :type id: str
    :param host_name: URL host name at which the knowledgebase is hosted.
    :type host_name: str
    :param last_accessed_timestamp: Time stamp at which the knowledgebase was
     last accessed (UTC).
    :type last_accessed_timestamp: str
    :param last_changed_timestamp: Time stamp at which the knowledgebase was
     last modified (UTC).
    :type last_changed_timestamp: str
    :param last_published_timestamp: Time stamp at which the knowledgebase was
     last published (UTC).
    :type last_published_timestamp: str
    :param name: Friendly name of the knowledgebase.
    :type name: str
    :param user_id: User who created / owns the knowledgebase.
    :type user_id: str
    :param urls: URL sources from which Q-A were extracted and added to the
     knowledgebase.
    :type urls: list[str]
    :param sources: Custom sources from which Q-A were extracted or explicitly
     added to the knowledgebase.
    :type sources: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'host_name': {'key': 'hostName', 'type': 'str'},
        'last_accessed_timestamp': {'key': 'lastAccessedTimestamp', 'type': 'str'},
        'last_changed_timestamp': {'key': 'lastChangedTimestamp', 'type': 'str'},
        'last_published_timestamp': {'key': 'lastPublishedTimestamp', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'urls': {'key': 'urls', 'type': '[str]'},
        'sources': {'key': 'sources', 'type': '[str]'},
    }

    def __init__(self, *, id: str=None, host_name: str=None, last_accessed_timestamp: str=None, last_changed_timestamp: str=None, last_published_timestamp: str=None, name: str=None, user_id: str=None, urls=None, sources=None, **kwargs) -> None:
        super(KnowledgebaseDTO, self).__init__(**kwargs)
        self.id = id
        self.host_name = host_name
        self.last_accessed_timestamp = last_accessed_timestamp
        self.last_changed_timestamp = last_changed_timestamp
        self.last_published_timestamp = last_published_timestamp
        self.name = name
        self.user_id = user_id
        self.urls = urls
        self.sources = sources