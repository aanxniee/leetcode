class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def formatEmail(email):

            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")

            return local + "@" + domain

        ans = set()

        for email in emails:
            formattedEmail = formatEmail(email)
            ans.add(formattedEmail)

        return len(ans)
        