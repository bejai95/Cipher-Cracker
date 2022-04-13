import pytest
from transpositionHacker import transpositionHacker

invalid1CipherText = "wgrg wefwe fdgo u efnd rogdg owieo ewofiwao w"
invalid2CipherText = "Sed tristique laoreet lacus, eu."
invalid3CipherText = "Donec erat est, posuere eu nulla ut, hendrerit maximus felis."

invalid4CipherText = "Mauris risus lorem, dictum in malesuada non, congue sit amet lorem. Integer ac turpis ex. Sed faucibus enim eu tincidunt."

invalid5CipherText = "Donec feugiat ipsum eu elit fermentum hendrerit. Nullam semper neque lorem. Nulla auctor, massa ut euismod volutpat, ligula lacus mattis urna, a luctus mi massa nec nisl. Sed sed maximus arcu, quis accumsan purus. Maecenas fringilla lorem ut felis placerat."

invalid6CipherText = "Cras egestas cursus orci ut aliquet. Praesent semper eros libero, varius sagittis velit pellentesque sit amet. Nullam elit massa, malesuada eu pulvinar nec, euismod ut dolor. Nam rhoncus quis nisi id pharetra. Donec eu dolor eget eros maximus posuere. Ut eget turpis feugiat, bibendum sapien non, condimentum ante. In blandit dui at tincidunt laoreet. Vivamus egestas mauris at egestas posuere. Nullam interdum fermentum augue. Nulla quam elit, commodo ut nulla in, congue facilisis mauris. Donec lobortis aliquet tellus, nec fermentum."

valid1PlainText = "Common sense is not so common."
valid1CipherText = "Cenoonommstmme oo snnio. s s c"

valid2PlainText = """Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. Considered a "father of the computer", Babbage is credited with inventing the first mechanical computer that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbage's original plans. Built to tolerances achievable in the 19th century, the success of the finished engine indicated that Babbage's machine would have worked. Nine years later, the Science Museum completed the printer Babbage had designed for the difference engine."""

valid2CipherText = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

valid3PlainText = """Why do Americans have so many different types of towels? We have beach towels, hand towels, bath towels, dish towels, camping towels, quick-dry towels, and let’s not forget paper towels. Would 1 type of towel work for each of these things? Let’s take a beach towel. It can be used to dry your hands and body with no difficulty. A beach towel could be used to dry dishes. Just think how many dishes you could dry with one beach towel. I’ve used a beach towel with no adverse effects while camping. If you buy a thin beach towel it can dry quickly too. I’d probably cut up a beach towel to wipe down counters or for cleaning other items, but a full beach towel could be used too. Is having so many types of towels an extravagant luxury that Americans enjoy or is it necessary? I’d say it's overkill and we could cut down on the many types of towels that manufacturers deem necessary."""

valid3CipherText = """WethaemdsoocLo nilrku stsy ibounao svm a ntu.h yanlpr wfhewtdc y  beh otclwng uh aeiyw oryspvdsiyne  teo uc hced wuokyet flaogrt etwe oee ,n olto’l blodooa nh wl leoudvfai i herd s t gttsofs.dotuiwucaoibeyc rtl i ncntcelsom bod o .w   rdyls lh  lul utshlbnttae'o s  aoewitwf ettIyy.dhmd baey tto e ego ncsum dAnfaesoeoWlhat    ea ted  io  orb  wlse latemy clhwlro ek ywAbsndoavcatouwr euseu sodnhee ths esguwsecoi e.yrwcea  .pi iasolxesv yamrdo ,tl,eloe autb   yehrmtc  pftce sunaec t iiwt os tdr anrheuJd l sphaIaeoehdm rjrrut ncfeobw,a  kt    asuiw.teiin’  rm  aayoyktymeaflwae np1 hbbhncessi o nn dbd sttnn y?i pacnesetlqda fieeaohdthtIweg d eoc,ooy t  ldenesr?lhsu ptona n    eh’ef.brpawl wo ehoIlosus e s ,ileyrgcuddttts vlf eyrcnebe.txar’ w fshnW,t cerp shssiooh oe eIa oh aul ytt danoaaate ockt ee? e fw iyn wcfcqb cnt Ipr i n fcrv  hwa-’t a tdafednoeuit huatoi cseaAssdo ty"""

def testInvalid1():
    data = transpositionHacker(invalid1CipherText)
    assert "message" in data.keys()

def testInvalid2():
    data = transpositionHacker(invalid2CipherText)
    assert "message" in data.keys()

def testInvalid3():
    data = transpositionHacker(invalid3CipherText)
    assert "message" in data.keys()

def testInvalid4():
    data = transpositionHacker(invalid4CipherText)
    assert "message" in data.keys()

def testInvalid5():
    data = transpositionHacker(invalid5CipherText)
    assert "message" in data.keys()

def testInvalid6():
    data = transpositionHacker(invalid6CipherText)
    assert "message" in data.keys()

def testValid1():
    data = transpositionHacker(valid1CipherText)
    assert data["plainText"] == valid1PlainText
    assert data["key"] == 8

def testValid2():
    data = transpositionHacker(valid2CipherText)
    assert data["plainText"] == valid2PlainText
    assert data["key"] == 10

def testValid3():
    data = transpositionHacker(valid3CipherText)
    assert data["plainText"] == valid3PlainText
    assert data["key"] == 20