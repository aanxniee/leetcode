from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        cdp = defaultdict(int)

        for d in cpdomains:
            count, domain = d.split()
        
            while "." in domain:
                cdp[domain] += int(count)

                domain = domain.split(".", 1)[-1]

            cdp[domain] += int(count)
 
        ans = []
        for k in cdp:
            ans.append(str(cdp[k]) + " " + k)

        return ans
