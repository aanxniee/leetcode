class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def formatEmail(email):
            
            local, domain = email.split("@")
            
            if "+" in local:
                local = local.split("+")[0]

            local = local.replace(".", "")

            print(local + "@" + domain)
            return local + "@" + domain

        ans = []

        for email in emails:
            formattedEmail = formatEmail(email)
            
            if formattedEmail not in ans:
                ans.append(formattedEmail)

        return len(ans)
        