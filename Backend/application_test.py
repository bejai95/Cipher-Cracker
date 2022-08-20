import pytest
import requests

baseURL = "https://api.ciphercracker.click/"

caesar1CipherText = "Ny bfx f htshjwsnsl ijajqturjsy ymfy mj htzqis'y ljy tzy tk mnx rnsi. Mj'i mfi rfsd kwnjsix ymwtzlmtzy mnx jfwqd djfwx fsi mfi ktsi rjrtwnjx tk uqfdnsl bnym ymjr, gzy mj htzqis'y zsijwxyfsi mtb ny mfi fqq xytuuji. Ymjwj bfx xtrj utnsy fx mj lwjb zu ymfy mj uqfdji bnym jfhm tk mnx kwnjsix ktw ymj ajwd qfxy ynrj, fsi mj mfi st nijf ymfy ny btzqi gj ymj qfxy."

caesar1PlainText = "It was a concerning development that he couldn't get out of his mind. He'd had many friends throughout his early years and had fond memories of playing with them, but he couldn't understand how it had all stopped. There was some point as he grew up that he played with each of his friends for the very last time, and he had no idea that it would be the last."

caesar2CipherText = "RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D, GOBOX'D, GYX'D. RO'N, S'N, CRO'N+ DROI'N- GO'N ioc RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D, GOBOX'D, GYX'D. RO'N, S'N, CRO'N+ DROI'N- GO'N ioc RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D GOBOX'D, GYX'D. RO'N, S'N, CRO')(*&&^%$#@!N DROI'!@#$%^&*()N- GO'N ioc xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn"

caesar2PlainText = "HE'S, IT'S, LET'S ^SHE'S, AREN'T, CAN'T, DIDN'T, DON'T &ISN'T, HASN'T, HADN'T, HAVEN'T, WEREN'T, WON'T. HE'D, I'D, SHE'D+ THEY'D- WE'D yes HE'S, IT'S, LET'S ^SHE'S, AREN'T, CAN'T, DIDN'T, DON'T &ISN'T, HASN'T, HADN'T, HAVEN'T, WEREN'T, WON'T. HE'D, I'D, SHE'D+ THEY'D- WE'D yes HE'S, IT'S, LET'S ^SHE'S, AREN'T, CAN'T, DIDN'T, DON'T &ISN'T, HASN'T, HADN'T, HAVEN'T WEREN'T, WON'T. HE'D, I'D, SHE')(*&&^%$#@!D THEY'!@#$%^&*()D- WE'D yes notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd"

caesar3CipherText = """Uzpqeodunmnxq abbdqeeuaz, ituot eqqyqp fa sqzqdmfq uz eayq gzrmyuxumd bmdf ar tqd oazeouagezqee, ruxxqp tqd itaxq nquzs iuft m hmsgq mzsguet. Uf ime xuwq m etmpai, xuwq m yuef bmeeuzs modaee tqd eagx'e egyyqd pmk. Uf ime efdmzsq mzp gzrmyuxumd; uf ime m yaap. Etq pup zaf euf ftqdq uzimdpxk gbndmupuzs tqd tgenmzp, xmyqzfuzs mf Rmfq, ituot tmp pudqofqp tqd raafefqbe fa ftq bmft ituot ftqk tmp fmwqz. Etq ime vgef tmhuzs m saap odk mxx fa tqdeqxr. Ftq yaecgufaqe ympq yqddk ahqd tqd, nufuzs tqd rudy, dagzp mdye mzp zubbuzs mf tqd nmdq uzefqbe.

Nmdnmdm tmp nqqz imufuzs mf ftq fmnxq rad fiqzfk yuzgfqe. uf tmp nqqz fiqzfk xazs mzp qjodgoumfuzs yuzgfqe. Pmhup tmp bdayueqp ftmf tq iagxp nq az fuyq fapmk. Tq zqhqd ime, ngf tq tmp bdayueqp ftue azq fuyq. Etq tmp ympq tuy dqbqmf ftq bdayueq ygxfubxq fuyqe ahqd ftq xmef iqqw gzfux etq'p nqxuqhqp tue bdayueq. Zai etq ime bmkuzs ftq bduoq.

Ftq oxaize tmp fmwqz ahqd. Mzp kqe, ftqk iqdq xufqdmxxk oxaize. Ahqd 100 tmp mbbqmdqp agf ar m eymxx HI ngs ftmf tmp nqqz pduhqz gb fa ftq nmzw. Zai ftqk iqdq mxx uzeupq mzp tmp fmwqz uf ahqd."""

caesar3PlainText = """Indescribable oppression, which seemed to generate in some unfamiliar part of her consciousness, filled her whole being with a vague anguish. It was like a shadow, like a mist passing across her soul's summer day. It was strange and unfamiliar; it was a mood. She did not sit there inwardly upbraiding her husband, lamenting at Fate, which had directed her footsteps to the path which they had taken. She was just having a good cry all to herself. The mosquitoes made merry over her, biting her firm, round arms and nipping at her bare insteps.

Barbara had been waiting at the table for twenty minutes. it had been twenty long and excruciating minutes. David had promised that he would be on time today. He never was, but he had promised this one time. She had made him repeat the promise multiple times over the last week until she'd believed his promise. Now she was paying the price.

The clowns had taken over. And yes, they were literally clowns. Over 100 had appeared out of a small VW bug that had been driven up to the bank. Now they were all inside and had taken it over."""

transposition1PlainText = """Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. Considered a "father of the computer", Babbage is credited with inventing the first mechanical computer that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbage's original plans. Built to tolerances achievable in the 19th century, the success of the finished engine indicated that Babbage's machine would have worked. Nine years later, the Science Museum completed the printer Babbage had designed for the difference engine."""

transposition1CipherText = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

transposition2PlainText = """Why do Americans have so many different types of towels? We have beach towels, hand towels, bath towels, dish towels, camping towels, quick-dry towels, and let’s not forget paper towels. Would 1 type of towel work for each of these things? Let’s take a beach towel. It can be used to dry your hands and body with no difficulty. A beach towel could be used to dry dishes. Just think how many dishes you could dry with one beach towel. I’ve used a beach towel with no adverse effects while camping. If you buy a thin beach towel it can dry quickly too. I’d probably cut up a beach towel to wipe down counters or for cleaning other items, but a full beach towel could be used too. Is having so many types of towels an extravagant luxury that Americans enjoy or is it necessary? I’d say it's overkill and we could cut down on the many types of towels that manufacturers deem necessary."""

transposition2CipherText = """WethaemdsoocLo nilrku stsy ibounao svm a ntu.h yanlpr wfhewtdc y  beh otclwng uh aeiyw oryspvdsiyne  teo uc hced wuokyet flaogrt etwe oee ,n olto’l blodooa nh wl leoudvfai i herd s t gttsofs.dotuiwucaoibeyc rtl i ncntcelsom bod o .w   rdyls lh  lul utshlbnttae'o s  aoewitwf ettIyy.dhmd baey tto e ego ncsum dAnfaesoeoWlhat    ea ted  io  orb  wlse latemy clhwlro ek ywAbsndoavcatouwr euseu sodnhee ths esguwsecoi e.yrwcea  .pi iasolxesv yamrdo ,tl,eloe autb   yehrmtc  pftce sunaec t iiwt os tdr anrheuJd l sphaIaeoehdm rjrrut ncfeobw,a  kt    asuiw.teiin’  rm  aayoyktymeaflwae np1 hbbhncessi o nn dbd sttnn y?i pacnesetlqda fieeaohdthtIweg d eoc,ooy t  ldenesr?lhsu ptona n    eh’ef.brpawl wo ehoIlosus e s ,ileyrgcuddttts vlf eyrcnebe.txar’ w fshnW,t cerp shssiooh oe eIa oh aul ytt danoaaate ockt ee? e fw iyn wcfcqb cnt Ipr i n fcrv  hwa-’t a tdafednoeuit huatoi cseaAssdo ty"""

substitution1CipherText = """Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"""

substitution2CipherText = """Oybb brkl vsu br usyev iru bvs tbyut, cpb Gsurqwey bvrpjvb wb fyt bvs ortb uwlwepkrpt ylgwes tvs'l sgsu useswgsl. Tpus, wb vyl cssq fskk-osyqwqj fvsq vs tywl wb, cpb tvs lwlq'b pqlsutbyql fvm yqmrqs frpkl fyqb br tpjjstb trosbvwqj bvyb frpkl kwbsuykkm hwkk mrp wi mrp yebpykkm oyqyjsl br yevwsgs wb. Bvsus't qr fym vs'l yjuss."""

substitution3CipherText = """Dwkgpj wy qcley le jkqi? Ewne qnd ewy vgydelki cgiilio ewckgow wld xlij. Wy akgpji'e byplyry qwne wnj zgde wnuuyiyj nij wy miyq ikbkjt ypdy qkgpj byplyry wlx nd qypp. Yryi lf wy jkagxyieyj qwne wnj wnuuyiyj bt qclelio le jkqi, wy delpp jlji'e byplyry nitkiy qkgpj delpp byplyry le. Dk ewy vgydelki cyxnliyj. Qnd le by qkcew le ek naegnppt qcley le jkqi?"""

substitution4CipherText = """Le qndi'e dguukdyj ek yij ewne qnt. Ewy upni wnj byyi xyelagpkgdpt ewkgowe kge nij ucnaelayj nonli nij nonli. Ewycy qnd kipt kiy ukddlbpy cydgpe kiay le wnj byyi lxupyxyieyj, bge nd ewyt dekkj ewycy ewy cydgpe qndi'e nitewlio apkdy ek qwne le dwkgpj wnry byyi. Ewyt npp bpnimpt pkkmyj ne ynaw qkijyclio wkq ewld akgpj wnry wnuuyiyj. Li ewylc xlijd, ewyt npp byoni ek bpnxy ewy kewyc xyxbycd kf ewy ockgu nd ek qwt ewyt wnj fnlpyj."""

substitution5CipherText = """Tvs ythsl bvs npstbwrq sgsq bvrpjv tvs lwlq'b usykkm fyqb br vsyu bvs yqtfsu. Wb fyt y qr-fwq twbpybwrq twqes tvs ykusylm hqsf. Wi vs brkl bvs bupbv, tvs'l jsb erqiwuoybwrq ri vsu frutb isyut. Wi vs kwsl, tvs'l hqrf bvyb vs fytq'b fvr tvs bvrpjvb vs fyt fvwev frpkl cs ykortb yt cyl. Msb tvs ythsl bvs npstbwrq yqmfym yql fywbsl iru vwt yqtfsu.

Trosbwost wb't bvs iwutb orosqb ri bvs lym bvyb eybevst mrp rii jpyul. Bvyb't fvyb Fsqlm fyt bvwqhwqj. Tvs rxsqsl vsu fwqlrf br tss iwus sqjwqst teussevwqj lrfq bvs tbussb. Fvwks bvwt fytq'b trosbvwqj eroxksbskm pqvsyul ri, wb yktr fytq'b qruoyk. Wb fyt y tpus twjq ri fvyb fyt jrwqj br vyxxsq bvyb lym. Tvs erpkl issk wb wq vsu crqst yql wb fytq'b bvs fym tvs fyqbsl bvs lym br csjwq.

Xybuweh lwlq'b fyqb br jr. Bvs iyeb bvyb tvs fyt wqtwtbwqj bvsm optb jr oyls vwo fyqb br jr sgsq kstt. Vs vyl qr lstwus br oyhs toykk bykh fwbv tbuyqjsut vs frpkl qsgsu yjywq tss dptb br cs xrkwbs. Cpb tvs wqtwtbsl bvyb Xybuweh jr, yql tvs frpkl trrq iwql rpb bvyb bvwt frpkl cs bvs cwjjstb owtbyhs tvs erpkl oyhs wq bvswu uskybwrqtvwx."""

substitution6CipherText = """L'x oklio ek wlcy uckfyddlkinp wypu ekxkcckq. L ani'e wnijpy ewld nitxkcy. Dwy fypp kryc ewy akffyy enbpy nij ikq ewycy ld bpkkj li wyc anewyeyc. Ewld ld xgaw xkcy ewni L yryc dloiyj gu ek jk.

Ewycy qnd n elxy li wld plfy qwyi wyc cgjyiydd qkgpj wnry dye wlx kryc ewy yjoy. Wy qkgpj wnry cnldyj wld rklay nij jyxnijyj ek duynm ek ewy xninoyc. Ewne qnd ik pkioyc ewy andy. Wy bncypt cynaeyj ne npp, pyeelio ewy cgjyiydd xype nqnt qlewkge dntlio n qkcj bnam ek wyc. Wy wnj byyi nckgij pkio yikgow ek mikq qwycy cgjyiydd anxy fckx nij wkq giwnuut ewy uycdki xgde by ek nae li ewne qnt. Npp wy akgpj jk qnd fyyp ulet nij by wnuut ewne wy jlji'e fyyp ewy qnt dwy jlj ek pndw kge plmy ewne.

Dwy qnd li n wgcct. Ike ewy denijncj wgcct qwyi tkg'cy li n cgdw ek oye dkxyupnay, bge n fcniela wgcct. Ewy etuy kf wgcct qwycy n fyq dyakijd akgpj xyni plfy kc jynew. Dwy cnayj jkqi ewy cknj loikclio duyyj plxled nij qynrlio byeqyyi ancd. Dwy qnd kipt n fyq xligeyd nqnt qwyi ecnffla anxy ek n jynj denijdelpp ki ewy cknj nwynj."""

substitution6PlainText = """I'm going to hire professional help tomorrow. I can't handle this anymore. She fell over the coffee table and now there is blood in her catheter. This is much more than I ever signed up to do.

There was a time in his life when her rudeness would have set him over the edge. He would have raised his voice and demanded to speak to the manager. That was no longer the case. He barely reacted at all, letting the rudeness melt away without saying a word back to her. He had been around long enough to know where rudeness came from and how unhappy the person must be to act in that way. All he could do was feel pity and be happy that he didn't feel the way she did to lash out like that.

She was in a hurry. Not the standard hurry when you're in a rush to get someplace, but a frantic hurry. The type of hurry where a few seconds could mean life or death. She raced down the road ignoring speed limits and weaving between cars. She was only a few minutes away when traffic came to a dead standstill on the road ahead."""

substitution7CipherText = """Ewy npncx qyie kff ne ysnaept 6:00 NX nd le wnj yryct xkcilio fkc ewy unde flry tyncd. Bncbncn byoni wyc xkcilio nij qnd cynjt ek yne bcynmfnde bt 7:00 NX. Ewy jnt nuuyncyj ek by nd ikcxnp nd nit kewyc, bge ewne qnd nbkge ek awnioy. Li fnae, le qnd oklio ek awnioy ne ysnaept 7:23 NX.

Ewycy qnd ikewlio ek lijlaney Iniat qnd oklio ek awnioy ewy qkcpj. Dwy pkkmyj plmy ni nrycnoy olcp oklio ek ni nrycnoy wlow dawkkp. Le qnd ewy fnae ewne yryctewlio nbkge wyc dyyxyj nrycnoy ewne qkgpj yij gu byakxlio wyc dguycukqyc.

Wy dakpjyj wlxdypf fkc bylio dk eyienelry. Wy miyq wy dwkgpji'e by dk angelkgd, bge ewycy qnd n dlsew dyidy eypplio wlx ewne ewliod qycyi'e ysnaept nd ewyt nuuyncyj. Le qnd ewne qylcj awlpp ewne ckppd gu tkgc iyam nij xnmyd ewy wnlc denij ki yij. Wy miyq ewne bylio dk eyienelry akgpj yij gu akdelio wlx ewy zkb, bge wy pynciyj ewne pldeyilio ek wld dlsew dyidy gdgnppt myue wlx fckx oyeelio liek n pke kf eckgbpy."""

substitution8CipherText = """Ewy qnry acndwyj nij wle ewy dnijandepy wynj-ki. Ewy dnijandepy byoni ek xype gijyc ewy qnryd fkcay nij nd ewy qnry cyayjyj, wnpf ewy dnijandepy qnd okiy. Ewy iyse qnry wle, ike vgley nd deckio, bge delpp xninoyj ek akryc ewy cyxnlid kf ewy dnijandepy nij enmy xkcy kf le nqnt. Ewy ewlcj qnry, n blo kiy, acndwyj kryc ewy dnijandepy akxupyeypt akryclio nij yiogpflio le. Qwyi le cyayjyj, ewycy qnd ik ecnay ewy dnijandepy yryc ysldeyj nij wkgcd kf wncj qkcm jldnuuyncyj fkcyryc.

Dleelio li ewy dgi, nqnt fckx yryctkiy qwk wnj jkiy wlx wncx li ewy unde, wy vglyept pldeyiyj ek ewkdy qwk cknxyj bt. Wy fype ne uynay li ewy xkxyie, wkulio le qkgpj pnde, bge mikqlio ewy cyuclyry qkgpj dkki akxy ek ni yij. Wy apkdyj wld ytyd, ewy dgi bynelio jkqi ki fnay nij wy dxlpyj. Wy dxlpyj fkc ewy flcde elxy li nd pkio nd wy akgpj cyxyxbyc.

"Le'd iyryc okkj ek olry ewyx jyenlpd," Znilay ekpj wyc dldeyc. "Npqntd by n pleepy rnogy nij myyu ewyx ogyddlio." Wyc dldeyc pldeyiyj lieyiept nij ikjjyj li nocyyxyie. Dwy jlji'e fgppt gijycdenij qwne wyc dldeyc qnd dntlio bge ewne jlji'e xneeyc. Dwy pkryj wyc dk xgaw ewne dwy qkgpj wnry nocyyj ek qwneyryc anxy kge kf wyc xkgew.

Wy qnd nfeyc ewy ecgew. Ne pynde, ewne'd qwne wy ekpj wlxdypf. Wy byplyryj le, bge nit cnelkinp uycdki ki ewy kgedljy akgpj dyy wy qnd ptlio ek wlxdypf. Le qnd nuuncyie wy qnd cynppt kipt nfeyc wld kqi ecgew ewne wy'j npcynjt jyaljyj nij qnd nfeyc ewld ecgew byangdy ewy fnaed jlji'e pliy gu qlew ewy ecgew wy qnieyj. Dk wy akieligyj ek eypp yryctkiy wy qnd nfeyc ewy ecgew kbplrlkgd ek ewy cynp ecgew dleelio clowe li fckie kf wlx.

Dwy iyryc plmyj apynilio ewy dlim. Le qnd bytkij wyc akxucywyidlki wkq le oke dk jlcet dk vglampt. Le dyyxyj ewne dwy qnd fkcayj ek apyni le yryct kewyc jnt. Yryi qwyi dwy qnd ysecn ancyfgp ek myyu ewliod apyni nij kcjycpt, le delpp yijyj gu pkkmlio plmy n xydd li n akgupy kf jntd. Qwne dwy jlji'e mikq qnd ewycy qnd n elit acynegcy plrlio li le ewne jlji'e plmy ewliod iyne."""

substitution8PlainText = """The wave crashed and hit the sandcastle head-on. The sandcastle began to melt under the waves force and as the wave receded, half the sandcastle was gone. The next wave hit, not quite as strong, but still managed to cover the remains of the sandcastle and take more of it away. The third wave, a big one, crashed over the sandcastle completely covering and engulfing it. When it receded, there was no trace the sandcastle ever existed and hours of hard work disappeared forever.

Sitting in the sun, away from everyone who had done him harm in the past, he quietly listened to those who roamed by. He felt at peace in the moment, hoping it would last, but knowing the reprieve would soon come to an end. He closed his eyes, the sun beating down on face and he smiled. He smiled for the first time in as long as he could remember.

"It's never good to give them details," Janice told her sister. "Always be a little vague and keep them guessing." Her sister listened intently and nodded in agreement. She didn't fully understand what her sister was saying but that didn't matter. She loved her so much that she would have agreed to whatever came out of her mouth.

He was after the truth. At least, that's what he told himself. He believed it, but any rational person on the outside could see he was lying to himself. It was apparent he was really only after his own truth that he'd already decided and was after this truth because the facts didn't line up with the truth he wanted. So he continued to tell everyone he was after the truth oblivious to the real truth sitting right in front of him.

She never liked cleaning the sink. It was beyond her comprehension how it got so dirty so quickly. It seemed that she was forced to clean it every other day. Even when she was extra careful to keep things clean and orderly, it still ended up looking like a mess in a couple of days. What she didn't know was there was a tiny creature living in it that didn't like things neat."""

substitution9CipherText = """Jnry qndi'e ysnaept dgcy wkq wy wnj yijyj gu li ewld ucyjlanxyie. Wy cni ewckgow npp ewy yryied ewne wnj pynj ek ewld agccyie dlegnelki nij le delpp jlji'e xnmy dyidy. Wy qnieyj ek duyij dkxy elxy ek ect nij xnmy dyidy kf le npp, bge wy wnj wlowyc uclkclelyd ne ewy xkxyie. Ewy flcde qnd wkq ek oye kge kf wld agccyie dlegnelki kf bylio inmyj li n ecyy qlew dikq fnpplio npp nckgij nij ik qnt fkc wlx ek oye jkqi.

Le cynppt jkydi'e xneeyc qwne dwy ewlimd nd le ldi'e wyc uckbpyx ek dkpry. Ewne'd qwne wy myue ectlio ek akirliay wlxdypf. Dwy qnd ectlio ek lidyce wyc kulilki qwycy le qndi'e qnieyj kc qypakxy. Wy npcynjt wnj n upni nij yryi ewkgow ewne upni jlji'e akccydukij qlew qwne dwy qnieyj wlx ek jk kc qwne dwkgpj by jkiy, le qndi'e wyc jyaldlki ek xnmy. Ewy vgydelki ikq byanxy qwyewyc wy qkgpj delam ek wld akirlaelkid nij ok ewckgow qlew wld upni mikqlio dwy qkgpji'e nuuckry.

Le wnj byyi n dlxupy cynplhnelki ewne wnj awnioyj Jybcn'd plfy uycduyaelry. Le qnd cynppt dk dlxupy ewne dwy qnd yxbnccnddyj ewne dwy wnj plryj ewy ucyrlkgd flry tyncd qlew ewy qnt dwy xyndgcyj wyc qkcew. Ikq ewne dwy dnq qwne dwy wnj byyi jklio, dwy akgpj dyy wkq dnj le qnd. Ewne xnjy wyc npp ewy xkcy cyplyryj dwy wnj xnjy ewy awnioy. Ewy igxbyc kf wynced wyc Lidenocnx ukded cyaylryj qndi'e nit pkioyc ewy lijlanelki kf wyc kqi dypf-qkcew.

Npewkgow Dakee dnlj le jlji'e xneeyc ek wlx, wy miyq jyyu lidljy ewne le jlj. Ewyt wnj byyi fclyijd nd pkio nd wy akgpj cyxyxbyc nij ike kiay wnj wy wnj ek uckeyde ewne dkxyewlio Zky nukpkolhyj fkc jklio jlji'e cynppt xneeyc. Dakee degam ek wld ply nij lidldeyj nonli nij nonli ewne yryctewlio qnd fliy nd Zky akieligyj ek nukpkolhy. Dakee npcynjt miyq ewne jyduley wld qkcjd naayuelio ewy nukpkolyd ewne ewylc fclyijdwlu qkgpj iyryc by ewy dnxy.

Ewycy qnd ik clio ki wld flioyc. Ewne qnd n okkj dloi npewkgow fnc fckx uckkf ewne wy qnd nrnlpnbpy. Delpp, le qnd xgaw byeeyc ewni lf wy wnj byyi qynclio n qyjjlio clio ki wld wnij. Dwy opniayj ne wld wnij n ble xkcy lieyiept ek dyy lf ewycy qycy nit eni pliyd qwycy n clio xnt wnry byyi, nij wy'd dlxupt enmyi le kff. Dwy akgpji'e jyeyae nit qwlaw qnd npdk n okkj dloi nij n cyplyf. Ewy iyse deyu qkgpj by ek oye naaydd ek wld qnppye ek dyy lf ewycy qycy nit fnxlpt uwkekd li le."""

substitution10CipherText = """Pkry ldi'e npqntd n cnt kf dgidwliy. Ewne'd qwne ewy kpjyc olcpd myue eypplio wyc qwyi dwy dnlj dwy wnj fkgij ewy uycfyae xni. Dwy wnj ewkgowe ewld qnd dlxupt bleeyc enpm ki ewylc unce dliay ewyt wnj byyi ginbpy ek flij ecgy pkry plmy wycd. Bge ikq dwy wnj ek fnay ewy fnae ewne ewyt xnt wnry byyi clowe. Pkry xnt ike npqntd by n cnt kf dgidwliy. Ewne ld gipydd ewyt qycy cyfycclio ek wkq ewy dgi ani bgci.

Wkq wnj dwy byyi dk qckio? Npp wyc lideliaed nij lieglelki akxupyeypt fnlpyj wyc fkc ewy flcde elxy li wyc plfy. Dwy wnj dk wynrlpt cyplyj ki bkew qwyi xnmlio jyaldlkid gu gielp ewld xkxyie nij dwy fype n dyldxla dwlfe enmy upnay li wyc dypf-akifljyiay. Lf dwy akgpj by dk akxupyeypt qckio nbkge dkxyewlio dk dlxupy nd ewld, wkq akgpj dwy xnmy jyaldlkid nbkge cynppt lxukcenie ewliod enmlio upnay li wyc plfy? Dwy qndi'e dgcy qwne dwy dwkgpj jk iyse.

Ewy wynjuwkiyd qycy ki. Ewyt wnj byyi gelplhyj ki ugcukdy. Dwy akgpj wync wyc xkx typplio li ewy bnamockgij, bge akgpji'e xnmy kge ysnaept qwne ewy typplio qnd nbkge. Ewne qnd ysnaept qwt dwy wnj uge ewyx ki. Dwy miyq wyc xkx qkgpj yieyc wyc ckkx ne nit xligey, nij dwy akgpj ucyeyij ewne dwy wnji'e wyncj nit kf ewy ucyrlkgd typplio.

Ewycy qnd dkxyewlio duyalnp nbkge ewld pleepy acynegcy. Jkiin akgpji'e vgley uliuklie qwne le qnd, bge dwy miyq qlew npp wyc wynce ewne le qnd ecgy. Le qndi'e n xneeyc kf lf dwy qnd oklio ek ect nij dnry le, bge n xneeyc kf wkq dwy qnd oklio ek dnry le. Dwy qyie bnam ek ewy anc ek oye n bpnimye nij qwyi dwy cyegciyj ewy acynegcy qnd okiy.

Jnry qneawyj nd ewy fkcyde bgciyj gu ki ewy wlpp, kipt n fyq xlpyd fckx wyc wkgdy. Ewy anc wnj byyi wndelpt unamyj nij Xncen qnd lidljy ectlio ek ckgij gu ewy pnde kf ewy uyed. Jnry qyie ewckgow wld xyienp plde kf ewy xkde lxukcenie unuycd nij jkagxyied ewne ewyt akgpji'e pynry bywlij. Wy dakpjyj wlxdypf fkc ike wnrlio ucyuncyj ewydy byeeyc li njrniay nij wkuyj ewne wy wnj cyxyxbycyj yryctewlio ewne qnd iyyjyj. Wy akieligyj ek qnle fkc Xncen ek nuuync qlew ewy uyed, bge dwy delpp qnd ikqwycy ek by dyyi."""

substitution10PlainText = """Love isn't always a ray of sunshine. That's what the older girls kept telling her when she said she had found the perfect man. She had thought this was simply bitter talk on their part since they had been unable to find true love like hers. But now she had to face the fact that they may have been right. Love may not always be a ray of sunshine. That is unless they were referring to how the sun can burn.

How had she been so wrong? All her instincts and intuition completely failed her for the first time in her life. She had so heavily relied on both when making decisions up until this moment and she felt a seismic shift take place in her self-confidence. If she could be so completely wrong about something so simple as this, how could she make decisions about really important things taking place in her life? She wasn't sure what she should do next.

The headphones were on. They had been utilized on purpose. She could hear her mom yelling in the background, but couldn't make out exactly what the yelling was about. That was exactly why she had put them on. She knew her mom would enter her room at any minute, and she could pretend that she hadn't heard any of the previous yelling.

There was something special about this little creature. Donna couldn't quite pinpoint what it was, but she knew with all her heart that it was true. It wasn't a matter of if she was going to try and save it, but a matter of how she was going to save it. She went back to the car to get a blanket and when she returned the creature was gone.

Dave watched as the forest burned up on the hill, only a few miles from her house. The car had been hastily packed and Marta was inside trying to round up the last of the pets. Dave went through his mental list of the most important papers and documents that they couldn't leave behind. He scolded himself for not having prepared these better in advance and hoped that he had remembered everything that was needed. He continued to wait for Marta to appear with the pets, but she still was nowhere to be seen."""


def testcaesar1():
    url = baseURL + "unknown"
    param = {"cipherText": caesar1CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "caesar"
    assert payload["result"]["plainText"] == caesar1PlainText

def testcaesar2():
    url = baseURL + "unknown"
    param = {"cipherText": caesar2CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "caesar"
    assert payload["result"]["plainText"] == caesar2PlainText

def testcaesar3():
    url = baseURL + "unknown"
    param = {"cipherText": caesar3CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "caesar"
    assert payload["result"]["plainText"] == caesar3PlainText

def testcaesar4():
    url = baseURL + "caesar"
    param = {"cipherText": caesar3CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["plainText"] == caesar3PlainText

def testTransposition1():
    url = baseURL + "unknown"
    param = {"cipherText": transposition1CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "transposition"
    assert payload["result"]["plainText"] == transposition1PlainText

def testTransposition2():
    url = baseURL + "unknown"
    param = {"cipherText": transposition2CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "transposition"
    assert payload["result"]["plainText"] == transposition2PlainText

def testTransposition3():
    url = baseURL + "transposition"
    param = {"cipherText": transposition2CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["plainText"] == transposition2PlainText

def testSubstitutionPartial1():
    url = baseURL + "unknown"
    param = {"cipherText": substitution1CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial2():
    url = baseURL + "unknown"
    param = {"cipherText": substitution2CipherText}
    
    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial3():
    url = baseURL + "unknown"
    param = {"cipherText": substitution3CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial4():
    url = baseURL + "unknown"
    param = {"cipherText": substitution4CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial5():
    url = baseURL + "unknown"
    param = {"cipherText": substitution5CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial6():
    url = baseURL + "unknown"
    param = {"cipherText": substitution6CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial7():
    url = baseURL + "unknown"
    param = {"cipherText": substitution7CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial8():
    url = baseURL + "unknown"
    param = {"cipherText": substitution8CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial9():
    url = baseURL + "unknown"
    param = {"cipherText": substitution9CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionPartial10():
    url = baseURL + "unknown"
    param = {"cipherText": substitution10CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    assert payload["cipherType"] == "substitution"

def testSubstitutionFull1():
    url = baseURL + "unknown"
    param = {"cipherText": substitution6CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    intersectedMapping = payload["result"]["intersectedMapping"]

    url2 = baseURL + 'substitution?mode=full'
    params = {"cipherText": substitution6CipherText, "intersectedMapping": intersectedMapping}

    r = requests.put(url2, json = params)
    payload = r.json()

    assert payload["plainText"] == substitution6PlainText

def testSubstitutionFull2():
    url = baseURL + "unknown"
    param = {"cipherText": substitution8CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    intersectedMapping = payload["result"]["intersectedMapping"]

    url2 = baseURL + 'substitution?mode=full'
    params = {"cipherText": substitution8CipherText, "intersectedMapping": intersectedMapping}

    r = requests.put(url2, json = params)
    payload = r.json()

    assert payload["plainText"] == substitution8PlainText

def testSubstitutionFull3():
    url = baseURL + "unknown"
    param = {"cipherText": substitution10CipherText}

    r = requests.put(url, json = param)
    payload = r.json()
    intersectedMapping = payload["result"]["intersectedMapping"]

    url2 = baseURL + 'substitution?mode=full'
    params = {"cipherText": substitution10CipherText, "intersectedMapping": intersectedMapping}

    r = requests.put(url2, json = params)
    payload = r.json()

    assert payload["plainText"] == substitution10PlainText