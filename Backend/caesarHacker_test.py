import pytest
from caesarHacker import caesarHacker

invalid1CipherText = "evcniefv erfvrfv edcdc dwc tgtbyb hello hi I am cool yes almost"

invalid2CipherText = "RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D, GOBOX'D, GYX'D. RO'N, S'N, CRO'N+ DROI'N- GO'N ioc RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D, GOBOX'D, GYX'D. RO'N, S'N, CRO'N+ DROI'N- GO'N ioc RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D GOBOX'D, GYX'D. RO'N, S'N, CRO')(*&&^%$#@!N DROI'!@#$%^&*()N- GO'N ioc xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn"

valid1PlainText = "It was a concerning development that he couldn't get out of his mind. He'd had many friends throughout his early years and had fond memories of playing with them, but he couldn't understand how it had all stopped. There was some point as he grew up that he played with each of his friends for the very last time, and he had no idea that it would be the last."

valid1CipherText = "Ny bfx f htshjwsnsl ijajqturjsy ymfy mj htzqis'y ljy tzy tk mnx rnsi. Mj'i mfi rfsd kwnjsix ymwtzlmtzy mnx jfwqd djfwx fsi mfi ktsi rjrtwnjx tk uqfdnsl bnym ymjr, gzy mj htzqis'y zsijwxyfsi mtb ny mfi fqq xytuuji. Ymjwj bfx xtrj utnsy fx mj lwjb zu ymfy mj uqfdji bnym jfhm tk mnx kwnjsix ktw ymj ajwd qfxy ynrj, fsi mj mfi st nijf ymfy ny btzqi gj ymj qfxy."

valid2PlainText = """There are only three ways to make this work. The first is to let me take care of everything. The second is for you to take care of everything. The third is to split everything 50 / 50. I think the last option is the most preferable, but I'm certain it'll also mean the end of our marriage.

Although Scott said it didn't matter to him, he knew deep inside that it did. They had been friends as long as he could remember and not once had he had to protest that something Joe apologized for doing didn't really matter. Scott stuck to his lie and insisted again and again that everything was fine as Joe continued to apologize. Scott already knew that despite his words accepting the apologies that their friendship would never be the same."""

valid2CipherText = """Maxkx tkx hger makxx ptrl mh ftdx mabl phkd. Max ybklm bl mh exm fx mtdx vtkx hy xoxkrmabgz. Max lxvhgw bl yhk rhn mh mtdx vtkx hy xoxkrmabgz. Max mabkw bl mh liebm xoxkrmabgz 50 / 50. B mabgd max etlm himbhg bl max fhlm ikxyxktuex, unm B'f vxkmtbg bm'ee telh fxtg max xgw hy hnk ftkkbtzx.

Temahnza Lvhmm ltbw bm wbwg'm ftmmxk mh abf, ax dgxp wxxi bglbwx matm bm wbw. Maxr atw uxxg ykbxgwl tl ehgz tl ax vhnew kxfxfuxk tgw ghm hgvx atw ax atw mh ikhmxlm matm lhfxmabgz Chx tihehzbsxw yhk whbgz wbwg'm kxteer ftmmxk. Lvhmm lmnvd mh abl ebx tgw bglblmxw tztbg tgw tztbg matm xoxkrmabgz ptl ybgx tl Chx vhgmbgnxw mh tihehzbsx. Lvhmm tekxtwr dgxp matm wxlibmx abl phkwl tvvximbgz max tihehzbxl matm maxbk ykbxgwlabi phnew gxoxk ux max ltfx."""

valid3PlainText = "HE'S, IT'S, LET'S ^SHE'S, AREN'T, CAN'T, DIDN'T, DON'T &ISN'T, HASN'T, HADN'T, HAVEN'T, WEREN'T, WON'T. HE'D, I'D, SHE'D+ THEY'D- WE'D yes HE'S, IT'S, LET'S ^SHE'S, AREN'T, CAN'T, DIDN'T, DON'T &ISN'T, HASN'T, HADN'T, HAVEN'T, WEREN'T, WON'T. HE'D, I'D, SHE'D+ THEY'D- WE'D yes HE'S, IT'S, LET'S ^SHE'S, AREN'T, CAN'T, DIDN'T, DON'T &ISN'T, HASN'T, HADN'T, HAVEN'T WEREN'T, WON'T. HE'D, I'D, SHE')(*&&^%$#@!D THEY'!@#$%^&*()D- WE'D yes notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd notAWoRd"

valid3CipherText = "RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D, GOBOX'D, GYX'D. RO'N, S'N, CRO'N+ DROI'N- GO'N ioc RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D, GOBOX'D, GYX'D. RO'N, S'N, CRO'N+ DROI'N- GO'N ioc RO'C, SD'C, VOD'C ^CRO'C, KBOX'D, MKX'D, NSNX'D, NYX'D &SCX'D, RKCX'D, RKNX'D, RKFOX'D GOBOX'D, GYX'D. RO'N, S'N, CRO')(*&&^%$#@!N DROI'!@#$%^&*()N- GO'N ioc xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn xydKGyBn"

def testInvalid1():
    with pytest.raises(Exception):
        caesarHacker(invalid1CipherText)

def testInvalid2():
    with pytest.raises(Exception):
        caesarHacker(invalid2CipherText)

def testValid1():
    data = caesarHacker(valid1CipherText)
    assert data["plainText"] == valid1PlainText
    assert data["key"] == 5

def testValid2():
    data = caesarHacker(valid2CipherText)
    assert data["plainText"] == valid2PlainText
    assert data["key"] == 19

def testValid3():
    data = caesarHacker(valid3CipherText)
    assert data["plainText"] == valid3PlainText
    assert data["key"] == 10