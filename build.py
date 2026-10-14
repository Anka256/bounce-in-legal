"""Bounce In yasal sayfası: index.html (gizlilik politikası), Türkçe + İngilizce.
Metinler burada; sayfa üretilir: python3 build.py
Dil: ?lang=<kod> (oyun tr / en gönderir), yoksa tarayıcı dili, o da yoksa İngilizce.
Düzen Crossblocks'un yasal sayfasıyla aynı (anka256.github.io/crossblocks-legal).
"""
import html

EMAIL = "256games.dev@gmail.com"
LANGS = ["en", "tr"]
NAMES = {"en": "English", "tr": "Türkçe"}
ADS_URL = '<a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a>'

# rows: [(veri, amaç)]
P = {
"en": dict(
 title="Bounce In Privacy Policy", date="Effective date: 14 October 2026",
 intro="This policy explains what information the Bounce In mobile game (\"the game\", \"we\") collects, why, and what choices you have. Bounce In is developed by 256 Games (Onur Kansoy), who is the data controller.",
 h_sum="Summary", sum=[
  "No account, and no real name, email, phone number, contacts, location or photos are collected.",
  "Anonymous usage data is sent only if you turn it on in Settings; it is off by default.",
  "The weekly Tower leaderboard shows a nickname (random by default, you can change it) with your best floor and score.",
  "The game shows optional rewarded ads from Google AdMob only when you choose to watch one."],
 h_col="Information we collect", th=("Data", "Purpose"), rows=[
  ("Random player ID created for your device, nickname, weekly best Tower floor and score", "Weekly Tower leaderboard: ranking you and showing your row"),
  ("Anonymous usage data, only if \"Usage data\" is on: a random install ID, game version, system and language, and game events (for example level started / completed / failed, shots used, stars, floors reached, items bought, ad offers shown and watched, and whether Remove Ads was bought)", "Balancing levels, ads and the game"),
  ("Advertising ID, IP address and device information (collected by Google AdMob)", "Showing and measuring ads and preventing fraud; personalized ads only with your consent where required"),
  ("IP address", "Technically needed to connect to our server; not written to logs or stored with your data")],
 local="Your progress, settings, stars and records are stored on your device.",
 h_share="Sharing", share="We do not sell or rent your data, and we do not share it with advertisers or data brokers. Your nickname, best floor and score for the week are visible to other players on the leaderboard. Ads are provided by Google AdMob, which receives the data described in the Advertising section. The optional Remove Ads purchase is processed by Google Play; we never see your payment details, only whether the purchase was made.",
 h_ads="Advertising",
 ads="The game only shows optional rewarded ads from Google AdMob: when you run out of balls in a level you can choose to watch an ad for extra balls. There are no ads you are forced to watch. Google may collect and use your device's advertising ID, IP address and device information to show and measure ads and to prevent fraud, as described in Google's policy: {url}. In the EEA, the UK and Switzerland, the game asks for your consent with Google's consent form before personalized ads are shown; you can change your choice at any time in <strong>Settings → Privacy options</strong>. You can reset or delete your advertising ID in your device settings.",
 h_sec="Storage and security", sec="Leaderboard and usage data are stored on our server, a virtual private server provided by Natro (Türkiye). Traffic between the game and the server is encrypted (HTTPS), and the game only connects to our server's own certificate.",
 h_ret="Retention and deletion", ret="Usage data is not linked to you: the install ID is random, and turning \"Usage data\" off in Settings stops collection and deletes the ID and any unsent events from your device. Leaderboard entries are kept so weekly rankings stay correct. To have your leaderboard entries deleted, email us with your nickname (shown in <strong>Settings → Nickname</strong>); we delete them within 30 days and reply to confirm. Uninstalling the game removes all data stored on your device.",
 h_rights="Your rights", rights="Depending on where you live (for example under the GDPR or Türkiye's KVKK), you may have the right to access, correct, delete, or object to the processing of your data, and to complain to a data protection authority. To exercise these rights, contact us at the address below and include your nickname.",
 h_kids="Children", kids="The game does not ask for personal information such as names or contact details. We do not knowingly collect personal information from children under 13. If you believe a child has provided personal information (for example in a nickname), contact us and we will delete it.",
 h_chg="Changes", chg="If this policy changes, we will update this page and the effective date above. Significant changes will also be announced in the game.",
 h_contact="Contact"),
"tr": dict(
 title="Bounce In Gizlilik Politikası", date="Yürürlük tarihi: 14 Ekim 2026",
 intro="Bu politika, Bounce In mobil oyununun (\"oyun\", \"biz\") hangi bilgileri neden topladığını ve senin hangi seçeneklere sahip olduğunu açıklar. Oyunun geliştiricisi ve veri sorumlusu 256 Games (Onur Kansoy)'dur.",
 h_sum="Özet", sum=[
  "Hesap yoktur; gerçek ad, e-posta, telefon numarası, rehber, konum ya da fotoğraf toplanmaz.",
  "Anonim kullanım verisi yalnızca Ayarlar'dan açarsan gönderilir; varsayılan olarak kapalıdır.",
  "Haftalık Kule sıralamasında bir takma ad (varsayılan olarak rastgele, değiştirebilirsin), en iyi katın ve puanın görünür.",
  "Oyun, Google AdMob'un isteğe bağlı ödüllü reklamlarını yalnızca sen izlemeyi seçtiğinde gösterir."],
 h_col="Toplanan bilgiler", th=("Veri", "Amaç"), rows=[
  ("Cihazın için oluşturulan rastgele oyuncu kimliği, takma ad, haftalık en iyi Kule katı ve puanı", "Haftalık Kule sıralaması: seni sıralamak ve satırını göstermek"),
  ("Anonim kullanım verisi, yalnızca \"Kullanım verisi\" açıksa: rastgele kurulum kimliği, oyun sürümü, sistem ve dil, oyun olayları (örneğin bölüm başladı / bitti / kaybedildi, kullanılan atış, yıldız, ulaşılan kat, satın alınan nesneler, gösterilen ve izlenen reklam teklifleri, Reklamları kaldır'ın alınıp alınmadığı)", "Bölümleri, reklamları ve oyunu dengelemek"),
  ("Reklam kimliği, IP adresi ve cihaz bilgisi (Google AdMob tarafından toplanır)", "Reklam göstermek ve ölçmek, sahtekârlığı önlemek; kişiselleştirilmiş reklam yalnızca gerektiği yerde onayınla"),
  ("IP adresi", "Sunucumuza bağlanmak için teknik olarak gerekir; günlüklere yazılmaz, verilerinle birlikte saklanmaz")],
 local="İlerlemen, ayarların, yıldızların ve rekorların cihazında saklanır.",
 h_share="Paylaşım", share="Verilerini satmayız, kiralamayız; reklamcılarla ya da veri simsarlarıyla paylaşmayız. Takma adın, haftanın en iyi katı ve puanın sıralamada diğer oyunculara görünür. Reklamlar, Reklamlar bölümünde anlatılan verileri alan Google AdMob tarafından sağlanır. İsteğe bağlı Reklamları kaldır satın alması Google Play tarafından işlenir; ödeme bilgilerini hiç görmeyiz, yalnızca satın almanın yapılıp yapılmadığını biliriz.",
 h_ads="Reklamlar",
 ads="Oyun yalnızca Google AdMob'un isteğe bağlı ödüllü reklamlarını gösterir: bir bölümde topların bitince, ek top için reklam izlemeyi seçebilirsin. İzlemeye zorlandığın reklam yoktur. Google, reklam göstermek ve ölçmek ve sahtekârlığı önlemek için cihazının reklam kimliğini, IP adresini ve cihaz bilgilerini toplayıp kullanabilir; ayrıntılar Google'ın politikasında: {url}. AEA, Birleşik Krallık ve İsviçre'de oyun, kişiselleştirilmiş reklam göstermeden önce Google'ın onay formuyla onayını ister; seçimini istediğin zaman <strong>Ayarlar → Gizlilik seçenekleri</strong> bölümünden değiştirebilirsin. Reklam kimliğini cihazının ayarlarından sıfırlayabilir ya da silebilirsin.",
 h_sec="Saklama ve güvenlik", sec="Sıralama ve kullanım verileri, Natro (Türkiye) tarafından sağlanan sanal sunucumuzda saklanır. Oyunla sunucu arasındaki trafik şifrelidir (HTTPS) ve oyun yalnızca sunucumuzun kendi sertifikasına bağlanır.",
 h_ret="Saklama süresi ve silme", ret="Kullanım verisi seninle ilişkilendirilmez: kurulum kimliği rastgeledir; Ayarlar'da \"Kullanım verisi\"ni kapatmak toplamayı durdurur, kimliği ve gönderilmemiş olayları cihazından siler. Sıralama kayıtları, haftalık sıralamalar doğru kalsın diye saklanır. Sıralama kayıtlarının silinmesini istersen takma adınla (<strong>Ayarlar → Takma ad</strong> bölümünde görünür) bize e-posta gönder; 30 gün içinde siler ve onay yanıtı göndeririz. Oyunu kaldırmak cihazında saklanan tüm verileri siler.",
 h_rights="Hakların", rights="KVKK ve GDPR gibi mevzuat kapsamında verilerine erişme, düzeltme, silme, işlenmesine itiraz etme ve veri koruma otoritesine şikâyette bulunma hakkına sahip olabilirsin. Bu hakları kullanmak için aşağıdaki adrese takma adını yazarak başvurabilirsin.",
 h_kids="Çocuklar", kids="Oyun ad veya iletişim bilgisi gibi kişisel bilgiler istemez. 13 yaşından küçük çocuklardan bilerek kişisel bilgi toplamayız. Bir çocuğun kişisel bilgi verdiğini düşünüyorsan (örneğin takma adda) bize yaz, sileriz.",
 h_chg="Değişiklikler", chg="Bu politika değişirse bu sayfayı ve yukarıdaki tarihi güncelleriz. Önemli değişiklikler oyunda da duyurulur.",
 h_contact="İletişim"),
}

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="google" content="notranslate">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
<nav><label>🌐 <select id="lang" aria-label="Language">{options}</select></label></nav>
"""

SCRIPT = """</main>
<script>
// dil: ?lang= (oyun tr / en gönderir) ya da tarayıcı dili; yoksa İngilizce
(function(){
  var langs = %s;
  function pick(v){ v = (v || "").toLowerCase().replace("_", "-").split("-")[0]; return langs.indexOf(v) >= 0 ? v : "en"; }
  function show(l){
    document.documentElement.lang = l;
    langs.forEach(function(x){ document.getElementById(x).hidden = x !== l; });
    document.getElementById("lang").value = l;
    var t = document.getElementById(l).getAttribute("data-title"); if (t) document.title = t;
  }
  var q = new URLSearchParams(location.search).get("lang");
  show(pick(q || navigator.language));
  document.getElementById("lang").addEventListener("change", function(e){
    show(e.target.value); history.replaceState(null, "", "?lang=" + e.target.value);
  });
})();
</script>
</body>
</html>
""" % str(LANGS).replace("'", '"')


def privacy():
    opts = "".join('<option value="%s">%s</option>' % (l, NAMES[l]) for l in LANGS)
    out = [HEAD.format(title=P["en"]["title"], options=opts)]
    for l in LANGS:
        p = P[l]
        rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (html.escape(a), html.escape(b)) for a, b in p["rows"])
        out.append(f'''<section id="{l}" lang="{l}" data-title="{html.escape(p['title'])}"{' hidden' if l != 'en' else ''}>
<h1>{html.escape(p['title'])}</h1>
<p class="muted">{html.escape(p['date'])}</p>
<p>{html.escape(p['intro'])}</p>
<h2>{p['h_sum']}</h2>
<ul>{''.join('<li>%s</li>' % html.escape(x) for x in p['sum'])}</ul>
<h2>{p['h_col']}</h2>
<div class="wrap"><table><tr><th>{p['th'][0]}</th><th>{p['th'][1]}</th></tr>{rows}</table></div>
<p>{html.escape(p['local'])}</p>
<h2>{p['h_share']}</h2>
<p>{html.escape(p['share'])}</p>
<h2>{p['h_ads']}</h2>
<p>{p['ads'].replace('{url}', ADS_URL)}</p>
<h2>{p['h_sec']}</h2>
<p>{html.escape(p['sec'])}</p>
<h2>{p['h_ret']}</h2>
<p>{p['ret']}</p>
<h2>{p['h_rights']}</h2>
<p>{html.escape(p['rights'])}</p>
<h2>{p['h_kids']}</h2>
<p>{html.escape(p['kids'])}</p>
<h2>{p['h_chg']}</h2>
<p>{html.escape(p['chg'])}</p>
<h2>{p['h_contact']}</h2>
<p>256 Games (Onur Kansoy) — <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</section>
''')
    out.append(SCRIPT)
    return "".join(out)


if __name__ == "__main__":
    assert set(P) == set(LANGS)
    for l in LANGS:
        assert set(P[l]) == set(P["en"]), l
        assert len(P[l]["rows"]) == len(P["en"]["rows"]), l
    open("index.html", "w").write(privacy())
    print("ok:", len(LANGS), "languages")
