from pprint import pprint
from kubernetes import config as k8s_config
from kubernetes import client as k8s_client

class K8SCoreV2Api(k8s_client.CoreV1Api):
    pass

def main():
    #k8s_config.load_incluster_config()
    k8s_core_client = K8SCoreV2Api()

    response = k8s_core_client.list_namespaced_pod("default")
    pprint(response)

if __name__ == "__main__":
    main()
