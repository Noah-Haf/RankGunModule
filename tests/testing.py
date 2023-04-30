import rankgun 
import sys

Api_Token = sys.argv[0]

Workspace = rankgun.RankGunAPI(Api_Token, 1)

Attempt1 = Workspace.promote(username="RankGunTests")
Attempt2 = Workspace.demote(username="RankGunTests")

if Attempt1["status_code"] != 200 or Attempt2["status_code"] != 200: 
    raise("Something went wrong")
else:
    print("All went well")
