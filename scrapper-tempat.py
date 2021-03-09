import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tweepy import OAuthHandler, Stream, StreamListener
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="zj6hOR9GXVJYt2lr2FZKU1Q1G"
consumer_secret="0bXsZryRQixl5rvHSbfJYQnvGJirsCH0K6CV1XNz7efBT4fUgo"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1184880065546313728-TZIL5FB0fvMwTAWEEjyUY7TaO2tVVl"
access_token_secret="F7KiOSvS1qMGFoG0wMvcQ6IFoB310eG9qxGkwNomWSiqb"

# Use a service account
cred = credentials.Certificate('login.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        # print(data)
        json_data = json.loads(data)
        doc_name= json_data["id_str"]
        doc_ref = db.collection(u'tweet-tempat-bdg').document(u''+doc_name)
        doc_ref.set(json_data)
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True

# doc_ref = db.collection(u'users').document(u'alovelace2')
# doc_ref.set({
#     u'first': u'Ada2',
#     u'last': u'Lovelace',
#     u'born': 1815
# })


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Campaka','Ciroyom','Dunguscariang','dungus cariang',
    'Garuda','Kebonjeruk','kebon jeruk','Maleber','Cibadak','Karanganyar',
    'karang anyar','Karasak','Nyengseret','Panjunan','Pelindunghewan','pelindung hewan',
    'inhoftank','Antapani','Cisaranten','Sukamiskin','suka miskin','Babakan','Babakanciparay',
    'babakan ciparay','Cirangrang','Margahayu Utara','Margasuka','marga suka','Sukahaji',
    'suka haji','Batununggal','Kujangsari','Mengger','Wates','Caringin','Cibuntu','Cigondewah',
    'Cijerah','Gempolsari','gempol sari','Warungmuncang','warung muncang','Cihapit','Citarum',
    'Tamansari','taman sari','Binong','Cibangkong','Gumuruh','Kacapiring','Kebongedang','kebon gedang',
    'Kebonwaru','kebon waru','Maleer','Samoja','Babakan Asih','Babakan Tarogong','Jamika','Kopo',
    'Suka Asih','sukaasih','Cibaduyut','Kebon Lega','kebon lega','Mekarwangi','mekar wangi','Situsaeur',
    'situ saeur','Cijawura','Jatisari','Margasari','marga sari','Sekejati','Cigadung','Cihaurgeulis',
    'Neglasari','Sukaluyu','Cicadas','Cikutra','Padasuka','Pasirlayung','pasir layung','Sukamaju',
    'Sukapada','Cipadung','Cisurupan','Palasari','Pasirbiru','pasir biru','Arjuna','Husen Sastranegara',
    'husain sastranegara','bandara husen','bandara husain','bdo','Pajajaran','Pamoyanan','Pasirkaliki',
    'pasir kaliki','Sukaraja','Ciumbuleuit','Hegarmanah','hegar manah','Ledeng','Babakan Penghulu',
    'Pakemitan','Sukamulya','Cipaganti','Dago','Lebakgede','lebak gede','Lebaksiliwangi','lebak siliwangi',
    'Sadangserang','sadang serang','Sekeloa','Cimincrang','Cisaranten','Rancabolang','ranca bolang',
    'Rancanumpang','ranca numpang','Babakansari','babakan sari','Babakansurabaya','babakan surabaya',
    'Cicaheum','Compreng','Kebonkangkung','kebon kangkung','Kebunjayanti','kebun jayanti','kebonjayanti',
    'kebon jayanti','jayanti','Sukapura','suka pura','Burangrang','Cijagra','Cikawao','Lingkar Selatan',
    'Malabar','Paledang','Turangga','Jatihandap','jati handap','Karangpamulang','karang pamulang',
    'Pasir Impun','Sindangjaya','sindang jaya','Cipadung ','Mekarmulya','mekar mulya','Cipamokolan',
    'Darwati','Manjahlega','Mekar Jaya','mekarjaya','Ancol','Balonggede','balong gede','Ciateul',
    'Cigereleng','Ciseureuh','Pasirluyu','pasir luyu','Pungkur','Cipedes','Pasteur','Sukabungah','Sukagalih',
    'Sukawarna','Gegerkalong','geger kalong','Isola','Sarijadi','Sukarasa','Babakanciamis',
    'babakan ciamis','Braga','Kebonpisang','kebon pisang','Merdeka','Cigending','Pasanggrahan',
    'Pasirendah','pasir endah','Pasirjati','pasir jati','Pasirwangi','pasir wangi','Andir',
    'Astana Anyar','Antapani','antafunny','anta funny','Arcamanik','Babakan Ciparay','Bandung',
    'bdg','Batununggal','Bojongloa ','Buahbatu','bubat','Cibeunying ','Cibiru','Cicendo','Cidadap',
    'Cinambo','Coblong','Gedebage','gede bage','gd bage','gdbage','Kiaracondong','kiara condong',
    'kircon','Lengkong','Mandalajati','mandala jati','Panyileukan','Rancasari','Regol','Sukajadi',
    'Sukasari','Sumur Bandung','sumurbandung','Ujungberung','ujung berung'])