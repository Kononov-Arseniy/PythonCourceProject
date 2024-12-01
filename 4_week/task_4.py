'''
https://leetcode.com/problems/subdomain-visit-count/?envType=problem-list-v2&envId=array
'''

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        time_map = {}
        for cpdomain in cpdomains:
            strings = cpdomain.split(" ")
            times = int(strings[0])
            domains = strings[1].split(".")
            start_index = 0
            for i in range(len(domains)):
                if i > 0:
                    start_index += len(domains[i - 1]) + 1
                s = strings[1][start_index:]
                if s in time_map:
                    time_map[s] += times
                else:
                    time_map[s] = times
        result_list = []
        for key in time_map.keys():
            item = str(time_map[key]) + " " + key
            result_list.append(item)
        return result_list
