from future.utils import iteritems
from kubernetes   import config as k8s_config
from kubernetes   import client as k8s_client
from kubernetes   import watch  as k8s_watch


class K8SCoreV2Api(k8s_client.CoreV1Api):

    def watch_namespaced_pod(self, name, namespace, **kwargs):

        all_params = ['name', 'namespace', 'pretty', 'watch']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_namespaced_pod" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `read_namespaced_pod`")
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params) or (params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `read_namespaced_pod`")

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))
        if 'watch' in params:
            query_params.append(('watch', params['watch']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
        select_header_accept(['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf',
            'application/json;stream=watch', 'application/vnd.kubernetes.protobuf;stream=watch'])


        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['BearerToken']

        return self.api_client.call_api('/api/v1/watch/namespaces/{namespace}/pods/{name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='V1Pod',
                                        auth_settings=auth_settings,
                                        async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)[0]



def main():
    k8s_config.load_incluster_config()
    k8s_core_client = K8SCoreV2Api()

    watch = k8s_watch.Watch()

    for e in watch.stream(k8s_core_client.watch_namespaced_pod, name="pod-name", namespace="api"):
        print(e)
        #watch.stop()

if __name__ == "__main__":
    main()
