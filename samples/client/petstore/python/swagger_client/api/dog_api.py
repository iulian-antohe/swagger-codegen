# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_dog(self, body, **kwargs):  # noqa: E501
        """Add a new dog to the store  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_dog(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Dog body: Dog object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_dog_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_dog_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_dog_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add a new dog to the store  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_dog_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Dog body: Dog object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_dog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_dog`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dog', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dog(self, dog_id, **kwargs):  # noqa: E501
        """Deletes a dog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dog(dog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int dog_id: Dog id to delete (required)
        :param str api_key:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_dog_with_http_info(dog_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dog_with_http_info(dog_id, **kwargs)  # noqa: E501
            return data

    def delete_dog_with_http_info(self, dog_id, **kwargs):  # noqa: E501
        """Deletes a dog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dog_with_http_info(dog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int dog_id: Dog id to delete (required)
        :param str api_key:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dog_id', 'api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dog_id' is set
        if ('dog_id' not in params or
                params['dog_id'] is None):
            raise ValueError("Missing the required parameter `dog_id` when calling `delete_dog`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dog_id' in params:
            path_params['dogId'] = params['dog_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dog/{dogId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dog_by_id(self, dog_id, **kwargs):  # noqa: E501
        """Find dog by ID  # noqa: E501

        Returns a single dog  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dog_by_id(dog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int dog_id: ID of dog to return (required)
        :return: Dog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dog_by_id_with_http_info(dog_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dog_by_id_with_http_info(dog_id, **kwargs)  # noqa: E501
            return data

    def get_dog_by_id_with_http_info(self, dog_id, **kwargs):  # noqa: E501
        """Find dog by ID  # noqa: E501

        Returns a single dog  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dog_by_id_with_http_info(dog_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int dog_id: ID of dog to return (required)
        :return: Dog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dog_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dog_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dog_id' is set
        if ('dog_id' not in params or
                params['dog_id'] is None):
            raise ValueError("Missing the required parameter `dog_id` when calling `get_dog_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dog_id' in params:
            path_params['dogId'] = params['dog_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dog/{dogId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dog(self, body, **kwargs):  # noqa: E501
        """Update an existing dog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dog(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Dog body: Dog object that needs to be added. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dog_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dog_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_dog_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update an existing dog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dog_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Dog body: Dog object that needs to be added. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dog`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dog', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dog_with_form(self, animal_id, **kwargs):  # noqa: E501
        """Updates a dog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dog_with_form(animal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int animal_id: ID of dog that needs to be updated (required)
        :param str name:
        :param str status:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_dog_with_form_with_http_info(animal_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dog_with_form_with_http_info(animal_id, **kwargs)  # noqa: E501
            return data

    def update_dog_with_form_with_http_info(self, animal_id, **kwargs):  # noqa: E501
        """Updates a dog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_dog_with_form_with_http_info(animal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int animal_id: ID of dog that needs to be updated (required)
        :param str name:
        :param str status:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['animal_id', 'name', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dog_with_form" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'animal_id' is set
        if ('animal_id' not in params or
                params['animal_id'] is None):
            raise ValueError("Missing the required parameter `animal_id` when calling `update_dog_with_form`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'animal_id' in params:
            path_params['animalId'] = params['animal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
              # noqa: E501
        if 'status' in params:
              # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/dog/{dogId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
