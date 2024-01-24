"""
map transaction time to person to location
for each transaction check if amount is valid
for each transaction check if time is valid
for each transaction check if it happened by same person in diff city
"""

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalid = []

        # { name : [time, amount, city]}
        hmap = defaultdict(list)

        # build the transaction mapping
        for t in transactions:
            name, time, amount, city = t.split(",")
            time = int(time)
            hmap[name].append([time, amount, city])

        print(hmap)
        # check every transaction
        for t in transactions:
            name, time, amount, city = t.split(",")
            time = int(time)

            # transaction is invalid if amount > 1000
            if int(amount) > 1000:
                invalid.append(t)
                continue
            
            # check each transaction under the current name
            for i in hmap[name]:
                time_i, amount_i, city_i = i
                time_i = int(time_i)

                # if the transaction occured in a different city within less than 60 mins of the current transaction, it is invalid
                if city != city_i and abs(time - time_i) <= 60:
                    invalid.append(t)
                    break

        return invalid



        
        