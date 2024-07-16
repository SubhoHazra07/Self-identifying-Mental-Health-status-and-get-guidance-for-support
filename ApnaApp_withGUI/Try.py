from bardapi import Bard
import os
import time
os.environ['_BARD_API_KEY_']="dQg82u18Q_5dcIRuddrdDUfcGTv7j2o_kNd2hMfXvm1H0ROPkTRIRRqpCCvz6wmG-cCmAw"
input_text="Why is the sky blue?"
print(Bard().get_answer(input_text)['content'])