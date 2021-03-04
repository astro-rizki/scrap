import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
# project_id = "superweather-app"
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#   'projectId': project_id,
# })

# Use a service account
cred = credentials.Certificate('login.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'users').document(u'alovelace2')
doc_ref.set({
    u'first': u'Ada2',
    u'last': u'Lovelace',
    u'born': 1815
})

doc_ref = db.collection(u'users').document(u'aturing2')
doc_ref.set({
    u'first': u'Alan2',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})
