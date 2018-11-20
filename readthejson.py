#!/usr/bin/env python3

import json
from collections import Counter


def main():

    json_filename = input("\nEnter a JSON filename to load: ")
    with open(json_filename) as json_file:
        content = json.load(json_file)

    source_ip_amount = Counter()

    for item in content["tickets"]:
        for key, value in item.items():
            if key == "src_ip":
                source_ip_amount.update([value])

    print(f"\nThis is the counter with unique IPs: {source_ip_amount}\n")

    targeting_ip = input("\nEnter an IP address from the" +
                         " list to view how many destinations it targeted: ")

    unique_ip_counter = []
    unique_ip_addresses_targeted = 0
    for item in content["tickets"]:
        item = item.items()
        for key, value in item:
            if key == "src_ip" and value == targeting_ip:
                for key, value in item:
                    if key == "dst_ip" and value not in unique_ip_counter:
                        unique_ip_counter.append(value)
                        unique_ip_addresses_targeted += 1

    print(f"\n{unique_ip_addresses_targeted} unique IP addresses targeted")

    unique_ip_files_rcvd = Counter()

    for item in content["tickets"]:
        for key, value in item.items():
            if key == "file_hash":
                unique_ip_files_rcvd.update([value])

    unique_ip_files_rcvd = dict(unique_ip_files_rcvd)
    unique_ip_files_rcvd = list(unique_ip_files_rcvd.values())
    sum_list = 0
    for i in unique_ip_files_rcvd:
        sum_list = sum_list + i
    calc_avg = sum_list / len(unique_ip_files_rcvd)
    print("\nThe average calculation is: %.2f\n" % calc_avg)


if __name__ == "__main__":
    main()
