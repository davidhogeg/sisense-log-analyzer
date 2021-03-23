import json
from datetime import datetime


def parse_monitor_entry(timestamp=None, namespace=None, service=[], x_req=[], monitor_info=[]):
    # service=[], , mon_info=None, Rest=[]):
    # print("---------")
    # print(monitor_info)
    new_entry = {
        "timestamp": "".join(timestamp),
        "timestamp_ms": get_epoch_timestamp("".join(timestamp)),
        "namespace": "".join(namespace),
        "service": "".join(service),
        "x-request-id": "".join(x_req),
        "type": "MONITOR"
    }

    j = json.loads(monitor_info[0])
    # return new_entry
    return {**new_entry, **j}


def get_namespace(Namespace=None):
    ns = Namespace
    return ns


def get_epoch_timestamp(t=None):
    dt = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S.%f')
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0


def parse_info_entry(timestamp=None, namespace=None, service=[], x_req=[], rest_req=[]):
    # print("*******")
    #     Pattern: <Timestamp> [\s|,]* <Namespace> [\s|,]* <Service>.*\[INFO\] .* \[<X_req>\] .*\[ <REST_Request> \]
    new_entry = {
        "timestamp": "".join(timestamp),
        "timestamp_ms": get_epoch_timestamp("".join(timestamp)),
        "namespace": "".join(namespace),
        "service": "".join(service),
        "x-request-id": "".join(x_req),
        "type": "INFO",
        "is_start": True if rest_req[0] == "Start" else False,
        "is_finish": True if rest_req[0] == "Finish" else False,
        "rest_request_type": rest_req[1],
        "rest_request_endpoint": rest_req[2]
    }

    return new_entry


functions = {
    # 'Timestamp_1': get_timestamp,
    # 'Namespace': get_namespace,
    "Monitor Entry": parse_monitor_entry,
    "Info Entry": parse_info_entry
}
