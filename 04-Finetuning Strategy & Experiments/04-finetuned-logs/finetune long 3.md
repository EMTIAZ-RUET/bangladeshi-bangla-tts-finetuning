# Fine-tuning Training Log

**Source File:** `finetune long 3.odt`

**Converted:** 2025-09-23 21:34:55

## Training Output

```
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
for filename in filenames:
print(os.path.join(dirname, filename))
# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
/kaggle/input/100-th-epoch/__results__.html
/kaggle/input/100-th-epoch/__notebook__.ipynb
/kaggle/input/100-th-epoch/__output__.json
/kaggle/input/100-th-epoch/custom.css
/kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/config.json
/kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/checkpoint_877000.pth
/kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/train_tts.py
/kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/best_model.pth
/kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/best_model_862511.pth
/kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/events.out.tfevents.1746960153.e5db9382c602.135.0
/kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/trainer_0_log.txt
/kaggle/input/ttsbng/transformers/default/1/config.json
/kaggle/input/datahrbn/MyTTSDataset/cleanEndline.py
/kaggle/input/datahrbn/MyTTSDataset/outlier1.txt
/kaggle/input/datahrbn/MyTTSDataset/metadata.txt
/kaggle/input/datahrbn/MyTTSDataset/new line count.py
/kaggle/input/datahrbn/MyTTSDataset/test.py
/kaggle/input/datahrbn/MyTTSDataset/train_tts.py
/kaggle/input/datahrbn/MyTTSDataset/outlier.txt
/kaggle/input/datahrbn/MyTTSDataset/testOutlier.py
/kaggle/input/datahrbn/MyTTSDataset/data-deleteScript.py
/kaggle/input/datahrbn/MyTTSDataset/count audio and row.py
/kaggle/input/datahrbn/MyTTSDataset/checkSampleRate.py
/kaggle/input/datahrbn/MyTTSDataset/changeRate.py
/kaggle/input/datahrbn/MyTTSDataset/.idea/MyTTSDataset.iml
/kaggle/input/datahrbn/MyTTSDataset/.idea/git_toolbox_blame.xml
/kaggle/input/datahrbn/MyTTSDataset/.idea/.gitignore
/kaggle/input/datahrbn/MyTTSDataset/.idea/modules.xml
/kaggle/input/datahrbn/MyTTSDataset/.idea/workspace.xml
/kaggle/input/datahrbn/MyTTSDataset/.idea/misc.xml
/kaggle/input/datahrbn/MyTTSDataset/.idea/inspectionProfiles/profiles_settings.xml
/kaggle/input/datahrbn/MyTTSDataset/.idea/inspectionProfiles/Project_Default.xml
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4556.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio102.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2082.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio519.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4353.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2443.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio41.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1874.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4136.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3488.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1111.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2614.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio387.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1664.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1839.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4867.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4428.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1725.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1849.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2105.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3381.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2548.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2147.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1539.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio138.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3245.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4120.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1086.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2275.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3846.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4905.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4053.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2550.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4976.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1458.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4037.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4116.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1498.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2025.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3267.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio521.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3126.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3793.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2540.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2214.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2222.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1512.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4019.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2253.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2186.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2043.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4240.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2117.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio773.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio126.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3837.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3364.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2925.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1854.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3262.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4791.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio480.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3152.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1759.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1914.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3645.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2951.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4279.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3766.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1324.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2420.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1597.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2867.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2973.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4320.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1393.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1996.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2900.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1467.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2895.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4079.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4488.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1707.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4936.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2142.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio719.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5072.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio931.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1257.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4579.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2749.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4751.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio427.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3268.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3927.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio301.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5074.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio753.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2201.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1819.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5103.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4492.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5057.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1287.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3457.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3459.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3288.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2321.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3702.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1178.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio907.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1144.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2577.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2446.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1319.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2569.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2986.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2929.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3127.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1179.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio882.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio214.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1020.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1861.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4717.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio302.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio112.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio785.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1767.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4550.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2113.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1734.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3054.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1669.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio319.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3778.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4260.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2432.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4451.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1558.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1623.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio316.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3756.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3077.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5059.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3356.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2971.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio778.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2708.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio966.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2522.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio523.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1055.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio191.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5139.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio860.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio543.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3631.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2725.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1300.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4210.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4102.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1071.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2897.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5022.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio972.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4013.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5079.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2409.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2438.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio625.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio296.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2996.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4285.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4962.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1966.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1981.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3596.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1199.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2717.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1145.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio489.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3899.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4330.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio968.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1449.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4801.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3772.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3903.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5118.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2870.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1797.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3100.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio265.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4973.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio786.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2458.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio258.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio72.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1351.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4300.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4999.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1326.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1641.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2338.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4177.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio701.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1674.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4549.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1476.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4650.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2737.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1321.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio357.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio528.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2746.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2916.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5154.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1706.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio493.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio669.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3370.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2751.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4081.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio673.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4810.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1980.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4354.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1366.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3564.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio497.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4483.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio461.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2072.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4305.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio271.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3271.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2452.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4099.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio604.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1369.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1763.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1017.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio29.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3904.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4121.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4348.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1229.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4998.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2296.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio852.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2283.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2182.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio216.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1235.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3618.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4032.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2919.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio432.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2959.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4958.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4571.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4838.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1690.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio535.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5041.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1632.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4059.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4642.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio854.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1394.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio424.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4075.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4589.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1504.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3605.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1555.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3277.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1036.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio188.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2221.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1207.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1945.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio794.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3345.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio929.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4539.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4362.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4204.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1451.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3076.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2660.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1023.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4195.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio200.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3494.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio462.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2059.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2416.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2849.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1425.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2924.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4096.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1078.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2574.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1801.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio799.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio554.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3887.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1899.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio938.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3043.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3719.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1318.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1968.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4914.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2774.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2635.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1769.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3358.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4145.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4510.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4473.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio440.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4500.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3908.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2908.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3585.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3014.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio425.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4295.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4068.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5112.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3955.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio532.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2516.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5151.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1937.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4689.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2499.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2603.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3857.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio571.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4766.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1601.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4444.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2004.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio821.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio633.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3528.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio398.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5157.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2553.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3909.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2207.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2799.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4796.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio800.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2688.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3823.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3619.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2260.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4647.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4641.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1853.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1472.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3934.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3765.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2373.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3513.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4363.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3260.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2993.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio84.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3523.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1771.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1359.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4727.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1442.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3830.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2766.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1715.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio345.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1733.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4480.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1731.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4364.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2955.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1909.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2671.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3791.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4275.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2316.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2065.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio144.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1863.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2381.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio749.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3128.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2869.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4978.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3739.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1049.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4907.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4685.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1275.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio291.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1778.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2303.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3526.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4277.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio499.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2640.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio452.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1895.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3684.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1317.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4681.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3470.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio913.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3265.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2489.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio516.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2238.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3461.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3171.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2759.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5092.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio999.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3735.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2861.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio298.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1418.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4518.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1543.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3157.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio390.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4063.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5141.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1183.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3774.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio174.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1921.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2949.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2202.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio586.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio638.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2465.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2918.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4414.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2699.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1206.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2187.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2380.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2265.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3549.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1606.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1875.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3219.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3576.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4548.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4995.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2360.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1783.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio463.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1524.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio542.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3009.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1217.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2826.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2183.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2309.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3041.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1932.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2037.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio751.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2987.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio909.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3058.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio694.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3622.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2302.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4718.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2039.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2827.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4993.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1397.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1489.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2675.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio202.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1939.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2692.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio469.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1398.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio715.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1835.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3707.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1693.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2570.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3556.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio109.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1557.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1784.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio992.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1171.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1177.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio157.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4773.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio136.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1011.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4762.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio575.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4425.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio53.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio117.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2989.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4199.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4090.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3562.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio36.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2264.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3944.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4155.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio414.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1857.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3481.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1756.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1028.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1505.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3223.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2530.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1481.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio865.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2354.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio732.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3489.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5105.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio131.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4687.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4286.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4494.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4347.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3923.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3988.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio878.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1753.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1704.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2340.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5104.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4074.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3878.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2419.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1758.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3207.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4203.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio890.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3091.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1344.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio624.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1320.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio618.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4506.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2471.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio801.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio649.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3931.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2942.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1587.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio436.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1747.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3066.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4906.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3869.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3581.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4439.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio197.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4318.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4950.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio121.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4398.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3640.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3985.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3057.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2511.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1889.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5132.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4478.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3965.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2091.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1132.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2638.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3008.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3087.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4159.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio137.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio784.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4018.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3840.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio198.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2377.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4761.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2317.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3996.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1535.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio956.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3165.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4536.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2422.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2941.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2383.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3093.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1488.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1794.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2079.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2228.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3449.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio619.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3125.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1154.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio64.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2051.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio965.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio510.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4036.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2966.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4269.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1088.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2274.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1085.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4513.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4445.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3038.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio977.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3336.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1322.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3833.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1447.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3571.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2825.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio163.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3486.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3656.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2030.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1721.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4045.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2310.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5071.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4249.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2466.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio817.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1789.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2747.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3302.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio904.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3036.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio211.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1727.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2961.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1529.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2103.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio501.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3520.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3777.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio207.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4108.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3563.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio91.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3254.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio151.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3154.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3557.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4541.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4241.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3997.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4412.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2448.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5128.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5108.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio812.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3296.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2862.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3730.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5013.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio584.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio870.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio165.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1862.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1331.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio249.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2035.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio51.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4253.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4338.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1908.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3147.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3145.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3693.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4342.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2549.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3150.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5028.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4301.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio321.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1865.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4595.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4617.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1903.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3462.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4707.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1468.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3881.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3301.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio648.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1279.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3065.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3897.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1010.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1387.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio374.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4910.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio634.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3538.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2588.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2695.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1172.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3971.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1591.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1503.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3276.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio86.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1663.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4213.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5009.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1027.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1074.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2526.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2161.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4607.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4459.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2743.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3323.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4519.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5122.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1544.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1296.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2767.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3332.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2979.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3440.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3886.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4521.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio372.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3921.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1261.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3397.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio368.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1918.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3580.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4759.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1060.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio916.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1450.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2029.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio346.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2239.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4965.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2502.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1112.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4741.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1732.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio654.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4424.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio215.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio471.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5042.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4484.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1029.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3326.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3511.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3383.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4963.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio514.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4039.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4919.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio702.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3591.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4294.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4865.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4884.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1444.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio552.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5149.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio585.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2650.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2196.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2575.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3709.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio184.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4799.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1630.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1080.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2429.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio438.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3476.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2665.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4917.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1483.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4551.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1834.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio114.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4092.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4833.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2770.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3551.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4208.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4967.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4230.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2953.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2889.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2944.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2255.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio846.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio50.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3685.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio598.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1099.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2341.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1283.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3388.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio337.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3050.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5081.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio873.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1070.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4234.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3522.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5143.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio495.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3424.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4226.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio442.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio699.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1598.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3607.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2807.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio348.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3799.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio601.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2504.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2402.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4908.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4118.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1402.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1661.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio458.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5053.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio569.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3769.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1388.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio334.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2612.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2371.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2192.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1103.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1195.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1353.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3600.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4977.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio156.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4150.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4831.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3084.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2344.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4739.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio312.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3022.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio979.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio793.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3802.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4131.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio989.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2732.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4273.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3382.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3315.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4955.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3238.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2762.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2832.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1428.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4351.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1936.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1791.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5145.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3493.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2106.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4094.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4583.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio24.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio911.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1607.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3990.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5107.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2318.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2023.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3137.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1069.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio534.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3317.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3441.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2601.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3828.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio167.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio790.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3873.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio68.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio647.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4626.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2674.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3933.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio805.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3510.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4380.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1001.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2994.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1204.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2011.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5069.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio288.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4256.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio10.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1678.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3633.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4502.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3419.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4129.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio611.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2210.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1703.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3182.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1250.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3642.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2144.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2628.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1421.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4775.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4083.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio683.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4337.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4276.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio747.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio146.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4012.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4157.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio710.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4057.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3875.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4543.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4168.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2707.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4776.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4538.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4212.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio940.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4225.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4994.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2276.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3129.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2453.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2672.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1173.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1890.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2385.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1951.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4798.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio905.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1816.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2838.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2615.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4830.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1152.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4866.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio513.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4911.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio964.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1109.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1533.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5114.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio915.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2401.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio290.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio836.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4902.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1232.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4166.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2063.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2206.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1800.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3151.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio553.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio155.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3442.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3826.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio674.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1395.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2567.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1870.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3458.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2805.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1377.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3770.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2254.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4757.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2000.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3311.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3098.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio874.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3824.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1176.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3337.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2375.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1382.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio78.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1315.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio170.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1571.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1037.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3072.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio441.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1523.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3123.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio317.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3939.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3754.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio474.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4943.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2400.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1284.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2410.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4033.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1415.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio745.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4052.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4475.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4209.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1066.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4242.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3184.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1869.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2673.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3762.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio226.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1717.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2829.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3786.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3010.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1308.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2558.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4307.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3028.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3870.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3120.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5037.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio129.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio590.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3757.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1698.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio96.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4635.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2788.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4612.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5062.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1978.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4291.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2337.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1222.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio406.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3221.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio472.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1552.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1105.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2457.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3981.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1219.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2131.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2964.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4058.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4632.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3532.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2133.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4883.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1894.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4314.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1034.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2594.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1330.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4841.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2683.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio161.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1337.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2545.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1490.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1383.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3232.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3861.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2427.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2784.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio235.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio324.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2382.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4197.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1252.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4238.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1531.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1952.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1522.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4682.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4691.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1416.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1239.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2823.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3465.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1548.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4797.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio937.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4219.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio600.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1864.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio502.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1042.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1748.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3901.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3380.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4028.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1550.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4673.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4429.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio42.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1625.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2062.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2498.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio718.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3970.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1576.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4453.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2997.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4025.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4742.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2369.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio707.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3609.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4690.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio338.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio221.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2208.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1866.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3635.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2298.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1995.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4771.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio953.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5046.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio213.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2365.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4636.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3259.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4132.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2623.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1738.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4114.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2943.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4487.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4694.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2494.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio717.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3051.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1282.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1295.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4468.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3759.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3699.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4605.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4781.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3190.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1486.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4486.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3210.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1025.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4649.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4476.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4584.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4639.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2733.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2138.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1156.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4597.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1743.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1051.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5017.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2844.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4469.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3063.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4477.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio595.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio386.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4918.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4281.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4457.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2620.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3094.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4447.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1654.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4321.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1694.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3159.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1637.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1525.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1227.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio816.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2667.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3922.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1762.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2078.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3760.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3479.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3946.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4638.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio952.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2833.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4561.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2423.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio343.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3961.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5093.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3661.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4173.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3338.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5005.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4923.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio980.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio971.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3994.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3011.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3859.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1628.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4692.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3197.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5078.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3583.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1897.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3073.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio607.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3711.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5073.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2176.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1719.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3648.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4467.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2356.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio752.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio385.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio77.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2782.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1313.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2450.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3643.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3972.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1076.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3954.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1911.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio443.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio984.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio247.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5120.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2483.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2258.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio344.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3789.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2357.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1501.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4047.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4870.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1456.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio949.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2081.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio688.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3013.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3531.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3281.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4278.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2495.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio872.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2605.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3257.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio588.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1150.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4714.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4576.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1702.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2342.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1711.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio411.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1613.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio43.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2227.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio99.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5056.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4065.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio490.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1087.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio38.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1612.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3753.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2822.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5110.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3905.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3357.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3825.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2729.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5015.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1844.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5124.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio46.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio177.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4010.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2662.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2528.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio189.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2647.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2345.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5019.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4382.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4339.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3877.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1002.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio730.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2960.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1437.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4341.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio350.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio253.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5052.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio130.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4960.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1655.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1213.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4982.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio246.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4393.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2590.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio695.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1999.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2903.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio650.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1741.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1739.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4482.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2405.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1075.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4049.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3153.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1198.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1949.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1569.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1609.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2565.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3327.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5047.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio243.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1143.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4578.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4243.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3700.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1310.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio565.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4643.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1991.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio788.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio616.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4499.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio545.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2034.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4034.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1638.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4035.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4449.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2722.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1976.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio560.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2156.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3264.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5004.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3342.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2841.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4106.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5096.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1578.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1751.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3681.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2602.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio264.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2428.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4184.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio686.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1485.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4360.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4825.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1404.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2533.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4328.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3503.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio31.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2578.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1201.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3005.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1536.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5100.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4050.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio379.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1072.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1272.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4368.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1059.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1407.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2199.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3515.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio82.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio95.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3664.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4422.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2015.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3695.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio110.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4913.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio169.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2014.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4786.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1821.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio993.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4851.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3396.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3341.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4481.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3404.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2786.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4135.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio557.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1367.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio422.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1965.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio693.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4372.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4889.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4613.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3604.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1737.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio644.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1514.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3124.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4557.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1808.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3114.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4202.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4861.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4387.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2334.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio178.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4847.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio444.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2408.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1562.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio273.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio378.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1944.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio835.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2753.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2295.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio455.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio418.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1031.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4263.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2135.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4835.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2315.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3229.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio212.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3414.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4564.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4878.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2584.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3130.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2046.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2372.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio397.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1465.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2359.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2049.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5026.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3775.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio991.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4296.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2194.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4624.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2656.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2907.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1024.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1362.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4947.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3634.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2765.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3439.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio367.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3803.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4161.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1491.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2118.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1881.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1676.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3429.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1538.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4756.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4466.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3085.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio815.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2726.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4292.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio274.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1268.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio866.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4652.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2555.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio371.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1293.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4789.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5134.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4003.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3724.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5021.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3455.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1163.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio429.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio581.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio141.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3473.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4931.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4699.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1290.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio340.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3534.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio359.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3082.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio303.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1594.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1622.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5129.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2397.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2682.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4163.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4512.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3222.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1340.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio566.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3387.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4596.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4400.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1376.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio410.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2198.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3960.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1255.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3978.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4175.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2904.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2543.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3989.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5001.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1735.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1251.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3195.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5126.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4949.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1912.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2559.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3813.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1209.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1054.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1455.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio118.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio930.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1457.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1648.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3964.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4534.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4407.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio487.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2828.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3902.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4144.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4432.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3800.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4969.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2403.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2606.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio399.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4656.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3541.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2437.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3086.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2698.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3393.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2624.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio829.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2017.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4559.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4434.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4303.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2010.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1380.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2777.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2804.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3438.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2873.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio858.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio94.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1660.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1016.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1433.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1950.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1065.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1631.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3047.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3835.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3848.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1148.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4675.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3815.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3148.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3433.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4971.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2007.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1328.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3269.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3261.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2881.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1681.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2845.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio66.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4862.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1409.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2114.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio549.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio921.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1780.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4811.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio737.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2934.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4117.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio551.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1347.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3275.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4706.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3046.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2780.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4820.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4970.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3000.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2496.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2284.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2611.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2247.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2024.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4560.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2205.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio653.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2235.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4545.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio61.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4244.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4345.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1000.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2546.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5095.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1967.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4001.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2179.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4569.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1220.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3888.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio974.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3425.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4051.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4258.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1958.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio622.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4957.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1169.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2045.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio986.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4719.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4553.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2980.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3537.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4909.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio615.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio643.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2480.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio123.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio579.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio627.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3392.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4869.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2639.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio325.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3924.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2120.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4415.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3776.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio309.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4817.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4959.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1429.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio840.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1159.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4672.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3138.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4986.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2992.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4824.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio315.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2267.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1892.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2441.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3548.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio37.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1202.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1820.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1855.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5016.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4602.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3412.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4095.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio830.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4319.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio962.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio134.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio561.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4900.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4021.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2597.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4493.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2406.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2166.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1872.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio318.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3218.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2016.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4956.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1766.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3716.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2779.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3967.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4416.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2096.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio285.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2806.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3175.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4600.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3614.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio206.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2972.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1873.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1904.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio958.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3836.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2311.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1773.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1584.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2909.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5085.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3177.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1477.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio990.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3976.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio423.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1084.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2219.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4629.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1940.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4828.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1691.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1979.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1837.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2003.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2376.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3686.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3660.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2361.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2389.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5131.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3501.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1208.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4442.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio408.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2262.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3346.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2076.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4712.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2445.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5029.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio998.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3303.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3135.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4187.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2808.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1830.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio464.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio454.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4229.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2415.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3920.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4890.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2155.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2243.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1003.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4581.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1129.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4040.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3482.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4331.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1018.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio322.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4192.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3250.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3561.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4298.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3559.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2353.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4728.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4220.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3820.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1167.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4996.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio677.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3865.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2137.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1329.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3394.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1537.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio881.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3305.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4809.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2374.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio311.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio506.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3959.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio845.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3914.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1392.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3827.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3366.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3720.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2697.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4198.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4078.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1240.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4054.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2518.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio97.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2476.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio736.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4582.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3172.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio525.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3321.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio484.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4317.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1101.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2170.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4340.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1266.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1647.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4151.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3974.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2507.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio623.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4885.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4147.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4640.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2589.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4038.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4516.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3074.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2050.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1701.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1972.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2308.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3435.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3544.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2469.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4048.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4940.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1942.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2663.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1243.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4725.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3415.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3925.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2431.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3911.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1687.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio305.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2087.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1484.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5150.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio578.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2392.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4984.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4408.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2172.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1181.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2669.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3721.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4311.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3373.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2520.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio698.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1720.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1138.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio217.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1804.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1124.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio572.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3109.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4436.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4504.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4133.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio970.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio125.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3352.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4814.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio902.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3611.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3610.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1375.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio676.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5119.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4747.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4526.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio791.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio665.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2621.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3483.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4465.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1356.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1299.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1520.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio483.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3876.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1534.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4880.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3158.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4954.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4879.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio750.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1358.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4532.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4697.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1757.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2355.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio415.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5060.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1954.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1842.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3629.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2905.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio997.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2798.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4630.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3253.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1852.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3550.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1718.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio754.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2720.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2001.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio802.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1973.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1577.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3215.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2006.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1454.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4178.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio49.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4223.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio39.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3423.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3810.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3390.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4721.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3536.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2463.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2736.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3061.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3163.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2899.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5155.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3122.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2026.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3670.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4590.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3078.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1982.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1131.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4430.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3797.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3446.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2364.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio994.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio899.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3049.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio614.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio833.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2497.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5025.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4839.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1311.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1391.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2913.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1559.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1273.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio140.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3052.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2391.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1599.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1941.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3725.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1677.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio473.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio637.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4180.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2398.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4455.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4146.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio685.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio81.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4252.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3676.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3430.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2230.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4659.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5109.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio9.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1422.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1262.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4520.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1081.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1583.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1333.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5077.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio509.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4895.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1253.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2645.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2894.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio124.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1879.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3263.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4158.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4170.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5034.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1828.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio55.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4498.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1617.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2399.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1221.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3623.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1427.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1860.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2740.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio456.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2486.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3146.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4448.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio326.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2512.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4767.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1888.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4369.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4164.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio339.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5033.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5067.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio89.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4633.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio295.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5002.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4115.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4371.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2153.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio470.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3863.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2756.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1596.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1595.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2901.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1097.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5138.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5027.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio969.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4446.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio795.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4792.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3533.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio748.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1749.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio826.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio196.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3474.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio757.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1923.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio255.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4724.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1517.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio186.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2173.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1147.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4805.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3747.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio538.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4193.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1463.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2778.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio518.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio768.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1381.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3117.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2110.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3740.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2745.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1277.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1585.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio620.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4020.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio820.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio293.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2379.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5051.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4302.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2914.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3930.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1095.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3624.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2957.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2580.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3602.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3466.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio133.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2902.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1563.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1083.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4172.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1390.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3898.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio380.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1091.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio281.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3173.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1021.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio831.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1822.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1795.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio173.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3313.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5008.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio238.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3744.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4952.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio44.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1961.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2268.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3788.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2506.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4683.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1760.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4186.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio735.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4098.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio609.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1115.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio823.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio626.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3937.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3491.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio459.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2154.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2092.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4704.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2229.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio856.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2220.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3588.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4067.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4087.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4100.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1110.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio278.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5147.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio769.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4336.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1556.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio827.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1957.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2831.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4113.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3445.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2225.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1426.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3594.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2211.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1713.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2631.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio898.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4433.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio26.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4871.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio330.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2517.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4754.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1560.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2020.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio363.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3002.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio15.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2129.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3378.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1460.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3650.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2482.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2998.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4896.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4668.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3156.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio135.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4388.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2041.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4531.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3992.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1497.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio395.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4420.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3329.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio570.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4826.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1249.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3552.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio692.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3821.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1301.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio152.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2488.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1104.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio8.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2855.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4016.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1386.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4928.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3862.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3998.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1327.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3140.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2982.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2289.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio279.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio924.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3348.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1570.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio547.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4419.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3365.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3239.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1403.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1189.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2991.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3741.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3216.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4929.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4934.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3179.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3367.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio262.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3053.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2866.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4218.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio918.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3144.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1385.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio770.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1506.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4946.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1019.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio154.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2209.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3294.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2581.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3411.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3320.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4661.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1475.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3590.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio289.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio981.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2242.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3318.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4688.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4877.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1160.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio562.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3205.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2126.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2322.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3617.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4485.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3880.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4527.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4088.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3545.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio574.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3015.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4669.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1948.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1420.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1248.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio224.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1761.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1194.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4748.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2731.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4537.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3434.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2871.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3444.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2508.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2394.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2772.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4440.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2152.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3518.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2127.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3026.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2858.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4705.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2817.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio405.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4110.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3003.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3407.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1930.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2384.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2234.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5117.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2890.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio936.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1033.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2084.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1665.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4167.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4897.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4875.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1216.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio476.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3314.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio849.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3368.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio482.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1528.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2586.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio891.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2582.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2038.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5010.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2917.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio104.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2013.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3203.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3540.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2585.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4391.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5090.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2119.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1938.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1015.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4344.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1614.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio779.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1744.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4933.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1032.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2510.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1659.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1868.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1829.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2651.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2396.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3048.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5083.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2544.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2272.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3243.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4014.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2509.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio520.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3968.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4598.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1190.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1730.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3186.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3809.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5040.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4022.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio720.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1799.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3119.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio741.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2285.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3037.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1137.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1689.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio679.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1586.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4821.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1910.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3027.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2566.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2604.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4533.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1226.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3555.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1413.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1859.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio450.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio703.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio988.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1519.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio439.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2965.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4270.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1729.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3682.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2162.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2676.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2332.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3507.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2093.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2168.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3907.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4496.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4188.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1685.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4060.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2436.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2224.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio537.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio294.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2019.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio681.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2314.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2417.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4793.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1089.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2990.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5080.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1108.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3764.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio670.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2245.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4779.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4899.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4508.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3306.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2053.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2167.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3353.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3034.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio922.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3284.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2978.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3134.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3834.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3705.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1511.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2803.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1473.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1258.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2932.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio742.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4332.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio236.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4938.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1582.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2655.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2568.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio172.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4807.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1012.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio541.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio555.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1592.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio743.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio544.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4086.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1288.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1573.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3160.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4026.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3892.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2775.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2320.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3785.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2256.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5097.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio27.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio636.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio690.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1905.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2424.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2734.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio119.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3032.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4731.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2002.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4912.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio857.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2910.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3089.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3703.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2460.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2070.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio48.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5044.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1256.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1639.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2101.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1352.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4939.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3949.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2560.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio299.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3391.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio834.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4233.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2912.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4503.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2116.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2297.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3565.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4005.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1726.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3115.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio932.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3773.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio142.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4250.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3745.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio629.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4574.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2846.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio563.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio927.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4392.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio842.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2874.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4122.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3083.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2447.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio762.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1561.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4920.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1135.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4515.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1970.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1781.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4334.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2301.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3162.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2843.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1924.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2693.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5045.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2627.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4592.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4523.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio47.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2249.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2456.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3817.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2411.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio652.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3213.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3665.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3359.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio392.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio420.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3919.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio369.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3547.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2056.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio416.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4860.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1278.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4542.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio503.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4620.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2879.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4774.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio767.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4922.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2454.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4222.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3860.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio492.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio45.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio838.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3029.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio709.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1371.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1026.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4232.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3437.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4740.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio642.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1507.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio106.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1530.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3056.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1410.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4894.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio355.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2066.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2071.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4808.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio111.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4156.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio885.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1009.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4216.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4267.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio500.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4030.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2576.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4853.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio871.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4777.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2088.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2716.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2887.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1814.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2735.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1692.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio160.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio453.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2928.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3714.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4211.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3431.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1959.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4667.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3075.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3872.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2952.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3627.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1157.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3928.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1073.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1566.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3226.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3426.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2523.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio875.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3405.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4189.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2836.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3889.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1057.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio419.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4665.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1656.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio526.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4140.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1118.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1527.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1891.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio74.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3198.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3527.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio448.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1474.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio973.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4587.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1887.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2911.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1752.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio524.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1309.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5076.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3525.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4686.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio861.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2977.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4848.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3746.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2713.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio409.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1590.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3401.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3351.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1233.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio723.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio591.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4988.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4772.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1782.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1254.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4876.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4823.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4937.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2292.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3958.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio250.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio481.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2083.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1812.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2282.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3169.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4935.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3395.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1827.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1765.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1126.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio40.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4324.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2327.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4378.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1877.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1926.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4859.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2481.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3542.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1964.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4745.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1291.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2189.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4128.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio457.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4284.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3935.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3593.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2652.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4282.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3807.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1098.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1365.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2769.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4024.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1419.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio863.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio383.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio712.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2040.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3612.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio353.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1223.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5082.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4693.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4758.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3432.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2985.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2893.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2539.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3212.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4829.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4495.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1746.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2149.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4599.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio908.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1925.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4385.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4985.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4462.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio159.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2473.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4304.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2277.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3478.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4239.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3546.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio79.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2727.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4280.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1838.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio659.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2863.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3750.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2538.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio564.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3649.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3973.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5156.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3984.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1005.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1289.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3409.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5094.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3589.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1680.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3105.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2259.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio187.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1265.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1843.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2984.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4359.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3597.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio662.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4043.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1621.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2541.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3468.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio310.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2583.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3947.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3567.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3854.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2705.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3570.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4813.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1107.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2139.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3498.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4093.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3286.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio655.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4142.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5070.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3568.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2165.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5003.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4023.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2927.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1435.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio587.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3748.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2074.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1916.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1263.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5087.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2854.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2800.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio105.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2484.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4855.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4410.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4558.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3758.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1977.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2738.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2969.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5153.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio641.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio488.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3982.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4231.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5136.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4662.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4103.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2600.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3929.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3595.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5121.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio71.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio867.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3798.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3805.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4293.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1841.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2930.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2312.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1162.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1499.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio335.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3121.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3361.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1896.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3270.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1915.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3110.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1700.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3743.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio533.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio582.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4525.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3578.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3362.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2721.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1117.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4437.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio705.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio954.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio772.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio796.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4207.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3794.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1093.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1445.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2021.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1448.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2658.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1575.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio145.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio22.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2244.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2350.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3042.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4089.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3059.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3007.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3710.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio599.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4634.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3225.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio240.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4123.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3044.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1722.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4664.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio774.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1779.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3952.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio341.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio721.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2271.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3701.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio657.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio19.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4746.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1431.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4152.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2593.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2818.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio20.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3530.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2703.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3310.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio328.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3081.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5113.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1192.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1298.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1943.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4441.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio297.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1434.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1636.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1231.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio511.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2213.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4524.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2440.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio430.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4000.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1180.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4997.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1572.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2637.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1736.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3428.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3454.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1373.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4882.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio727.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3201.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4674.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3224.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3620.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio394.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2413.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3016.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2474.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1022.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2617.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1750.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2136.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2554.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1139.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1336.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1975.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2816.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4191.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2352.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio596.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio164.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1515.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3287.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1440.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1629.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio354.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio716.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3598.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2169.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio32.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2579.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2313.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5075.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4421.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3783.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2330.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1884.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2592.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio269.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2324.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5014.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1355.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3849.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio957.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2280.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4628.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio261.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2412.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3842.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1125.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio531.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1479.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3300.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1851.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3499.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio228.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1292.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3659.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1153.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1113.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3852.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3896.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3738.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4479.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2418.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2319.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2349.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1341.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4842.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3251.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio242.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2892.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3831.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1658.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2414.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1893.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio451.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2094.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1446.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2304.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2270.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1775.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5023.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2195.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4975.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2821.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1946.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio725.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3278.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5054.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2915.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3993.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio864.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2524.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3636.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio358.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2797.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2787.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2515.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4333.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1461.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio85.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio60.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3402.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1605.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4130.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio848.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2459.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4259.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1120.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1986.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2022.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1234.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2648.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1567.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio822.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3983.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4072.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio602.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio182.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio850.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4644.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio782.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1006.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio646.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3723.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2534.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3090.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2519.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2047.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4080.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio162.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3308.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio576.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4726.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3819.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4205.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5152.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3403.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4255.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3822.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio610.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3713.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4394.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3371.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3069.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2145.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4921.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3613.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1776.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1286.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2757.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio381.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3844.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio132.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2880.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2771.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2266.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2124.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio756.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3728.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3234.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio329.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3575.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio201.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3957.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2939.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio158.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4006.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4423.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2958.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3637.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2052.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3733.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1061.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4346.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1053.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1516.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio895.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4165.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio17.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2232.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio313.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4990.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4046.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio229.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1303.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4461.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1281.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3603.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2988.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1624.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio621.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3566.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio370.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio897.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3679.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4463.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2263.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3139.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2012.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3658.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3045.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3667.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4815.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3847.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3167.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio613.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4091.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2231.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3843.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4540.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1696.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4966.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio272.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3616.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3096.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio639.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio143.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio30.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4580.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4426.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1482.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3639.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1947.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3853.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3116.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1807.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4002.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3768.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1170.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1411.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3324.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2702.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2387.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio797.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2884.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1983.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2796.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1146.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4327.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3644.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3691.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2809.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio658.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio651.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio700.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio608.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1745.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2706.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1191.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4611.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4299.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1041.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4684.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1994.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1764.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2595.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio168.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3200.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1200.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio868.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2752.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2042.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5140.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4126.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio877.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio6.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4374.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio959.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3560.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1742.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4297.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3256.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3496.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5144.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3193.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4312.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1608.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2407.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio507.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2057.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2632.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio185.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2461.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio675.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1174.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4460.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4858.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4055.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2055.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3181.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1158.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1048.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4732.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1740.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4567.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2089.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1688.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio731.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3416.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio666.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2226.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1826.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3573.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio11.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio101.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1626.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3333.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3995.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4834.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2366.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4470.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3060.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2599.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2451.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3024.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4555.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1205.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4288.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio886.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio52.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5106.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3812.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio166.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2920.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3866.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4200.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio98.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2629.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2069.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3966.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3599.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4790.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3722.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4084.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio100.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio583.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5088.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio888.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio739.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio883.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2981.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio83.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3178.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1297.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1370.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3894.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4623.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2215.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3230.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4358.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1166.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio704.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio713.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4356.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2659.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2848.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4206.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4708.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio592.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio945.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1339.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1064.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3662.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2723.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1898.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4603.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio950.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3418.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2793.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3386.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4803.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1962.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2160.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3787.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3683.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3918.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4509.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2477.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1850.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3688.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1882.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3108.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio804.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio73.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4169.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4546.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio203.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3340.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio479.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5049.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5065.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2252.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3450.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3652.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3508.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4355.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio995.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio179.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3558.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3164.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1670.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4171.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1836.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3625.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio985.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3841.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio14.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2710.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3504.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4343.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio597.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4980.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4443.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio711.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1618.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2815.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3283.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio16.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4653.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4637.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1675.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2750.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio460.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1346.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2926.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2286.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1885.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3202.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3237.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio893.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3950.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio933.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4529.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1793.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4101.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2561.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1805.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3926.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5006.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio209.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3334.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3502.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio361.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4143.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4041.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4874.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio996.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1050.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4552.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5099.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio726.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio939.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2551.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio776.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4290.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio93.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3453.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2657.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5035.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio906.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2946.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2333.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1798.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3752.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio286.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2643.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4501.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio807.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio892.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2644.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5018.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio59.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4376.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4547.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio684.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio241.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3492.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3912.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4752.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3767.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3938.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4138.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2840.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1901.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4932.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4134.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3183.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3161.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio775.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2130.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4735.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio546.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio107.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4872.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2306.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2104.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2058.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2185.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1867.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1651.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5032.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1123.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2064.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2240.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2963.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1686.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4768.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio580.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio780.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1927.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3991.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1133.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1922.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1264.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1134.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio494.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2246.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4812.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1345.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3012.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4367.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2587.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio225.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3079.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio755.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4945.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio431.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4888.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio360.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio496.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3626.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3413.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5039.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio530.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3514.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2351.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2395.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3694.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4658.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2790.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3143.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4254.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4409.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3696.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2347.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4800.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4160.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3832.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4179.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1384.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4289.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3692.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3363.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1581.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4401.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2596.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3236.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio508.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2819.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1182.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio204.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5127.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3067.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2715.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1643.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4004.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3347.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4370.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3176.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2860.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1642.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1168.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1684.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4322.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2054.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2200.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio447.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio208.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio244.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3485.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3290.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4646.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4974.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2562.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2273.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2661.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1913.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3464.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2060.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2148.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4248.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio682.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4716.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio389.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1304.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4788.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1840.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio825.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3443.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4246.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio284.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio539.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3456.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1414.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4696.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2744.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4948.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3816.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3055.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4406.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4262.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1211.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1155.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3480.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4925.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3727.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio828.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4989.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3019.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3630.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2328.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5101.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio320.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio276.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2954.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4064.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4606.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio153.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3577.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4837.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1114.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio404.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio760.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio491.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1969.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1602.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2269.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio987.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4785.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio628.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1469.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4352.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio947.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3021.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3913.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1043.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3252.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4843.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio746.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5030.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4651.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio433.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1285.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1815.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4729.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio960.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2931.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4822.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4780.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3136.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3628.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4125.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4375.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1697.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4215.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3592.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio678.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4924.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1652.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4864.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4505.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4464.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1193.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1500.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4730.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2184.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3350.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4715.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2191.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio280.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3871.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2700.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1847.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4176.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3035.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4326.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4182.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2386.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2678.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1354.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2363.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2393.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2288.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2032.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4082.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1574.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio982.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2711.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3289.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2472.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1832.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio758.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4609.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2111.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2404.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2329.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1128.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1307.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio798.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1361.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2933.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio220.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1348.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1990.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio375.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2535.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2250.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3372.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3272.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3543.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1323.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1667.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2837.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3033.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4008.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4698.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio839.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2789.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4390.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3132.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4648.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1541.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio696.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio205.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2983.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4857.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2689.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio589.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio505.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3845.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2099.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5061.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1368.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1056.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1004.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2098.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2150.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4528.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2768.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4868.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio366.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3471.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4916.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2830.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1682.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2824.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2128.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1068.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1568.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3666.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3677.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2801.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1796.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1185.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2163.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2233.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3214.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1470.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2636.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1984.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4413.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1364.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio403.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1140.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4264.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4427.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3463.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1554.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3572.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4663.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio761.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2956.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4593.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3068.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio254.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio862.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1787.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio69.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3749.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1603.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1710.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3731.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2491.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2666.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3385.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2435.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio116.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1985.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3451.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4783.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4562.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio919.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2095.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2607.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3309.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3674.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1627.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3241.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2097.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2794.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2878.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2938.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4713.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio792.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3101.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio239.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4389.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio400.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio810.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3801.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4396.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4073.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5011.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4104.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3779.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4770.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio70.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2730.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2367.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5102.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4577.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio192.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio738.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1650.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1806.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3641.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2115.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3384.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1754.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4027.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio630.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2294.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio233.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3814.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3020.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3882.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4069.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio880.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1809.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4217.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3097.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4795.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2610.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3248.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1412.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio910.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4601.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2343.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1119.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4886.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio120.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio889.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1987.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3655.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1699.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio811.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3006.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1242.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1052.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1960.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1342.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio477.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio401.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2888.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio808.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2005.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3436.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio306.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4702.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5125.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3209.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3717.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio733.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio373.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4881.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1974.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5098.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2514.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3936.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4563.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3761.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio680.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3343.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4678.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2755.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio766.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1116.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2882.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4992.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4794.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2646.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4070.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio645.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3249.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4194.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4616.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3829.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4627.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio671.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5135.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4710.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4588.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4471.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2181.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio691.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4972.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2525.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1218.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2886.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3742.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2203.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4181.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3497.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio308.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5084.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3389.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4411.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2279.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3408.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3377.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2102.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2967.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3675.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio376.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1579.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1430.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4011.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2278.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4306.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2307.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio901.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3729.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4350.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3331.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2948.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2531.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3280.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2500.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5115.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4309.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio813.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio267.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio934.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3838.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5091.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2999.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1878.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4530.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4981.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3951.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1928.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4261.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1130.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4744.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1662.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1267.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3102.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3349.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3030.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2031.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1349.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3477.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio270.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4964.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4941.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4764.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3962.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3307.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3360.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1335.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio946.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4749.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3447.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2175.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4873.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1102.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio171.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2970.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1276.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3516.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1241.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1236.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3796.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5133.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4214.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2630.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3519.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2532.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2741.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio92.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1953.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4849.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2241.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio781.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3410.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3017.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3732.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio475.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4586.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2714.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3663.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3917.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2814.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3850.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3980.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1092.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4015.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1090.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4221.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2197.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5086.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2177.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio728.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2898.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2112.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3646.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4737.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1902.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3174.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio183.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3355.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4456.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio28.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1487.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3112.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio127.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1406.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3247.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1424.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio18.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3133.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3539.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3080.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio912.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio434.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio887.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2653.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2795.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3031.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio759.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1462.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3325.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4535.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2223.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3282.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2061.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio56.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio128.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1215.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2212.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2048.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio859.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3208.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3867.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio606.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3316.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3018.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2336.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2891.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2613.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2859.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3734.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3505.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio347.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2121.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3895.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3204.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1956.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1212.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2718.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3715.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1389.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4818.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4846.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4930.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1810.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4383.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio522.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4381.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3070.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio393.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio175.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4257.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3569.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3319.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2151.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3977.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio222.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2237.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4228.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1441.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1963.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2856.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1989.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3638.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4854.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4056.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3512.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3718.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio25.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio517.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2758.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5116.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2100.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1768.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1620.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1513.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4271.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4615.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2470.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4201.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio180.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2421.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3680.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2875.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2968.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1811.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1818.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio275.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4450.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1096.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2216.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1679.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2331.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4703.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1825.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2976.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4044.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2086.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4618.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5130.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2140.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2368.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4402.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3417.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2571.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4763.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3088.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio426.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio824.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2390.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5038.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4709.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4856.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1998.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3790.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1492.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3524.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1274.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio837.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3375.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1518.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio540.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2478.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4497.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3808.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1848.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2922.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio920.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1615.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3736.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1900.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio62.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2842.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1920.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio978.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1400.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1246.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4736.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio76.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1770.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3266.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3113.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1645.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1545.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5063.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2521.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4127.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1997.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2649.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3606.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1802.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio384.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2852.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4417.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4844.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2529.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2811.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3673.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio90.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio122.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2178.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2439.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4806.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4671.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1709.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2696.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2622.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2654.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio219.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio632.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1547.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3915.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4507.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2679.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2974.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4723.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2876.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3452.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1423.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3969.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1786.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2906.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1480.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3180.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2810.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3025.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio714.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4625.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1141.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4386.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2248.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3712.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2146.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio819.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio88.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2293.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio421.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4722.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4361.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4575.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1565.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4418.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3312.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1712.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1038.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4373.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2950.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio928.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2634.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2527.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4733.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio983.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio307.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3427.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3669.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio617.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1360.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio687.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4608.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1540.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4357.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio478.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1314.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3940.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio722.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3217.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio661.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2791.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1259.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4366.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2940.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4174.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1408.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4097.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio740.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4489.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3986.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio234.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2449.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio87.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio103.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2923.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio256.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2542.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio667.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4458.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5123.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2433.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4701.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4755.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3244.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3948.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3467.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2633.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3291.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2701.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1611.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio504.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2945.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio640.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4316.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4105.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2591.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4816.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2434.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4903.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2157.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1917.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2694.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3233.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2378.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2739.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1955.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2573.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio869.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1230.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5137.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4472.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4283.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2370.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4845.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1062.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1803.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1247.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1695.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3298.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4631.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5089.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3187.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio708.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3755.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2812.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4111.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3632.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3999.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2719.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2537.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio63.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1906.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1992.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2557.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1374.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio232.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4066.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4968.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3255.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio853.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1845.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3240.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4141.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1224.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5012.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1260.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio612.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2552.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1823.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4987.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3782.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4009.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1792.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2028.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4676.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3039.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1993.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio466.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio967.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio115.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4836.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2760.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3299.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2134.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio365.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3654.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4377.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4622.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio925.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2847.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3335.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1164.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5000.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1245.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2536.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2251.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3194.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3399.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2075.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2618.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2358.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4431.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2008.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4454.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2188.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3975.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2141.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio314.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4403.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1646.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2143.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4711.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2180.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3304.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1653.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1728.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2947.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio33.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4904.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2763.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1640.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3484.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1871.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4926.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1723.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2236.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2664.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4071.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3855.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2626.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1432.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4399.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3916.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3668.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5146.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3040.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2493.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3963.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1271.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio300.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3608.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio190.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3111.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio54.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1716.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1350.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2090.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2835.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2724.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio263.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio536.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3885.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio412.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2159.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1831.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2547.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio512.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2107.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1244.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4124.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4310.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio251.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4544.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1186.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2346.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1785.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3509.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3206.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1151.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio935.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4452.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3421.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio23.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1526.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4247.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4991.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5036.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2687.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio900.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4162.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1635.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3781.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio35.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1774.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4154.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1553.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio527.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4287.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4062.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4944.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2764.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2690.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2857.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2487.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1846.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio729.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1508.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio783.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1600.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2325.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3092.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1063.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio342.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio231.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1077.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2616.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2556.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4029.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1521.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4677.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2691.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5007.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3273.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4787.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1332.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2290.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio948.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2937.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio894.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1184.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4274.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3460.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4149.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio660.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio34.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1436.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1238.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1593.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3653.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1338.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1008.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1551.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3615.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio331.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio844.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio391.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio445.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1439.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3279.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3103.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1824.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3582.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio818.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2783.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3690.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio193.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1269.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1708.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3704.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1013.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio558.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4491.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio147.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1644.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4522.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2085.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3529.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3118.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3751.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio150.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2883.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3199.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3400.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio277.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4474.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2036.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4570.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4227.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2513.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3784.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2204.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3196.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3868.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2430.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1649.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2839.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4438.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio943.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3475.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio402.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2785.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2073.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4365.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3220.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2503.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1225.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2748.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1496.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio57.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1106.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4077.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio139.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3420.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3487.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4349.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4397.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3883.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2792.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4031.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3932.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1046.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3943.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3795.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4891.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2563.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio843.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio573.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4196.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1493.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4953.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio567.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1136.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio266.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1858.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3189.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1494.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4315.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2572.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1633.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4119.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1094.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio467.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1466.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio257.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio465.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio12.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio605.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio80.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio961.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1378.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3874.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3621.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1788.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3884.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio663.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3708.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5148.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1014.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3553.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio917.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4660.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4915.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3647.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4237.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2776.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio230.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1934.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio485.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio809.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1040.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2027.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1886.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4007.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3211.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3188.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1880.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3737.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4983.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1067.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3398.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2820.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1044.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2681.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2485.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3258.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3879.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3004.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2709.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2962.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4148.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1452.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio449.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3587.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2680.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3554.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4329.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2109.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio787.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio413.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2287.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4804.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2193.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3689.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio559.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1047.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio396.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3191.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1401.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2975.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4573.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2619.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2761.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3369.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2877.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4272.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4827.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5111.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3657.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio268.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3858.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio550.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio210.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio664.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4961.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4654.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1058.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3472.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio287.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4236.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4139.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4313.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3379.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4594.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1453.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio944.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio568.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2044.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1280.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2261.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2033.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3344.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio283.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3490.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4657.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3979.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4621.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4734.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2490.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3601.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3818.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio955.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3687.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1325.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3945.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3771.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2642.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1363.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio548.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2754.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio879.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1509.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3064.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4379.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1035.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio951.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio377.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4404.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1175.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio227.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1714.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2475.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4153.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4892.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2067.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio724.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2218.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2492.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1876.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3535.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1471.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2505.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4395.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3192.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2995.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1343.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2608.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3185.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4738.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2851.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2773.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2257.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1705.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4565.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3672.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1546.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1045.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2668.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio764.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio13.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3231.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio7.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2885.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1127.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio593.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2362.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1933.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1316.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio941.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1929.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1312.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2872.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4743.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1161.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2704.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4514.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3495.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2564.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio486.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5066.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio248.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3023.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3839.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2670.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1405.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2598.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio777.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio21.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2158.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4405.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2896.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1122.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2299.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1542.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2864.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1988.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2677.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3322.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio362.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4268.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3422.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3107.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio631.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2868.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio706.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio332.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4695.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3856.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2684.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1142.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4511.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3354.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio577.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio113.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1357.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4183.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4819.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2479.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1502.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1379.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio814.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio446.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4109.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4107.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1919.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio635.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1610.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3910.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio75.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4308.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2834.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio292.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3698.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1305.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2921.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2455.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio603.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2426.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2865.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio841.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5142.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2125.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1188.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1438.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4190.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3297.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5048.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4832.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio67.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4384.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1464.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4942.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2802.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio975.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3763.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2501.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1668.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3890.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1210.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4042.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5050.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio668.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1589.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3806.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3574.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio942.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3227.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4802.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4566.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio252.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio58.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5058.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio515.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4778.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2641.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1079.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio148.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio926.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio763.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3584.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2326.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1082.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1604.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1549.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2625.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1833.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1883.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2462.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4863.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2068.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3235.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio245.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio851.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio437.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio697.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio333.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio407.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1935.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2335.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3242.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4979.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio876.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2686.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1619.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1334.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1755.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1121.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio914.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4720.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1294.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4765.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3521.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2190.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1149.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4604.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4235.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2009.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1165.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3141.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3469.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1306.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3517.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3792.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4898.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1187.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3987.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2080.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2164.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2685.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4061.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio176.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4490.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1443.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4951.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1510.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3406.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio260.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4852.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1724.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1030.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2217.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1634.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1197.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio832.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4017.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3292.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2123.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4784.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4680.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio417.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4901.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4572.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2108.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1495.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio349.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio195.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3891.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2712.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2323.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1657.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio356.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4112.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio259.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4591.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2850.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4666.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3166.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2348.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3142.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1672.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3274.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2609.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1372.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2077.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4245.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4850.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1039.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2813.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio388.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio847.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3095.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1817.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2936.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1532.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4568.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3170.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio194.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1971.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio903.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3155.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1228.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3246.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1270.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio282.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1459.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio237.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2339.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1856.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio734.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3228.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2305.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3376.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3149.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3706.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio218.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3168.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1417.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3099.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio884.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3104.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio181.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio108.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3697.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio789.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4585.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4619.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio428.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4645.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2281.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio594.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4435.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1907.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio199.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4679.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio923.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio689.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio803.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio336.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1616.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3506.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3651.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4265.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2728.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2742.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1813.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3811.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3726.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5055.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1214.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1399.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2018.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1302.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio149.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio323.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3448.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3893.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3900.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3071.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3131.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1777.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4137.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1683.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2388.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3285.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4224.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3579.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio896.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3906.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4185.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3586.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3851.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio672.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio976.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4655.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3374.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2122.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4266.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1007.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5068.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3941.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio806.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3780.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5024.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio5064.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3804.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3864.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2935.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio744.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4893.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1478.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3671.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4927.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4251.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4840.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio435.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2853.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3678.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio3062.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio1396.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio4887.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2781.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2425.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio2132.wav
/kaggle/input/datahrbn/MyTTSDataset/wavs/audio855.wav
pip install TTS
Collecting TTS
Downloading TTS-0.22.0-cp311-cp311-manylinux1_x86_64.whl.metadata (21 kB)
Requirement already satisfied: cython>=0.29.30 in /usr/local/lib/python3.11/dist-packages (from TTS) (3.0.12)
Requirement already satisfied: scipy>=1.11.2 in /usr/local/lib/python3.11/dist-packages (from TTS) (1.15.2)
Requirement already satisfied: torch>=2.1 in /usr/local/lib/python3.11/dist-packages (from TTS) (2.6.0+cu124)
Requirement already satisfied: torchaudio in /usr/local/lib/python3.11/dist-packages (from TTS) (2.6.0+cu124)
Requirement already satisfied: soundfile>=0.12.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (0.13.1)
Requirement already satisfied: librosa>=0.10.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (0.11.0)
Collecting scikit-learn>=1.3.0 (from TTS)
Downloading scikit_learn-1.6.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
Requirement already satisfied: inflect>=5.6.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (7.5.0)
Requirement already satisfied: tqdm>=4.64.1 in /usr/local/lib/python3.11/dist-packages (from TTS) (4.67.1)
Collecting anyascii>=0.3.0 (from TTS)
Downloading anyascii-0.3.2-py3-none-any.whl.metadata (1.5 kB)
Requirement already satisfied: pyyaml>=6.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (6.0.2)
Requirement already satisfied: fsspec>=2023.6.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (2025.3.2)
Requirement already satisfied: aiohttp>=3.8.1 in /usr/local/lib/python3.11/dist-packages (from TTS) (3.11.18)
Requirement already satisfied: packaging>=23.1 in /usr/local/lib/python3.11/dist-packages (from TTS) (25.0)
Requirement already satisfied: flask>=2.0.1 in /usr/local/lib/python3.11/dist-packages (from TTS) (3.1.0)
Collecting pysbd>=0.3.4 (from TTS)
Downloading pysbd-0.3.4-py3-none-any.whl.metadata (6.1 kB)
Requirement already satisfied: umap-learn>=0.5.1 in /usr/local/lib/python3.11/dist-packages (from TTS) (0.5.7)
Collecting pandas<2.0,>=1.4 (from TTS)
Downloading pandas-1.5.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Requirement already satisfied: matplotlib>=3.7.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (3.7.2)
Collecting trainer>=0.0.32 (from TTS)
Downloading trainer-0.0.36-py3-none-any.whl.metadata (8.1 kB)
Collecting coqpit>=0.0.16 (from TTS)
Downloading coqpit-0.0.17-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: jieba in /usr/local/lib/python3.11/dist-packages (from TTS) (0.42.1)
Collecting pypinyin (from TTS)
Downloading pypinyin-0.54.0-py2.py3-none-any.whl.metadata (12 kB)
Collecting hangul-romanize (from TTS)
Downloading hangul_romanize-0.1.0-py3-none-any.whl.metadata (1.2 kB)
Collecting gruut==2.2.3 (from gruut[de,es,fr]==2.2.3->TTS)
Downloading gruut-2.2.3.tar.gz (73 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.5/73.5 kB 3.3 MB/s eta 0:00:00
Preparing metadata (setup.py) ... done
Collecting jamo (from TTS)
Downloading jamo-0.4.1-py3-none-any.whl.metadata (2.3 kB)
Requirement already satisfied: nltk in /usr/local/lib/python3.11/dist-packages (from TTS) (3.9.1)
Collecting g2pkk>=0.1.1 (from TTS)
Downloading g2pkk-0.1.2-py3-none-any.whl.metadata (2.0 kB)
Collecting bangla (from TTS)
Downloading bangla-0.0.5-py3-none-any.whl.metadata (4.7 kB)
Collecting bnnumerizer (from TTS)
Downloading bnnumerizer-0.0.2.tar.gz (4.7 kB)
Preparing metadata (setup.py) ... done
Collecting bnunicodenormalizer (from TTS)
Downloading bnunicodenormalizer-0.1.7-py3-none-any.whl.metadata (22 kB)
Requirement already satisfied: einops>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (0.8.1)
Requirement already satisfied: transformers>=4.33.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (4.51.3)
Collecting encodec>=0.1.1 (from TTS)
Downloading encodec-0.1.1.tar.gz (3.7 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.7/3.7 MB 50.9 MB/s eta 0:00:00
Preparing metadata (setup.py) ... done
Collecting unidecode>=1.3.2 (from TTS)
Downloading Unidecode-1.4.0-py3-none-any.whl.metadata (13 kB)
Collecting num2words (from TTS)
Downloading num2words-0.5.14-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: spacy>=3 in /usr/local/lib/python3.11/dist-packages (from spacy[ja]>=3->TTS) (3.8.5)
Requirement already satisfied: numpy>=1.24.3 in /usr/local/lib/python3.11/dist-packages (from TTS) (1.26.4)
Requirement already satisfied: numba>=0.57.0 in /usr/local/lib/python3.11/dist-packages (from TTS) (0.60.0)
Requirement already satisfied: Babel<3.0.0,>=2.8.0 in /usr/local/lib/python3.11/dist-packages (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS) (2.17.0)
Collecting dateparser~=1.1.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS)
Downloading dateparser-1.1.8-py2.py3-none-any.whl.metadata (27 kB)
Collecting gruut-ipa<1.0,>=0.12.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS)
Downloading gruut-ipa-0.13.0.tar.gz (101 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.6/101.6 kB 8.1 MB/s eta 0:00:00
Preparing metadata (setup.py) ... done
Collecting gruut_lang_en~=2.0.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS)
Downloading gruut_lang_en-2.0.1.tar.gz (15.3 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.3/15.3 MB 82.9 MB/s eta 0:00:00
Preparing metadata (setup.py) ... done
Collecting jsonlines~=1.2.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS)
Downloading jsonlines-1.2.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting networkx<3.0.0,>=2.5.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS)
Downloading networkx-2.8.8-py3-none-any.whl.metadata (5.1 kB)
Collecting python-crfsuite~=0.9.7 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS)
Downloading python_crfsuite-0.9.11-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.3 kB)
Collecting gruut_lang_de~=2.0.0 (from gruut[de,es,fr]==2.2.3->TTS)
Downloading gruut_lang_de-2.0.1.tar.gz (18.1 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.1/18.1 MB 80.8 MB/s eta 0:00:00
Preparing metadata (setup.py) ... done
Collecting gruut_lang_es~=2.0.0 (from gruut[de,es,fr]==2.2.3->TTS)
Downloading gruut_lang_es-2.0.1.tar.gz (31.4 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 31.4/31.4 MB 58.3 MB/s eta 0:00:00
Preparing metadata (setup.py) ... done
Collecting gruut_lang_fr~=2.0.0 (from gruut[de,es,fr]==2.2.3->TTS)
Downloading gruut_lang_fr-2.0.2.tar.gz (10.9 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.9/10.9 MB 94.8 MB/s eta 0:00:00
Preparing metadata (setup.py) ... done
Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp>=3.8.1->TTS) (2.6.1)
Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp>=3.8.1->TTS) (1.3.2)
Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp>=3.8.1->TTS) (25.3.0)
Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp>=3.8.1->TTS) (1.6.0)
Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp>=3.8.1->TTS) (6.4.3)
Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp>=3.8.1->TTS) (0.3.1)
Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp>=3.8.1->TTS) (1.20.0)
Requirement already satisfied: Werkzeug>=3.1 in /usr/local/lib/python3.11/dist-packages (from flask>=2.0.1->TTS) (3.1.3)
Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from flask>=2.0.1->TTS) (3.1.6)
Requirement already satisfied: itsdangerous>=2.2 in /usr/local/lib/python3.11/dist-packages (from flask>=2.0.1->TTS) (2.2.0)
Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from flask>=2.0.1->TTS) (8.1.8)
Requirement already satisfied: blinker>=1.9 in /usr/local/lib/python3.11/dist-packages (from flask>=2.0.1->TTS) (1.9.0)
Requirement already satisfied: more_itertools>=8.5.0 in /usr/local/lib/python3.11/dist-packages (from inflect>=5.6.0->TTS) (10.6.0)
Requirement already satisfied: typeguard>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from inflect>=5.6.0->TTS) (4.4.2)
Requirement already satisfied: audioread>=2.1.9 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (3.0.1)
Requirement already satisfied: joblib>=1.0 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (1.5.0)
Requirement already satisfied: decorator>=4.3.0 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (4.4.2)
Requirement already satisfied: pooch>=1.1 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (1.8.2)
Requirement already satisfied: soxr>=0.3.2 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (0.5.0.post1)
Requirement already satisfied: typing_extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (4.13.2)
Requirement already satisfied: lazy_loader>=0.1 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (0.4)
Requirement already satisfied: msgpack>=1.0 in /usr/local/lib/python3.11/dist-packages (from librosa>=0.10.0->TTS) (1.1.0)
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib>=3.7.0->TTS) (1.3.1)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.11/dist-packages (from matplotlib>=3.7.0->TTS) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.11/dist-packages (from matplotlib>=3.7.0->TTS) (4.57.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib>=3.7.0->TTS) (1.4.8)
Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from matplotlib>=3.7.0->TTS) (11.1.0)
Requirement already satisfied: pyparsing<3.1,>=2.3.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib>=3.7.0->TTS) (3.0.9)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.11/dist-packages (from matplotlib>=3.7.0->TTS) (2.9.0.post0)
Collecting docopt>=0.6.2 (from num2words->TTS)
Downloading docopt-0.6.2.tar.gz (25 kB)
Preparing metadata (setup.py) ... done
Requirement already satisfied: llvmlite<0.44,>=0.43.0dev0 in /usr/local/lib/python3.11/dist-packages (from numba>=0.57.0->TTS) (0.43.0)
Requirement already satisfied: mkl_fft in /usr/local/lib/python3.11/dist-packages (from numpy>=1.24.3->TTS) (1.3.8)
Requirement already satisfied: mkl_random in /usr/local/lib/python3.11/dist-packages (from numpy>=1.24.3->TTS) (1.2.4)
Requirement already satisfied: mkl_umath in /usr/local/lib/python3.11/dist-packages (from numpy>=1.24.3->TTS) (0.1.1)
Requirement already satisfied: mkl in /usr/local/lib/python3.11/dist-packages (from numpy>=1.24.3->TTS) (2025.1.0)
Requirement already satisfied: tbb4py in /usr/local/lib/python3.11/dist-packages (from numpy>=1.24.3->TTS) (2022.1.0)
Requirement already satisfied: mkl-service in /usr/local/lib/python3.11/dist-packages (from numpy>=1.24.3->TTS) (2.4.1)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<2.0,>=1.4->TTS) (2025.2)
Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn>=1.3.0->TTS) (3.6.0)
Requirement already satisfied: cffi>=1.0 in /usr/local/lib/python3.11/dist-packages (from soundfile>=0.12.0->TTS) (1.17.1)
Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (3.0.12)
Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (1.0.5)
Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (1.0.12)
Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (2.0.11)
Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (3.0.9)
Requirement already satisfied: thinc<8.4.0,>=8.3.4 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (8.3.4)
Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (1.1.3)
Requirement already satisfied: srsly<3.0.0,>=2.4.3 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (2.5.1)
Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (2.0.10)
Requirement already satisfied: weasel<0.5.0,>=0.1.0 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (0.4.1)
Requirement already satisfied: typer<1.0.0,>=0.3.0 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (0.15.2)
Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (2.32.3)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (2.11.4)
Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (75.2.0)
Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /usr/local/lib/python3.11/dist-packages (from spacy>=3->spacy[ja]>=3->TTS) (3.5.0)
Collecting sudachipy!=0.6.1,>=0.5.2 (from spacy[ja]>=3->TTS)
Downloading SudachiPy-0.6.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)
Collecting sudachidict_core>=20211220 (from spacy[ja]>=3->TTS)
Downloading SudachiDict_core-20250129-py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (3.18.0)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (12.4.127)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (12.4.127)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (12.4.127)
Collecting nvidia-cudnn-cu12==9.1.0.70 (from torch>=2.1->TTS)
Downloading nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cublas-cu12==12.4.5.8 (from torch>=2.1->TTS)
Downloading nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cufft-cu12==11.2.1.3 (from torch>=2.1->TTS)
Downloading nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-curand-cu12==10.3.5.147 (from torch>=2.1->TTS)
Downloading nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting nvidia-cusolver-cu12==11.6.1.9 (from torch>=2.1->TTS)
Downloading nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)
Collecting nvidia-cusparse-cu12==12.3.1.170 (from torch>=2.1->TTS)
Downloading nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl.metadata (1.6 kB)
Requirement already satisfied: nvidia-cusparselt-cu12==0.6.2 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (0.6.2)
Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (2.21.5)
Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (12.4.127)
Collecting nvidia-nvjitlink-cu12==12.4.127 (from torch>=2.1->TTS)
Downloading nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)
Requirement already satisfied: triton==3.2.0 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (3.2.0)
Requirement already satisfied: sympy==1.13.1 in /usr/local/lib/python3.11/dist-packages (from torch>=2.1->TTS) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from sympy==1.13.1->torch>=2.1->TTS) (1.3.0)
Requirement already satisfied: psutil in /usr/local/lib/python3.11/dist-packages (from trainer>=0.0.32->TTS) (7.0.0)
Requirement already satisfied: tensorboard in /usr/local/lib/python3.11/dist-packages (from trainer>=0.0.32->TTS) (2.18.0)
Requirement already satisfied: huggingface-hub<1.0,>=0.30.0 in /usr/local/lib/python3.11/dist-packages (from transformers>=4.33.0->TTS) (0.31.1)
Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.11/dist-packages (from transformers>=4.33.0->TTS) (2024.11.6)
Requirement already satisfied: tokenizers<0.22,>=0.21 in /usr/local/lib/python3.11/dist-packages (from transformers>=4.33.0->TTS) (0.21.1)
Requirement already satisfied: safetensors>=0.4.3 in /usr/local/lib/python3.11/dist-packages (from transformers>=4.33.0->TTS) (0.5.3)
Requirement already satisfied: pynndescent>=0.5 in /usr/local/lib/python3.11/dist-packages (from umap-learn>=0.5.1->TTS) (0.5.13)
Requirement already satisfied: pycparser in /usr/local/lib/python3.11/dist-packages (from cffi>=1.0->soundfile>=0.12.0->TTS) (2.22)
Requirement already satisfied: tzlocal in /usr/local/lib/python3.11/dist-packages (from dateparser~=1.1.0->gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS) (5.3.1)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.30.0->transformers>=4.33.0->TTS) (1.1.0)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from Jinja2>=3.1.2->flask>=2.0.1->TTS) (3.0.2)
Requirement already satisfied: six in /usr/local/lib/python3.11/dist-packages (from jsonlines~=1.2.0->gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS) (1.17.0)
Requirement already satisfied: language-data>=1.2 in /usr/local/lib/python3.11/dist-packages (from langcodes<4.0.0,>=3.2.0->spacy>=3->spacy[ja]>=3->TTS) (1.3.0)
Requirement already satisfied: platformdirs>=2.5.0 in /usr/local/lib/python3.11/dist-packages (from pooch>=1.1->librosa>=0.10.0->TTS) (4.3.8)
Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=3->spacy[ja]>=3->TTS) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=3->spacy[ja]>=3->TTS) (2.33.2)
Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=3->spacy[ja]>=3->TTS) (0.4.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy>=3->spacy[ja]>=3->TTS) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy>=3->spacy[ja]>=3->TTS) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy>=3->spacy[ja]>=3->TTS) (2.4.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy>=3->spacy[ja]>=3->TTS) (2025.4.26)
Requirement already satisfied: blis<1.3.0,>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from thinc<8.4.0,>=8.3.4->spacy>=3->spacy[ja]>=3->TTS) (1.2.1)
Requirement already satisfied: confection<1.0.0,>=0.0.1 in /usr/local/lib/python3.11/dist-packages (from thinc<8.4.0,>=8.3.4->spacy>=3->spacy[ja]>=3->TTS) (0.1.5)
Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy>=3->spacy[ja]>=3->TTS) (1.5.4)
Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy>=3->spacy[ja]>=3->TTS) (14.0.0)
Requirement already satisfied: cloudpathlib<1.0.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy>=3->spacy[ja]>=3->TTS) (0.21.0)
Requirement already satisfied: smart-open<8.0.0,>=5.2.1 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy>=3->spacy[ja]>=3->TTS) (7.1.0)
Requirement already satisfied: intel-openmp<2026,>=2024 in /usr/local/lib/python3.11/dist-packages (from mkl->numpy>=1.24.3->TTS) (2024.2.0)
Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.11/dist-packages (from mkl->numpy>=1.24.3->TTS) (2022.1.0)
Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.11/dist-packages (from tbb==2022.*->mkl->numpy>=1.24.3->TTS) (1.3.0)
Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.11/dist-packages (from mkl_umath->numpy>=1.24.3->TTS) (2024.2.0)
Requirement already satisfied: absl-py>=0.4 in /usr/local/lib/python3.11/dist-packages (from tensorboard->trainer>=0.0.32->TTS) (1.4.0)
Requirement already satisfied: grpcio>=1.48.2 in /usr/local/lib/python3.11/dist-packages (from tensorboard->trainer>=0.0.32->TTS) (1.72.0rc1)
Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.11/dist-packages (from tensorboard->trainer>=0.0.32->TTS) (3.7)
Requirement already satisfied: protobuf!=4.24.0,>=3.19.6 in /usr/local/lib/python3.11/dist-packages (from tensorboard->trainer>=0.0.32->TTS) (3.20.3)
Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from tensorboard->trainer>=0.0.32->TTS) (0.7.2)
Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.11/dist-packages (from intel-openmp<2026,>=2024->mkl->numpy>=1.24.3->TTS) (2024.2.0)
Requirement already satisfied: marisa-trie>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy>=3->spacy[ja]>=3->TTS) (1.2.1)
Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3->spacy[ja]>=3->TTS) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3->spacy[ja]>=3->TTS) (2.19.1)
Requirement already satisfied: wrapt in /usr/local/lib/python3.11/dist-packages (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy>=3->spacy[ja]>=3->TTS) (1.17.2)
Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3->spacy[ja]>=3->TTS) (0.1.2)
Downloading TTS-0.22.0-cp311-cp311-manylinux1_x86_64.whl (937 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 938.0/938.0 kB 48.5 MB/s eta 0:00:00
Downloading anyascii-0.3.2-py3-none-any.whl (289 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 289.9/289.9 kB 15.7 MB/s eta 0:00:00
Downloading coqpit-0.0.17-py3-none-any.whl (13 kB)
Downloading g2pkk-0.1.2-py3-none-any.whl (25 kB)
Downloading num2words-0.5.14-py3-none-any.whl (163 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.5/163.5 kB 12.9 MB/s eta 0:00:00
Downloading pandas-1.5.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.0 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.0/12.0 MB 90.3 MB/s eta 0:00:00
Downloading pysbd-0.3.4-py3-none-any.whl (71 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.1/71.1 kB 5.6 MB/s eta 0:00:00
Downloading scikit_learn-1.6.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.5 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.5/13.5 MB 91.9 MB/s eta 0:00:00
Downloading nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl (363.4 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 363.4/363.4 MB 4.7 MB/s eta 0:00:00
Downloading nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl (664.8 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 664.8/664.8 MB 2.2 MB/s eta 0:00:00
Downloading nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl (211.5 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 211.5/211.5 MB 1.6 MB/s eta 0:00:00
Downloading nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl (56.3 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.3/56.3 MB 31.5 MB/s eta 0:00:00
Downloading nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl (127.9 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 127.9/127.9 MB 13.6 MB/s eta 0:00:00
Downloading nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl (207.5 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 207.5/207.5 MB 8.2 MB/s eta 0:00:00
Downloading nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (21.1 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 21.1/21.1 MB 75.0 MB/s eta 0:00:00
Downloading trainer-0.0.36-py3-none-any.whl (51 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 51.2/51.2 kB 3.6 MB/s eta 0:00:00
Downloading Unidecode-1.4.0-py3-none-any.whl (235 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 235.8/235.8 kB 19.1 MB/s eta 0:00:00
Downloading bangla-0.0.5-py3-none-any.whl (5.1 kB)
Downloading bnunicodenormalizer-0.1.7-py3-none-any.whl (23 kB)
Downloading hangul_romanize-0.1.0-py3-none-any.whl (4.6 kB)
Downloading jamo-0.4.1-py3-none-any.whl (9.5 kB)
Downloading pypinyin-0.54.0-py2.py3-none-any.whl (837 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 837.0/837.0 kB 39.2 MB/s eta 0:00:00
Downloading dateparser-1.1.8-py2.py3-none-any.whl (293 kB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 293.8/293.8 kB 20.0 MB/s eta 0:00:00
Downloading jsonlines-1.2.0-py2.py3-none-any.whl (7.6 kB)
Downloading networkx-2.8.8-py3-none-any.whl (2.0 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 69.2 MB/s eta 0:00:00
Downloading python_crfsuite-0.9.11-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 62.0 MB/s eta 0:00:00
Downloading SudachiDict_core-20250129-py3-none-any.whl (72.1 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 72.1/72.1 MB 24.4 MB/s eta 0:00:00
Downloading SudachiPy-0.6.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 75.4 MB/s eta 0:00:00
Building wheels for collected packages: gruut, encodec, bnnumerizer, docopt, gruut-ipa, gruut_lang_de, gruut_lang_en, gruut_lang_es, gruut_lang_fr
Building wheel for gruut (setup.py) ... done
Created wheel for gruut: filename=gruut-2.2.3-py3-none-any.whl size=75785 sha256=101ae09c5cd8f31fe989472c14dcc5df99b8051871954595a35b624e77e08866
Stored in directory: /root/.cache/pip/wheels/1f/a0/bc/4dacab52579ab464cffafbe7a8e3792dd36ad9ac288b264843
Building wheel for encodec (setup.py) ... done
Created wheel for encodec: filename=encodec-0.1.1-py3-none-any.whl size=45759 sha256=93e7203aea019ab94e14a65fc646815f8f0dbaca5c8a58b3ab4fd46186c9834c
Stored in directory: /root/.cache/pip/wheels/b4/a4/88/480018a664e58ca7ce6708759193ee51b017b3b72aa3df8a85
Building wheel for bnnumerizer (setup.py) ... done
Created wheel for bnnumerizer: filename=bnnumerizer-0.0.2-py3-none-any.whl size=5260 sha256=85fafa070a3901cd2906ac3ddcfce6ef3b7c8e5028e2384613394c9a50d29788
Stored in directory: /root/.cache/pip/wheels/9e/b9/e3/4145416693824818c0b931988a692676ecd4bbf2ea41d1eedd
Building wheel for docopt (setup.py) ... done
Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13706 sha256=23080d6d10e2a092b55fe7a6ac54ab79186ac40a3858e34ad83b2f543f67938d
Stored in directory: /root/.cache/pip/wheels/1a/b0/8c/4b75c4116c31f83c8f9f047231251e13cc74481cca4a78a9ce
Building wheel for gruut-ipa (setup.py) ... done
Created wheel for gruut-ipa: filename=gruut_ipa-0.13.0-py3-none-any.whl size=104873 sha256=caf6c51ddf49611ae38a3d73327a628db4cfe93a563908c02121d5148481554e
Stored in directory: /root/.cache/pip/wheels/c7/10/89/a5908dd7a9a032229684b7679396785e19f816667f788087fb
Building wheel for gruut_lang_de (setup.py) ... done
Created wheel for gruut_lang_de: filename=gruut_lang_de-2.0.1-py3-none-any.whl size=18498314 sha256=49eaec9c88d1704a0111a461e93c27abe43601fc6b967b7fbc49ce2a85c81315
Stored in directory: /root/.cache/pip/wheels/87/fa/df/5fdf5d3cc26ba859b8698a1f28581d1a6aa081edc6df9847ab
Building wheel for gruut_lang_en (setup.py) ... done
Created wheel for gruut_lang_en: filename=gruut_lang_en-2.0.1-py3-none-any.whl size=15326858 sha256=117632ca99761aafc755e45230c5febee4d6f5e0c13321ad42a86311428d8f1d
Stored in directory: /root/.cache/pip/wheels/06/30/52/dc5cd222b4bbde285838fed1f96636e96f85cd75493e79a978
Building wheel for gruut_lang_es (setup.py) ... done
Created wheel for gruut_lang_es: filename=gruut_lang_es-2.0.1-py3-none-any.whl size=32173927 sha256=cee81a8550b190236bfa0b6d45e2d23d3f592ffe6eae60714c5561cff13ec953
Stored in directory: /root/.cache/pip/wheels/c8/eb/59/30b5d15e56347e595f613036cbea0f807ad9621c75cd75d912
Building wheel for gruut_lang_fr (setup.py) ... done
Created wheel for gruut_lang_fr: filename=gruut_lang_fr-2.0.2-py3-none-any.whl size=10968767 sha256=3d6a63dba04ad790d69a7222a83ed07bcc9d3ed18e00c33e3834096e74e73bfa
Stored in directory: /root/.cache/pip/wheels/e0/e7/a0/7c416a3eeaa94ca71bf7bcbc6289cced2263d8ba35e82444bb
Successfully built gruut encodec bnnumerizer docopt gruut-ipa gruut_lang_de gruut_lang_en gruut_lang_es gruut_lang_fr
Installing collected packages: sudachipy, jamo, hangul-romanize, gruut_lang_fr, gruut_lang_es, gruut_lang_en, gruut_lang_de, docopt, bnunicodenormalizer, bnnumerizer, bangla, unidecode, sudachidict_core, python-crfsuite, pysbd, pypinyin, nvidia-nvjitlink-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cublas-cu12, num2words, networkx, jsonlines, gruut-ipa, coqpit, anyascii, nvidia-cusparse-cu12, nvidia-cudnn-cu12, g2pkk, dateparser, nvidia-cusolver-cu12, scikit-learn, gruut, trainer, pandas, encodec, TTS
Attempting uninstall: nvidia-nvjitlink-cu12
Found existing installation: nvidia-nvjitlink-cu12 12.9.41
Uninstalling nvidia-nvjitlink-cu12-12.9.41:
Successfully uninstalled nvidia-nvjitlink-cu12-12.9.41
Attempting uninstall: nvidia-curand-cu12
Found existing installation: nvidia-curand-cu12 10.3.10.19
Uninstalling nvidia-curand-cu12-10.3.10.19:
Successfully uninstalled nvidia-curand-cu12-10.3.10.19
Attempting uninstall: nvidia-cufft-cu12
Found existing installation: nvidia-cufft-cu12 11.4.0.6
Uninstalling nvidia-cufft-cu12-11.4.0.6:
Successfully uninstalled nvidia-cufft-cu12-11.4.0.6
Attempting uninstall: nvidia-cublas-cu12
Found existing installation: nvidia-cublas-cu12 12.9.0.13
Uninstalling nvidia-cublas-cu12-12.9.0.13:
Successfully uninstalled nvidia-cublas-cu12-12.9.0.13
Attempting uninstall: networkx
Found existing installation: networkx 3.4.2
Uninstalling networkx-3.4.2:
Successfully uninstalled networkx-3.4.2
Attempting uninstall: nvidia-cusparse-cu12
Found existing installation: nvidia-cusparse-cu12 12.5.9.5
Uninstalling nvidia-cusparse-cu12-12.5.9.5:
Successfully uninstalled nvidia-cusparse-cu12-12.5.9.5
Attempting uninstall: nvidia-cudnn-cu12
Found existing installation: nvidia-cudnn-cu12 9.3.0.75
Uninstalling nvidia-cudnn-cu12-9.3.0.75:
Successfully uninstalled nvidia-cudnn-cu12-9.3.0.75
Attempting uninstall: nvidia-cusolver-cu12
Found existing installation: nvidia-cusolver-cu12 11.7.4.40
Uninstalling nvidia-cusolver-cu12-11.7.4.40:
Successfully uninstalled nvidia-cusolver-cu12-11.7.4.40
Attempting uninstall: scikit-learn
Found existing installation: scikit-learn 1.2.2
Uninstalling scikit-learn-1.2.2:
Successfully uninstalled scikit-learn-1.2.2
Attempting uninstall: pandas
Found existing installation: pandas 2.2.3
Uninstalling pandas-2.2.3:
Successfully uninstalled pandas-2.2.3
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
dask-cudf-cu12 25.2.2 requires pandas<2.2.4dev0,>=2.0, but you have pandas 1.5.3 which is incompatible.
dask-expr 1.1.21 requires pandas>=2, but you have pandas 1.5.3 which is incompatible.
cudf-cu12 25.2.2 requires pandas<2.2.4dev0,>=2.0, but you have pandas 1.5.3 which is incompatible.
datasets 3.6.0 requires fsspec[http]<=2025.3.0,>=2023.1.0, but you have fsspec 2025.3.2 which is incompatible.
woodwork 0.31.0 requires pandas>=2.0.0, but you have pandas 1.5.3 which is incompatible.
featuretools 1.31.0 requires pandas>=2.0.0, but you have pandas 1.5.3 which is incompatible.
visions 0.8.1 requires pandas>=2.0.0, but you have pandas 1.5.3 which is incompatible.
pyldavis 3.4.1 requires pandas>=2.0.0, but you have pandas 1.5.3 which is incompatible.
category-encoders 2.7.0 requires scikit-learn<1.6.0,>=1.0.0, but you have scikit-learn 1.6.1 which is incompatible.
cesium 0.12.4 requires numpy<3.0,>=2.0, but you have numpy 1.26.4 which is incompatible.
google-colab 1.0.0 requires google-auth==2.38.0, but you have google-auth 2.40.1 which is incompatible.
google-colab 1.0.0 requires notebook==6.5.7, but you have notebook 6.5.4 which is incompatible.
google-colab 1.0.0 requires pandas==2.2.2, but you have pandas 1.5.3 which is incompatible.
mizani 0.13.2 requires pandas>=2.2.0, but you have pandas 1.5.3 which is incompatible.
dopamine-rl 4.1.2 requires gymnasium>=1.0.0, but you have gymnasium 0.29.0 which is incompatible.
scikit-image 0.25.2 requires networkx>=3.0, but you have networkx 2.8.8 which is incompatible.
nx-cugraph-cu12 25.2.0 requires networkx>=3.2, but you have networkx 2.8.8 which is incompatible.
bigframes 1.42.0 requires rich<14,>=12.4.4, but you have rich 14.0.0 which is incompatible.
plotnine 0.14.5 requires matplotlib>=3.8.0, but you have matplotlib 3.7.2 which is incompatible.
plotnine 0.14.5 requires pandas>=2.2.0, but you have pandas 1.5.3 which is incompatible.
xarray 2025.1.2 requires pandas>=2.1, but you have pandas 1.5.3 which is incompatible.
pandas-gbq 0.28.0 requires google-api-core<3.0.0dev,>=2.10.2, but you have google-api-core 1.34.1 which is incompatible.
Successfully installed TTS-0.22.0 anyascii-0.3.2 bangla-0.0.5 bnnumerizer-0.0.2 bnunicodenormalizer-0.1.7 coqpit-0.0.17 dateparser-1.1.8 docopt-0.6.2 encodec-0.1.1 g2pkk-0.1.2 gruut-2.2.3 gruut-ipa-0.13.0 gruut_lang_de-2.0.1 gruut_lang_en-2.0.1 gruut_lang_es-2.0.1 gruut_lang_fr-2.0.2 hangul-romanize-0.1.0 jamo-0.4.1 jsonlines-1.2.0 networkx-2.8.8 num2words-0.5.14 nvidia-cublas-cu12-12.4.5.8 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nvjitlink-cu12-12.4.127 pandas-1.5.3 pypinyin-0.54.0 pysbd-0.3.4 python-crfsuite-0.9.11 scikit-learn-1.6.1 sudachidict_core-20250129 sudachipy-0.6.10 trainer-0.0.36 unidecode-1.4.0
Note: you may need to restart the kernel to use updated packages.
!CUDA_VISIBLE_DEVICES="0" python /kaggle/input/datahrbn/MyTTSDataset/train_tts.py \
--config_path /kaggle/input/ttsbng/transformers/default/1/config.json \
--restore_path /kaggle/input/100-th-epoch/vits_4_nov-Sep-23-2025_10+42AM-0000000/checkpoint_877000.pth
| > Found 5089 files in /kaggle/input/datahrbn/MyTTSDataset
> Using model: vits
> Setting up Audio Processor...
| > sample_rate:22050
| > resample:False
| > num_mels:80
| > log_func:np.log10
| > min_level_db:0
| > frame_shift_ms:None
| > frame_length_ms:None
| > ref_level_db:None
| > fft_size:1024
| > power:None
| > preemphasis:0.0
| > griffin_lim_iters:None
| > signal_norm:None
| > symmetric_norm:None
| > mel_fmin:0
| > mel_fmax:None
| > pitch_fmin:None
| > pitch_fmax:None
| > spec_gain:20.0
| > stft_pad_mode:reflect
| > max_norm:1.0
| > clip_norm:True
| > do_trim_silence:False
| > trim_db:60
| > do_sound_norm:False
| > do_amp_to_db_linear:True
| > do_amp_to_db_mel:True
| > do_rms_norm:False
| > db_level:None
| > stats_path:None
| > base:10
| > hop_length:256
| > win_length:1024
fatal: not a git repository (or any parent up to mount point /kaggle)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
fatal: not a git repository (or any parent up to mount point /kaggle)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
> Training Environment:
| > Backend: Torch
| > Mixed precision: True
| > Precision: fp16
| > Current device: 0
| > Num. of GPUs: 1
| > Num. of CPUs: 4
| > Num. of Torch Threads: 2
| > Torch seed: 54321
| > Torch CUDNN: True
| > Torch CUDNN deterministic: False
| > Torch CUDNN benchmark: True
| > Torch TF32 MatMul: False
2025-05-14 10:28:21.375103: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1747218501.597344 133 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1747218501.661933 133 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
> Start Tensorboard: tensorboard --logdir=/kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
/usr/local/lib/python3.11/dist-packages/trainer/trainer.py:552: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
self.scaler = torch.cuda.amp.GradScaler()
> Restoring from checkpoint_877000.pth ...
> Restoring Model...
> Restoring Optimizer...
> Restoring Scaler...
> Model restored from step 877000
/usr/local/lib/python3.11/dist-packages/trainer/trainer.py:561: FutureWarning: `torch.cuda.amp.GradScaler(args...)` is deprecated. Please use `torch.amp.GradScaler('cuda', args...)` instead.
self.scaler = torch.cuda.amp.GradScaler()
> Model has 83050540 parameters
> EPOCH: 0/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> DataLoader initialization
| > Tokenizer:
| > add_blank: True
| > use_eos_bos: False
| > use_phonemes: False
| > Number of instances : 5039
| > Preprocessing samples
| > Max text length: 603
| > Min text length: 16
| > Avg text length: 130.5689620956539
|
| > Max audio length: 1167808.0
| > Min audio length: 97060.0
| > Avg audio length: 424813.2304028577
| > Num. instances discarded samples: 0
| > Batch group size: 0.
> TRAINING (2025-05-14 10:28:49)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
[!] Character '\n' not found in the vocabulary. Discarding it.
/usr/local/lib/python3.11/dist-packages/torch/functional.py:709: UserWarning: stft with return_complex=False is deprecated. In a future pytorch release, stft will return complex tensors for all inputs, and return_complex=False will raise an error.
Note: you can still call torch.view_as_real on the complex output to recover the old return format. (Triggered internally at /pytorch/aten/src/ATen/native/SpectralOps.cpp:873.)
return _VF.stft( # type: ignore[attr-defined]
/usr/local/lib/python3.11/dist-packages/TTS/tts/models/vits.py:1273: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
with autocast(enabled=False): # use float32 for the criterion
/usr/local/lib/python3.11/dist-packages/TTS/tts/models/vits.py:1284: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
with autocast(enabled=False):
/usr/local/lib/python3.11/dist-packages/TTS/tts/models/vits.py:1311: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
with autocast(enabled=False): # use float32 for the criterion
--> TIME: 2025-05-14 10:30:10 -- STEP: 99/630 -- GLOBAL_STEP: 877100
| > loss_disc: 2.541196346282959 (2.583098987136225)
| > loss_disc_real_0: 0.20284852385520935 (0.17028560549622834)
| > loss_disc_real_1: 0.19826216995716095 (0.21420876922631504)
| > loss_disc_real_2: 0.25432053208351135 (0.2280016639316925)
| > loss_disc_real_3: 0.23575444519519806 (0.227563643846849)
| > loss_disc_real_4: 0.24201123416423798 (0.23676217324805982)
| > loss_disc_real_5: 0.2607475221157074 (0.2283143029369489)
| > loss_0: 2.541196346282959 (2.583098987136225)
| > grad_norm_0: tensor(7.8930, device='cuda:0') (tensor(20.8855, device='cuda:0'))
| > loss_gen: 2.324298143386841 (2.231554644276398)
| > loss_kl: 1.5612194538116455 (1.5566532419185446)
| > loss_feat: 6.414757251739502 (7.076604583046653)
| > loss_mel: 16.319232940673828 (15.508287978894783)
| > loss_duration: 1.4498400688171387 (1.4432771591225066)
| > amp_scaler: 256.0 (636.1212121212118)
| > loss_1: 28.06934928894043 (27.81637773610125)
| > grad_norm_1: tensor(159.8710, device='cuda:0') (tensor(248.6020, device='cuda:0'))
| > current_lr_0: 0.0002
| > current_lr_1: 0.0002
| > step_time: 0.6971 (0.7194715509511004)
| > loader_time: 0.0058 (0.0054759112271395615)
--> TIME: 2025-05-14 10:31:24 -- STEP: 199/630 -- GLOBAL_STEP: 877200
| > loss_disc: 2.5696399211883545 (2.59817287670308)
| > loss_disc_real_0: 0.11310849338769913 (0.16996975943221518)
| > loss_disc_real_1: 0.2000749707221985 (0.2144461447120312)
| > loss_disc_real_2: 0.2251717448234558 (0.22797891370315648)
| > loss_disc_real_3: 0.21167348325252533 (0.230459611544657)
| > loss_disc_real_4: 0.23473016917705536 (0.23955846124857513)
| > loss_disc_real_5: 0.24328827857971191 (0.23221386092991086)
| > loss_0: 2.5696399211883545 (2.59817287670308)
| > grad_norm_0: tensor(10.7297, device='cuda:0') (tensor(19.0180, device='cuda:0'))
| > loss_gen: 2.029984712600708 (2.2090387518082433)
| > loss_kl: 1.4565503597259521 (1.5865955754141108)
| > loss_feat: 7.017753601074219 (6.9812930097532035)
| > loss_mel: 14.679983139038086 (15.5458496755092)
| > loss_duration: 1.424647569656372 (1.393087724345414)
| > amp_scaler: 256.0 (445.10552763819067)
| > loss_1: 26.60892105102539 (27.71586473742921)
| > grad_norm_1: tensor(83.8757, device='cuda:0') (tensor(240.1375, device='cuda:0'))
| > current_lr_0: 0.0002
| > current_lr_1: 0.0002
| > step_time: 0.5854 (0.7231272764541395)
| > loader_time: 0.0064 (0.005929011196347338)
--> TIME: 2025-05-14 10:32:42 -- STEP: 299/630 -- GLOBAL_STEP: 877300
| > loss_disc: 2.637537956237793 (2.5965678476569645)
| > loss_disc_real_0: 0.10217836499214172 (0.17167144732232076)
| > loss_disc_real_1: 0.1999306082725525 (0.21346425656291557)
| > loss_disc_real_2: 0.2410740703344345 (0.22852222252649607)
| > loss_disc_real_3: 0.27172544598579407 (0.23054160835551576)
| > loss_disc_real_4: 0.23348262906074524 (0.23922175717194344)
| > loss_disc_real_5: 0.2823101878166199 (0.231475421268007)
| > loss_0: 2.637537956237793 (2.5965678476569645)
| > grad_norm_0: tensor(25.3562, device='cuda:0') (tensor(19.5521, device='cuda:0'))
| > loss_gen: 2.209883213043213 (2.2026778770529702)
| > loss_kl: 1.5382657051086426 (1.5951844162765554)
| > loss_feat: 7.015866756439209 (6.8902633995515465)
| > loss_mel: 15.651371955871582 (15.543730614576052)
| > loss_duration: 1.4375065565109253 (1.3953236756117455)
| > amp_scaler: 256.0 (381.8595317725751)
| > loss_1: 27.852893829345703 (27.627180048454573)
| > grad_norm_1: tensor(141.1728, device='cuda:0') (tensor(248.9879, device='cuda:0'))
| > current_lr_0: 0.0002
| > current_lr_1: 0.0002
| > step_time: 1.0355 (0.7392290284402395)
| > loader_time: 0.0089 (0.00650849549666695)
--> TIME: 2025-05-14 10:34:08 -- STEP: 399/630 -- GLOBAL_STEP: 877400
| > loss_disc: 2.5036776065826416 (2.5935029613045524)
| > loss_disc_real_0: 0.15859703719615936 (0.1726315132433311)
| > loss_disc_real_1: 0.17949408292770386 (0.21400433409034758)
| > loss_disc_real_2: 0.23355287313461304 (0.22863891156843133)
| > loss_disc_real_3: 0.24674323201179504 (0.23046086963854337)
| > loss_disc_real_4: 0.22616897523403168 (0.23901906781328053)
| > loss_disc_real_5: 0.18244747817516327 (0.22836134397893917)
| > loss_0: 2.5036776065826416 (2.5935029613045524)
| > grad_norm_0: tensor(25.0814, device='cuda:0') (tensor(20.7856, device='cuda:0'))
| > loss_gen: 2.049567699432373 (2.208144545555115)
| > loss_kl: 1.5183061361312866 (1.6032853739004684)
| > loss_feat: 6.140530586242676 (6.887340947201379)
| > loss_mel: 15.255861282348633 (15.529142857792982)
| > loss_duration: 1.4309537410736084 (1.398575850596703)
| > amp_scaler: 256.0 (350.31578947368405)
| > loss_1: 26.395219802856445 (27.626489634501908)
| > grad_norm_1: tensor(249.0735, device='cuda:0') (tensor(261.4655, device='cuda:0'))
| > current_lr_0: 0.0002
| > current_lr_1: 0.0002
| > step_time: 0.7836 (0.7656899388870201)
| > loader_time: 0.0096 (0.007098129219877391)
--> TIME: 2025-05-14 10:35:44 -- STEP: 499/630 -- GLOBAL_STEP: 877500
| > loss_disc: 2.5580368041992188 (2.599084942039841)
| > loss_disc_real_0: 0.1362900286912918 (0.17268126902874106)
| > loss_disc_real_1: 0.24070052802562714 (0.21417419260035536)
| > loss_disc_real_2: 0.1872912049293518 (0.22916918389782878)
| > loss_disc_real_3: 0.23501206934452057 (0.23039158309748273)
| > loss_disc_real_4: 0.2016042023897171 (0.23975408635660259)
| > loss_disc_real_5: 0.19868752360343933 (0.23006371099628758)
| > loss_0: 2.5580368041992188 (2.599084942039841)
| > grad_norm_0: tensor(12.5176, device='cuda:0') (tensor(19.3417, device='cuda:0'))
| > loss_gen: 2.0745630264282227 (2.195856654094549)
| > loss_kl: 1.6381635665893555 (1.6032603489373156)
| > loss_feat: 6.355065822601318 (6.812628305507806)
| > loss_mel: 15.931011199951172 (15.53354621841339)
| > loss_duration: 1.517388105392456 (1.4125814886991392)
| > amp_scaler: 256.0 (331.4148296593185)
| > loss_1: 27.516189575195312 (27.557873070359474)
| > grad_norm_1: tensor(128.4508, device='cuda:0') (tensor(236.6487, device='cuda:0'))
| > current_lr_0: 0.0002
| > current_lr_1: 0.0002
| > step_time: 1.1726 (0.8010818595159985)
| > loader_time: 0.0102 (0.0076235172027098634)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_877500.pth
--> TIME: 2025-05-14 10:37:44 -- STEP: 599/630 -- GLOBAL_STEP: 877600
| > loss_disc: 2.654987096786499 (2.5985878584579947)
| > loss_disc_real_0: 0.1970704197883606 (0.1727115317731349)
| > loss_disc_real_1: 0.20512540638446808 (0.21445139936592822)
| > loss_disc_real_2: 0.18022485077381134 (0.22891314740670549)
| > loss_disc_real_3: 0.21067610383033752 (0.2302025156795282)
| > loss_disc_real_4: 0.22382207214832306 (0.24002311320257108)
| > loss_disc_real_5: 0.2397259771823883 (0.2301416313633298)
| > loss_0: 2.654987096786499 (2.5985878584579947)
| > grad_norm_0: tensor(17.7733, device='cuda:0') (tensor(19.4302, device='cuda:0'))
| > loss_gen: 1.9668817520141602 (2.19531105217432)
| > loss_kl: 1.4726840257644653 (1.608320862303592)
| > loss_feat: 5.841393947601318 (6.787265382744437)
| > loss_mel: 15.384966850280762 (15.559310445005389)
| > loss_duration: 1.4878348112106323 (1.4231590524141697)
| > amp_scaler: 256.0 (318.82470784641066)
| > loss_1: 26.153762817382812 (27.573366840216085)
| > grad_norm_1: tensor(304.6707, device='cuda:0') (tensor(238.8102, device='cuda:0'))
| > current_lr_0: 0.0002
| > current_lr_1: 0.0002
| > step_time: 1.4531 (0.8606340391608033)
| > loader_time: 0.0124 (0.008283108821098308)
> DataLoader initialization
| > Tokenizer:
| > add_blank: True
| > use_eos_bos: False
| > use_phonemes: False
| > Number of instances : 50
| > Preprocessing samples
| > Max text length: 227
| > Min text length: 34
| > Avg text length: 119.96
|
| > Max audio length: 747976.0
| > Min audio length: 121756.0
| > Avg audio length: 396798.88
| > Num. instances discarded samples: 0
| > Batch group size: 0.
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
/usr/local/lib/python3.11/dist-packages/TTS/tts/models/vits.py:1455: UserWarning: The use of `x.T` on tensors of dimension other than 2 to reverse their shape is deprecated and it will throw an error in a future release. Consider `x.mT` to transpose batches of matrices or `x.permute(*torch.arange(x.ndim - 1, -1, -1))` to reverse the dimensions of a tensor. (Triggered internally at /pytorch/aten/src/ATen/native/TensorShape.cpp:3725.)
test_figures["{}-alignment".format(idx)] = plot_alignment(alignment.T, output_fig=False)
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005259593327840169 (+0)
| > avg_loss_disc: 2.6548799872398376 (+0)
| > avg_loss_disc_real_0: 0.10644166668256123 (+0)
| > avg_loss_disc_real_1: 0.2484812339146932 (+0)
| > avg_loss_disc_real_2: 0.167192243039608 (+0)
| > avg_loss_disc_real_3: 0.2078298938771089 (+0)
| > avg_loss_disc_real_4: 0.25538210446635884 (+0)
| > avg_loss_disc_real_5: 0.2178861709932486 (+0)
| > avg_loss_0: 2.6548799872398376 (+0)
| > avg_loss_gen: 1.8552529613176982 (+0)
| > avg_loss_kl: 1.760383317867915 (+0)
| > avg_loss_feat: 6.7177348136901855 (+0)
| > avg_loss_mel: 15.871013402938843 (+0)
| > avg_loss_duration: 1.5238793989022572 (+0)
| > avg_loss_1: 27.728264172871906 (+0)
> BEST MODEL : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/best_model_877631.pth
> EPOCH: 1/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 10:38:53)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 10:39:30 -- STEP: 69/630 -- GLOBAL_STEP: 877700
| > loss_disc: 2.5716302394866943 (2.6018410143644903)
| > loss_disc_real_0: 0.266626238822937 (0.17447043944528137)
| > loss_disc_real_1: 0.17372985184192657 (0.2145699342523796)
| > loss_disc_real_2: 0.21889646351337433 (0.22977175617563553)
| > loss_disc_real_3: 0.22407829761505127 (0.22902384400367737)
| > loss_disc_real_4: 0.250437468290329 (0.2420167398193608)
| > loss_disc_real_5: 0.2260865867137909 (0.23255455925844717)
| > loss_0: 2.5716302394866943 (2.6018410143644903)
| > grad_norm_0: tensor(36.9208, device='cuda:0') (tensor(18.8026, device='cuda:0'))
| > loss_gen: 2.1733953952789307 (2.2124019532963843)
| > loss_kl: 1.757939100265503 (1.5921217479567598)
| > loss_feat: 7.15437126159668 (6.988252736520075)
| > loss_mel: 15.670079231262207 (15.51419404624165)
| > loss_duration: 1.4457192420959473 (1.4357048065766043)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.20150375366211 (27.74267525603806)
| > grad_norm_1: tensor(567.2295, device='cuda:0') (tensor(255.3572, device='cuda:0'))
| > current_lr_0: 0.000199975
| > current_lr_1: 0.000199975
| > step_time: 0.5161 (0.5247562864552373)
| > loader_time: 0.0051 (0.0051648685897606)
--> TIME: 2025-05-14 10:40:27 -- STEP: 169/630 -- GLOBAL_STEP: 877800
| > loss_disc: 2.691209077835083 (2.5913256018824833)
| > loss_disc_real_0: 0.2154233455657959 (0.17167555179292635)
| > loss_disc_real_1: 0.21937382221221924 (0.21296556726009888)
| > loss_disc_real_2: 0.21364463865756989 (0.23009426830082955)
| > loss_disc_real_3: 0.20549863576889038 (0.22930673549513844)
| > loss_disc_real_4: 0.24030040204524994 (0.24038844401314413)
| > loss_disc_real_5: 0.30724528431892395 (0.2316025540497176)
| > loss_0: 2.691209077835083 (2.5913256018824833)
| > grad_norm_0: tensor(22.2899, device='cuda:0') (tensor(19.3623, device='cuda:0'))
| > loss_gen: 2.5276482105255127 (2.211769889092304)
| > loss_kl: 1.425126075744629 (1.596593714324681)
| > loss_feat: 7.501079559326172 (6.939584825165879)
| > loss_mel: 15.82955265045166 (15.553203153892381)
| > loss_duration: 1.4860965013504028 (1.3842212899902162)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.76950454711914 (27.68537291126139)
| > grad_norm_1: tensor(457.5830, device='cuda:0') (tensor(253.8017, device='cuda:0'))
| > current_lr_0: 0.000199975
| > current_lr_1: 0.000199975
| > step_time: 0.5882 (0.5419546951203653)
| > loader_time: 0.0064 (0.0057019891118156845)
--> TIME: 2025-05-14 10:41:29 -- STEP: 269/630 -- GLOBAL_STEP: 877900
| > loss_disc: 2.5869736671447754 (2.598857665150582)
| > loss_disc_real_0: 0.2444716840982437 (0.17202929315956988)
| > loss_disc_real_1: 0.20690885186195374 (0.2145472049823924)
| > loss_disc_real_2: 0.23589393496513367 (0.2311623966716036)
| > loss_disc_real_3: 0.19940897822380066 (0.22931945938824722)
| > loss_disc_real_4: 0.20271266996860504 (0.2419478077316816)
| > loss_disc_real_5: 0.23216240108013153 (0.22845399252322526)
| > loss_0: 2.5869736671447754 (2.598857665150582)
| > grad_norm_0: tensor(11.4563, device='cuda:0') (tensor(21.9312, device='cuda:0'))
| > loss_gen: 2.3009955883026123 (2.2136464610862023)
| > loss_kl: 1.4130150079727173 (1.6007059759366915)
| > loss_feat: 6.563141822814941 (6.892141464474476)
| > loss_mel: 15.765031814575195 (15.572424172468788)
| > loss_duration: 1.4731621742248535 (1.3918518909291264)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.515344619750977 (27.670769999904707)
| > grad_norm_1: tensor(91.9019, device='cuda:0') (tensor(290.2534, device='cuda:0'))
| > current_lr_0: 0.000199975
| > current_lr_1: 0.000199975
| > step_time: 0.6135 (0.5686290618655401)
| > loader_time: 0.0072 (0.006298240675802124)
--> TIME: 2025-05-14 10:42:36 -- STEP: 369/630 -- GLOBAL_STEP: 878000
| > loss_disc: 2.654486656188965 (2.6088957780098836)
| > loss_disc_real_0: 0.28468233346939087 (0.17333781478931584)
| > loss_disc_real_1: 0.2235957533121109 (0.21427653265516286)
| > loss_disc_real_2: 0.25052693486213684 (0.23119856804851593)
| > loss_disc_real_3: 0.24912118911743164 (0.2297056522472764)
| > loss_disc_real_4: 0.2608570456504822 (0.242215686414623)
| > loss_disc_real_5: 0.2599897086620331 (0.2316656325083115)
| > loss_0: 2.654486656188965 (2.6088957780098836)
| > grad_norm_0: tensor(9.4669, device='cuda:0') (tensor(19.8528, device='cuda:0'))
| > loss_gen: 2.2195019721984863 (2.192004329143824)
| > loss_kl: 1.581434726715088 (1.599710757170267)
| > loss_feat: 6.473280906677246 (6.84010898259274)
| > loss_mel: 15.222283363342285 (15.551348854209673)
| > loss_duration: 1.4342799186706543 (1.4108323162487206)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.930782318115234 (27.594005259071913)
| > grad_norm_1: tensor(142.0419, device='cuda:0') (tensor(250.1096, device='cuda:0'))
| > current_lr_0: 0.000199975
| > current_lr_1: 0.000199975
| > step_time: 0.6786 (0.5926478768428804)
| > loader_time: 0.0094 (0.006803429869778434)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_878000.pth
--> TIME: 2025-05-14 10:43:54 -- STEP: 469/630 -- GLOBAL_STEP: 878100
| > loss_disc: 2.4152846336364746 (2.6089282279838115)
| > loss_disc_real_0: 0.1606421172618866 (0.1742007955273331)
| > loss_disc_real_1: 0.14918045699596405 (0.21396954281370778)
| > loss_disc_real_2: 0.24584928154945374 (0.2301022190529146)
| > loss_disc_real_3: 0.20289729535579681 (0.22933112272321543)
| > loss_disc_real_4: 0.21950066089630127 (0.24219400249818748)
| > loss_disc_real_5: 0.2431793361902237 (0.23260357118110414)
| > loss_0: 2.4152846336364746 (2.6089282279838115)
| > grad_norm_0: tensor(28.7089, device='cuda:0') (tensor(18.9020, device='cuda:0'))
| > loss_gen: 2.2141740322113037 (2.1811010527458246)
| > loss_kl: 1.612919807434082 (1.6087443546445643)
| > loss_feat: 6.450411319732666 (6.79440152975542)
| > loss_mel: 15.073073387145996 (15.550834822502217)
| > loss_duration: 1.4879441261291504 (1.410957959669231)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.838523864746094 (27.54603975210617)
| > grad_norm_1: tensor(130.6561, device='cuda:0') (tensor(232.4310, device='cuda:0'))
| > current_lr_0: 0.000199975
| > current_lr_1: 0.000199975
| > step_time: 0.7476 (0.6228327425812346)
| > loader_time: 0.0091 (0.007359659748036724)
--> TIME: 2025-05-14 10:45:19 -- STEP: 569/630 -- GLOBAL_STEP: 878200
| > loss_disc: 2.7293074131011963 (2.6087126166204575)
| > loss_disc_real_0: 0.11625935882329941 (0.1748797724216601)
| > loss_disc_real_1: 0.13457779586315155 (0.21401740298958355)
| > loss_disc_real_2: 0.21359945833683014 (0.22968720394613873)
| > loss_disc_real_3: 0.26273319125175476 (0.22961038780547607)
| > loss_disc_real_4: 0.22170795500278473 (0.24141934563803547)
| > loss_disc_real_5: 0.2840225398540497 (0.2321208407464052)
| > loss_0: 2.7293074131011963 (2.6087126166204575)
| > grad_norm_0: tensor(9.5172, device='cuda:0') (tensor(19.6457, device='cuda:0'))
| > loss_gen: 1.8731251955032349 (2.1872111535868424)
| > loss_kl: 1.6253676414489746 (1.6086590386442645)
| > loss_feat: 6.4404988288879395 (6.782436059103699)
| > loss_mel: 15.555947303771973 (15.561029928639819)
| > loss_duration: 1.459883213043213 (1.4217141292635715)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.954822540283203 (27.561050321180087)
| > grad_norm_1: tensor(50.3489, device='cuda:0') (tensor(235.7838, device='cuda:0'))
| > current_lr_0: 0.000199975
| > current_lr_1: 0.000199975
| > step_time: 0.9485 (0.6591813476307734)
| > loader_time: 0.0113 (0.007917424706457368)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005047003428141276 (-0.00021258989969889265)
| > avg_loss_disc: 2.516577184200287 (-0.13830280303955078)
| > avg_loss_disc_real_0: 0.18219377224644026 (+0.07575210556387903)
| > avg_loss_disc_real_1: 0.24094446251789728 (-0.007536771396795927)
| > avg_loss_disc_real_2: 0.21221857517957687 (+0.04502633213996887)
| > avg_loss_disc_real_3: 0.26245762904485065 (+0.05462773516774175)
| > avg_loss_disc_real_4: 0.2553660770257314 (-1.6027440627452982e-05)
| > avg_loss_disc_real_5: 0.2224112239976724 (+0.004525053004423796)
| > avg_loss_0: 2.516577184200287 (-0.13830280303955078)
| > avg_loss_gen: 2.2598869800567627 (+0.40463401873906446)
| > avg_loss_kl: 1.8486497004826863 (+0.08826638261477138)
| > avg_loss_feat: 6.772546807924907 (+0.05481199423472116)
| > avg_loss_mel: 15.197856267293295 (-0.6731571356455479)
| > avg_loss_duration: 1.5359817345937092 (+0.012102335691452026)
| > avg_loss_1: 27.614921410878498 (-0.1133427619934082)
> BEST MODEL : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/best_model_878261.pth
> EPOCH: 2/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 10:46:37)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 10:46:59 -- STEP: 39/630 -- GLOBAL_STEP: 878300
| > loss_disc: 2.594284772872925 (2.586544428116236)
| > loss_disc_real_0: 0.1482287049293518 (0.16994285449767724)
| > loss_disc_real_1: 0.19083476066589355 (0.21200826305609483)
| > loss_disc_real_2: 0.18914195895195007 (0.2302296723310764)
| > loss_disc_real_3: 0.22492742538452148 (0.22242107910987657)
| > loss_disc_real_4: 0.2061195820569992 (0.2418894080015329)
| > loss_disc_real_5: 0.247182697057724 (0.23870841700297135)
| > loss_0: 2.594284772872925 (2.586544428116236)
| > grad_norm_0: tensor(9.3708, device='cuda:0') (tensor(11.9438, device='cuda:0'))
| > loss_gen: 2.1438028812408447 (2.2033885686825485)
| > loss_kl: 1.489154577255249 (1.5699344139832716)
| > loss_feat: 6.02448844909668 (6.989003597161709)
| > loss_mel: 15.3169527053833 (15.708282861954126)
| > loss_duration: 1.449776291847229 (1.441045739711859)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.424175262451172 (27.91165493696164)
| > grad_norm_1: tensor(159.1225, device='cuda:0') (tensor(118.2621, device='cuda:0'))
| > current_lr_0: 0.000199950003125
| > current_lr_1: 0.000199950003125
| > step_time: 0.5331 (0.5253876111446283)
| > loader_time: 0.0056 (0.005050604160015402)
--> TIME: 2025-05-14 10:47:54 -- STEP: 139/630 -- GLOBAL_STEP: 878400
| > loss_disc: 2.7345004081726074 (2.6038832424355935)
| > loss_disc_real_0: 0.1471286416053772 (0.1724347338723622)
| > loss_disc_real_1: 0.18527959287166595 (0.21549338413228233)
| > loss_disc_real_2: 0.23606610298156738 (0.22916221350645846)
| > loss_disc_real_3: 0.23463378846645355 (0.228171865073897)
| > loss_disc_real_4: 0.2931419610977173 (0.2413291336177922)
| > loss_disc_real_5: 0.2556239068508148 (0.23458364177093233)
| > loss_0: 2.7345004081726074 (2.6038832424355935)
| > grad_norm_0: tensor(26.3092, device='cuda:0') (tensor(15.7586, device='cuda:0'))
| > loss_gen: 2.1208229064941406 (2.181420126407268)
| > loss_kl: 1.609281301498413 (1.5875089095650816)
| > loss_feat: 5.962406158447266 (6.8453106365615515)
| > loss_mel: 15.360509872436523 (15.590865265551232)
| > loss_duration: 1.4664416313171387 (1.4173660947264526)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.51946258544922 (27.62247100665415)
| > grad_norm_1: tensor(164.0948, device='cuda:0') (tensor(159.6741, device='cuda:0'))
| > current_lr_0: 0.000199950003125
| > current_lr_1: 0.000199950003125
| > step_time: 0.5405 (0.5316405141953943)
| > loader_time: 0.0065 (0.005648599254141609)
--> TIME: 2025-05-14 10:48:54 -- STEP: 239/630 -- GLOBAL_STEP: 878500
| > loss_disc: 2.5462546348571777 (2.601441624773097)
| > loss_disc_real_0: 0.22696425020694733 (0.17122899987208792)
| > loss_disc_real_1: 0.20538723468780518 (0.2153060934408938)
| > loss_disc_real_2: 0.22592100501060486 (0.23048966175342703)
| > loss_disc_real_3: 0.2715393304824829 (0.22936585327322015)
| > loss_disc_real_4: 0.32779207825660706 (0.24126725509825112)
| > loss_disc_real_5: 0.20342320203781128 (0.23178410230820148)
| > loss_0: 2.5462546348571777 (2.601441624773097)
| > grad_norm_0: tensor(17.8515, device='cuda:0') (tensor(17.4192, device='cuda:0'))
| > loss_gen: 2.3587143421173096 (2.193118925872706)
| > loss_kl: 1.4507226943969727 (1.6037393775943931)
| > loss_feat: 7.547421932220459 (6.838260371315928)
| > loss_mel: 16.229576110839844 (15.617171802281336)
| > loss_duration: 1.4825146198272705 (1.383332011589944)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.068950653076172 (27.63562253529058)
| > grad_norm_1: tensor(403.9136, device='cuda:0') (tensor(213.2641, device='cuda:0'))
| > current_lr_0: 0.000199950003125
| > current_lr_1: 0.000199950003125
| > step_time: 0.6172 (0.5557289871710613)
| > loader_time: 0.0086 (0.00621143744081633)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_878500.pth
--> TIME: 2025-05-14 10:50:02 -- STEP: 339/630 -- GLOBAL_STEP: 878600
| > loss_disc: 2.7622742652893066 (2.596013216142456)
| > loss_disc_real_0: 0.13105957210063934 (0.1711871982236175)
| > loss_disc_real_1: 0.2098546028137207 (0.2152180742021858)
| > loss_disc_real_2: 0.2753576934337616 (0.22970156433132194)
| > loss_disc_real_3: 0.25764045119285583 (0.2291515885816563)
| > loss_disc_real_4: 0.2502897381782532 (0.24023214593573658)
| > loss_disc_real_5: 0.30100783705711365 (0.23060419909370333)
| > loss_0: 2.7622742652893066 (2.596013216142456)
| > grad_norm_0: tensor(27.2328, device='cuda:0') (tensor(20.0995, device='cuda:0'))
| > loss_gen: 2.141814708709717 (2.201016566394705)
| > loss_kl: 1.5223491191864014 (1.6109694606434983)
| > loss_feat: 7.253742218017578 (6.818823969118012)
| > loss_mel: 16.17045021057129 (15.611517917441759)
| > loss_duration: 1.445335865020752 (1.4063756416680893)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.53369140625 (27.648703583573873)
| > grad_norm_1: tensor(64.1222, device='cuda:0') (tensor(242.2310, device='cuda:0'))
| > current_lr_0: 0.000199950003125
| > current_lr_1: 0.000199950003125
| > step_time: 0.6824 (0.5800597456704187)
| > loader_time: 0.0083 (0.006685934235564373)
--> TIME: 2025-05-14 10:51:15 -- STEP: 439/630 -- GLOBAL_STEP: 878700
| > loss_disc: 2.612591505050659 (2.596529955201376)
| > loss_disc_real_0: 0.24249425530433655 (0.17310890212553232)
| > loss_disc_real_1: 0.2695721685886383 (0.21516765589594564)
| > loss_disc_real_2: 0.19366919994354248 (0.2300414754616644)
| > loss_disc_real_3: 0.18695992231369019 (0.22857210661257046)
| > loss_disc_real_4: 0.24130327999591827 (0.23963312417743962)
| > loss_disc_real_5: 0.21658751368522644 (0.23041853675266605)
| > loss_0: 2.612591505050659 (2.596529955201376)
| > grad_norm_0: tensor(17.3850, device='cuda:0') (tensor(20.2332, device='cuda:0'))
| > loss_gen: 2.121614694595337 (2.20207190187754)
| > loss_kl: 1.5973156690597534 (1.609072247643134)
| > loss_feat: 6.621677875518799 (6.808110625977397)
| > loss_mel: 15.515256881713867 (15.59340903427715)
| > loss_duration: 1.4827239513397217 (1.407871325629719)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.338586807250977 (27.620535183604595)
| > grad_norm_1: tensor(197.5541, device='cuda:0') (tensor(243.4702, device='cuda:0'))
| > current_lr_0: 0.000199950003125
| > current_lr_1: 0.000199950003125
| > step_time: 0.723 (0.6092759911183064)
| > loader_time: 0.0089 (0.007229154365209347)
--> TIME: 2025-05-14 10:52:35 -- STEP: 539/630 -- GLOBAL_STEP: 878800
| > loss_disc: 2.460418701171875 (2.5962980983429795)
| > loss_disc_real_0: 0.15908318758010864 (0.17327869817586908)
| > loss_disc_real_1: 0.14025741815567017 (0.21495387455749154)
| > loss_disc_real_2: 0.16837047040462494 (0.22976408846303129)
| > loss_disc_real_3: 0.20524826645851135 (0.22895524602431755)
| > loss_disc_real_4: 0.2781110107898712 (0.23936074250593695)
| > loss_disc_real_5: 0.2567402124404907 (0.22998483965591512)
| > loss_0: 2.460418701171875 (2.5962980983429795)
| > grad_norm_0: tensor(20.0027, device='cuda:0') (tensor(20.8105, device='cuda:0'))
| > loss_gen: 2.18044376373291 (2.199557998627148)
| > loss_kl: 1.5742366313934326 (1.6045403404226994)
| > loss_feat: 6.917572975158691 (6.778249921073278)
| > loss_mel: 15.915013313293457 (15.574152008721912)
| > loss_duration: 1.4605507850646973 (1.418591065176785)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.047815322875977 (27.575091377923577)
| > grad_norm_1: tensor(190.2670, device='cuda:0') (tensor(248.1790, device='cuda:0'))
| > current_lr_0: 0.000199950003125
| > current_lr_1: 0.000199950003125
| > step_time: 0.8792 (0.6430254752206884)
| > loader_time: 0.0102 (0.00779113079488609)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005066076914469401 (+1.9073486328125e-05)
| > avg_loss_disc: 2.5726703802744546 (+0.05609319607416774)
| > avg_loss_disc_real_0: 0.1623471857359012 (-0.019846586510539055)
| > avg_loss_disc_real_1: 0.22351860255002975 (-0.017425859967867524)
| > avg_loss_disc_real_2: 0.24199815839529037 (+0.0297795832157135)
| > avg_loss_disc_real_3: 0.23264178012808165 (-0.029815848916769)
| > avg_loss_disc_real_4: 0.23681807021299997 (-0.018548006812731416)
| > avg_loss_disc_real_5: 0.2141428099324306 (-0.008268414065241814)
| > avg_loss_0: 2.5726703802744546 (+0.05609319607416774)
| > avg_loss_gen: 2.1148403783639274 (-0.14504660169283534)
| > avg_loss_kl: 1.6059687187274296 (-0.24268098175525665)
| > avg_loss_feat: 6.924666047096252 (+0.15211923917134573)
| > avg_loss_mel: 15.65458631515503 (+0.45673004786173443)
| > avg_loss_duration: 1.5306832293669383 (-0.005298505226770889)
| > avg_loss_1: 27.830745061238606 (+0.21582365036010742)
> EPOCH: 3/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 10:54:19)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 10:54:25 -- STEP: 9/630 -- GLOBAL_STEP: 878900
| > loss_disc: 2.691882371902466 (2.5710602866278753)
| > loss_disc_real_0: 0.1965857744216919 (0.18109815236594942)
| > loss_disc_real_1: 0.16926559805870056 (0.21206127769417232)
| > loss_disc_real_2: 0.22137288749217987 (0.22126242849561903)
| > loss_disc_real_3: 0.2887527346611023 (0.22513787779543135)
| > loss_disc_real_4: 0.2552274465560913 (0.2413397961192661)
| > loss_disc_real_5: 0.3239494264125824 (0.25236354106002384)
| > loss_0: 2.691882371902466 (2.5710602866278753)
| > grad_norm_0: tensor(15.4017, device='cuda:0') (tensor(15.0395, device='cuda:0'))
| > loss_gen: 2.3325726985931396 (2.2880855401357016)
| > loss_kl: 1.673779010772705 (1.5221229394276936)
| > loss_feat: 6.5987396240234375 (7.210574362013075)
| > loss_mel: 15.292482376098633 (15.857935587565104)
| > loss_duration: 1.44130277633667 (1.419380995962355)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.338876724243164 (28.298099729749893)
| > grad_norm_1: tensor(239.8386, device='cuda:0') (tensor(204.1157, device='cuda:0'))
| > current_lr_0: 0.00019992500937460937
| > current_lr_1: 0.00019992500937460937
| > step_time: 0.5496 (0.5179816087086996)
| > loader_time: 0.005 (0.004833141962687175)
--> TIME: 2025-05-14 10:55:20 -- STEP: 109/630 -- GLOBAL_STEP: 879000
| > loss_disc: 2.6621153354644775 (2.5916379460501004)
| > loss_disc_real_0: 0.10830757021903992 (0.17245900309687362)
| > loss_disc_real_1: 0.24678122997283936 (0.2140906881028359)
| > loss_disc_real_2: 0.21753065288066864 (0.2281228190441744)
| > loss_disc_real_3: 0.24514862895011902 (0.22762850132010398)
| > loss_disc_real_4: 0.24550969898700714 (0.24134611878373208)
| > loss_disc_real_5: 0.2463897466659546 (0.23327837036837132)
| > loss_0: 2.6621153354644775 (2.5916379460501004)
| > grad_norm_0: tensor(9.0378, device='cuda:0') (tensor(17.4595, device='cuda:0'))
| > loss_gen: 2.0497989654541016 (2.227746264650188)
| > loss_kl: 1.4466240406036377 (1.5759173609794828)
| > loss_feat: 5.856705665588379 (7.065950896761833)
| > loss_mel: 15.66637897491455 (15.64434955316946)
| > loss_duration: 1.4921653270721436 (1.4036464472429468)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.51167106628418 (27.9176104309362)
| > grad_norm_1: tensor(97.9731, device='cuda:0') (tensor(229.4586, device='cuda:0'))
| > current_lr_0: 0.00019992500937460937
| > current_lr_1: 0.00019992500937460937
| > step_time: 0.5397 (0.5392682092999103)
| > loader_time: 0.0057 (0.005640920149076969)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_879000.pth
--> TIME: 2025-05-14 10:56:22 -- STEP: 209/630 -- GLOBAL_STEP: 879100
| > loss_disc: 2.5255959033966064 (2.59230237144032)
| > loss_disc_real_0: 0.17572122812271118 (0.1745977365371713)
| > loss_disc_real_1: 0.21364179253578186 (0.2135061297975659)
| > loss_disc_real_2: 0.268145352602005 (0.22774300677924636)
| > loss_disc_real_3: 0.2223956286907196 (0.22805566508233832)
| > loss_disc_real_4: 0.2302558273077011 (0.2390831721741617)
| > loss_disc_real_5: 0.17090164124965668 (0.2318096777611372)
| > loss_0: 2.5255959033966064 (2.59230237144032)
| > grad_norm_0: tensor(12.0317, device='cuda:0') (tensor(19.1641, device='cuda:0'))
| > loss_gen: 2.1467370986938477 (2.2202950288234184)
| > loss_kl: 1.4465632438659668 (1.5940066929639247)
| > loss_feat: 7.769976615905762 (6.98724169708325)
| > loss_mel: 15.587423324584961 (15.608780053243683)
| > loss_duration: 1.466074824333191 (1.3690647251868358)
| > amp_scaler: 256.0 (263.3492822966505)
| > loss_1: 28.416772842407227 (27.779388135700135)
| > grad_norm_1: tensor(393.7550, device='cuda:0') (tensor(264.7254, device='cuda:0'))
| > current_lr_0: 0.00019992500937460937
| > current_lr_1: 0.00019992500937460937
| > step_time: 0.6121 (0.5592910981064207)
| > loader_time: 0.0077 (0.006149866934598348)
--> TIME: 2025-05-14 10:57:26 -- STEP: 309/630 -- GLOBAL_STEP: 879200
| > loss_disc: 2.685307741165161 (2.587703429379508)
| > loss_disc_real_0: 0.1945084035396576 (0.17269797736483483)
| > loss_disc_real_1: 0.2665232717990875 (0.21245254325442334)
| > loss_disc_real_2: 0.23624780774116516 (0.22771560383846073)
| > loss_disc_real_3: 0.2069026082754135 (0.22916689172724689)
| > loss_disc_real_4: 0.2261110544204712 (0.23800897820096187)
| > loss_disc_real_5: 0.24732759594917297 (0.2321085021333787)
| > loss_0: 2.685307741165161 (2.587703429379508)
| > grad_norm_0: tensor(20.4772, device='cuda:0') (tensor(20.4613, device='cuda:0'))
| > loss_gen: 2.132977247238159 (2.223204038675552)
| > loss_kl: 1.6356767416000366 (1.6079093229423453)
| > loss_feat: 7.210240364074707 (6.93191922906919)
| > loss_mel: 15.793675422668457 (15.559798894962446)
| > loss_duration: 1.4170339107513428 (1.398913191745967)
| > amp_scaler: 256.0 (260.9708737864076)
| > loss_1: 28.18960189819336 (27.721744697842396)
| > grad_norm_1: tensor(241.2140, device='cuda:0') (tensor(262.9482, device='cuda:0'))
| > current_lr_0: 0.00019992500937460937
| > current_lr_1: 0.00019992500937460937
| > step_time: 0.6463 (0.5807300694166264)
| > loader_time: 0.008 (0.006730632102990999)
--> TIME: 2025-05-14 10:58:38 -- STEP: 409/630 -- GLOBAL_STEP: 879300
| > loss_disc: 2.5887808799743652 (2.5855845314949235)
| > loss_disc_real_0: 0.12376617640256882 (0.17245479940930913)
| > loss_disc_real_1: 0.17423656582832336 (0.21260008713216832)
| > loss_disc_real_2: 0.20216183364391327 (0.22817861090225228)
| > loss_disc_real_3: 0.20304250717163086 (0.22829201001409796)
| > loss_disc_real_4: 0.25699907541275024 (0.2383169321602889)
| > loss_disc_real_5: 0.2384192943572998 (0.2318165319400195)
| > loss_0: 2.5887808799743652 (2.5855845314949235)
| > grad_norm_0: tensor(15.9234, device='cuda:0') (tensor(19.9091, device='cuda:0'))
| > loss_gen: 2.102752685546875 (2.2204959990051423)
| > loss_kl: 1.7298544645309448 (1.609622203924837)
| > loss_feat: 6.083014488220215 (6.892230879123754)
| > loss_mel: 14.808375358581543 (15.554821219595837)
| > loss_duration: 1.481697916984558 (1.401087482867437)
| > amp_scaler: 256.0 (259.75550122249393)
| > loss_1: 26.2056941986084 (27.678257757993666)
| > grad_norm_1: tensor(286.7720, device='cuda:0') (tensor(254.2993, device='cuda:0'))
| > current_lr_0: 0.00019992500937460937
| > current_lr_1: 0.00019992500937460937
| > step_time: 0.7147 (0.6095271600196301)
| > loader_time: 0.0102 (0.00729046649046807)
--> TIME: 2025-05-14 10:59:56 -- STEP: 509/630 -- GLOBAL_STEP: 879400
| > loss_disc: 2.7464351654052734 (2.585955462427645)
| > loss_disc_real_0: 0.24131599068641663 (0.17203949566030322)
| > loss_disc_real_1: 0.2221570909023285 (0.21266229469731657)
| > loss_disc_real_2: 0.18185929954051971 (0.22785234503989604)
| > loss_disc_real_3: 0.2268015295267105 (0.2288624367627273)
| > loss_disc_real_4: 0.26153188943862915 (0.23941052085875528)
| > loss_disc_real_5: 0.27522769570350647 (0.2316060519405807)
| > loss_0: 2.7464351654052734 (2.585955462427645)
| > grad_norm_0: tensor(9.9941, device='cuda:0') (tensor(20.1394, device='cuda:0'))
| > loss_gen: 2.031771659851074 (2.2230148809597896)
| > loss_kl: 1.82265043258667 (1.6108444516925777)
| > loss_feat: 6.270338535308838 (6.876849026483263)
| > loss_mel: 16.093852996826172 (15.566912802825508)
| > loss_duration: 1.4505817890167236 (1.4138898182008945)
| > amp_scaler: 256.0 (259.0176817288803)
| > loss_1: 27.6691951751709 (27.691511000537684)
| > grad_norm_1: tensor(164.4534, device='cuda:0') (tensor(252.6479, device='cuda:0'))
| > current_lr_0: 0.00019992500937460937
| > current_lr_1: 0.00019992500937460937
| > step_time: 0.8817 (0.6417664844535426)
| > loader_time: 0.0118 (0.007843359045991729)
--> TIME: 2025-05-14 11:01:30 -- STEP: 609/630 -- GLOBAL_STEP: 879500
| > loss_disc: 2.735424041748047 (2.5869013123911593)
| > loss_disc_real_0: 0.18937300145626068 (0.17309361019696312)
| > loss_disc_real_1: 0.26651501655578613 (0.21204927188079734)
| > loss_disc_real_2: 0.2647610604763031 (0.2276798370974796)
| > loss_disc_real_3: 0.28660067915916443 (0.22914570070839868)
| > loss_disc_real_4: 0.23063921928405762 (0.23995564532984653)
| > loss_disc_real_5: 0.20572338998317719 (0.23177557846008268)
| > loss_0: 2.735424041748047 (2.5869013123911593)
| > grad_norm_0: tensor(9.5415, device='cuda:0') (tensor(19.4117, device='cuda:0'))
| > loss_gen: 2.101592779159546 (2.2193995763124152)
| > loss_kl: 1.4222073554992676 (1.614908765689493)
| > loss_feat: 6.939339637756348 (6.850958444410554)
| > loss_mel: 15.856945037841797 (15.550884683731153)
| > loss_duration: 1.4815211296081543 (1.4235840305710459)
| > amp_scaler: 256.0 (258.52216748768484)
| > loss_1: 27.801607131958008 (27.65973552146373)
| > grad_norm_1: tensor(146.7632, device='cuda:0') (tensor(241.3360, device='cuda:0'))
| > current_lr_0: 0.00019992500937460937
| > current_lr_1: 0.00019992500937460937
| > step_time: 1.0348 (0.6873801795915627)
| > loader_time: 0.0125 (0.008415743635205801)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_879500.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005137443542480469 (+7.136662801106742e-05)
| > avg_loss_disc: 2.642359515031179 (+0.06968913475672434)
| > avg_loss_disc_real_0: 0.21716844538847604 (+0.05482125965257484)
| > avg_loss_disc_real_1: 0.23763051629066467 (+0.014111913740634918)
| > avg_loss_disc_real_2: 0.23404837772250175 (-0.00794978067278862)
| > avg_loss_disc_real_3: 0.26705170919497806 (+0.03440992906689641)
| > avg_loss_disc_real_4: 0.24624175081650415 (+0.009423680603504181)
| > avg_loss_disc_real_5: 0.24248638624946275 (+0.02834357631703216)
| > avg_loss_0: 2.642359515031179 (+0.06968913475672434)
| > avg_loss_gen: 2.183242936929067 (+0.06840255856513977)
| > avg_loss_kl: 1.731288770834605 (+0.12532005210717534)
| > avg_loss_feat: 6.888766527175903 (-0.03589951992034912)
| > avg_loss_mel: 15.492371956507364 (-0.16221435864766498)
| > avg_loss_duration: 1.5266241828600566 (-0.004059046506881714)
| > avg_loss_1: 27.82229455312093 (-0.008450508117675781)
> EPOCH: 4/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:02:08)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:02:51 -- STEP: 79/630 -- GLOBAL_STEP: 879600
| > loss_disc: 2.35213041305542 (2.5677605882475647)
| > loss_disc_real_0: 0.14960011839866638 (0.17090774138894266)
| > loss_disc_real_1: 0.18732726573944092 (0.2096428401485274)
| > loss_disc_real_2: 0.24082742631435394 (0.2279833425072175)
| > loss_disc_real_3: 0.2373432070016861 (0.22918872271157517)
| > loss_disc_real_4: 0.23043963313102722 (0.2383376744729054)
| > loss_disc_real_5: 0.21791738271713257 (0.22857610504083994)
| > loss_0: 2.35213041305542 (2.5677605882475647)
| > grad_norm_0: tensor(22.8094, device='cuda:0') (tensor(23.3726, device='cuda:0'))
| > loss_gen: 2.4357922077178955 (2.2572432650795466)
| > loss_kl: 1.699660301208496 (1.5724403858184814)
| > loss_feat: 8.564120292663574 (7.194968314110478)
| > loss_mel: 17.175325393676758 (15.67936344388165)
| > loss_duration: 1.4587764739990234 (1.4418917411490333)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 31.333675384521484 (28.145907100242905)
| > grad_norm_1: tensor(368.9142, device='cuda:0') (tensor(302.7877, device='cuda:0'))
| > current_lr_0: 0.00019990001874843754
| > current_lr_1: 0.00019990001874843754
| > step_time: 0.5289 (0.5242257661457302)
| > loader_time: 0.0055 (0.0053233617468725295)
--> TIME: 2025-05-14 11:03:49 -- STEP: 179/630 -- GLOBAL_STEP: 879700
| > loss_disc: 2.4899797439575195 (2.5747717718838303)
| > loss_disc_real_0: 0.20464372634887695 (0.17128000142021557)
| > loss_disc_real_1: 0.1977246105670929 (0.21035598667973246)
| > loss_disc_real_2: 0.23560872673988342 (0.22776121034302524)
| > loss_disc_real_3: 0.2488357573747635 (0.2295432064952797)
| > loss_disc_real_4: 0.22222687304019928 (0.23895289511653964)
| > loss_disc_real_5: 0.21682238578796387 (0.23114071569962208)
| > loss_0: 2.4899797439575195 (2.5747717718838303)
| > grad_norm_0: tensor(8.6254, device='cuda:0') (tensor(19.0266, device='cuda:0'))
| > loss_gen: 2.227363109588623 (2.2334564058474293)
| > loss_kl: 1.4439083337783813 (1.6068144976759755)
| > loss_feat: 6.587099552154541 (7.072572196662093)
| > loss_mel: 15.18795394897461 (15.546501324829443)
| > loss_duration: 1.4467613697052002 (1.3891119457489958)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.89308738708496 (27.848456292179048)
| > grad_norm_1: tensor(71.7175, device='cuda:0') (tensor(246.6274, device='cuda:0'))
| > current_lr_0: 0.00019990001874843754
| > current_lr_1: 0.00019990001874843754
| > step_time: 0.589 (0.5474861533948164)
| > loader_time: 0.0074 (0.005851501859100177)
--> TIME: 2025-05-14 11:04:52 -- STEP: 279/630 -- GLOBAL_STEP: 879800
| > loss_disc: 2.5523171424865723 (2.576867146304004)
| > loss_disc_real_0: 0.1582830250263214 (0.1712374511478623)
| > loss_disc_real_1: 0.19264426827430725 (0.21097633378800526)
| > loss_disc_real_2: 0.20450736582279205 (0.2288037274153002)
| > loss_disc_real_3: 0.23362277448177338 (0.23014004256135673)
| > loss_disc_real_4: 0.23404675722122192 (0.24030181840329187)
| > loss_disc_real_5: 0.25970906019210815 (0.23064244840307474)
| > loss_0: 2.5523171424865723 (2.576867146304004)
| > grad_norm_0: tensor(6.3666, device='cuda:0') (tensor(18.9127, device='cuda:0'))
| > loss_gen: 2.1249921321868896 (2.229524478690169)
| > loss_kl: 1.675625205039978 (1.6222634665854943)
| > loss_feat: 6.1677021980285645 (6.995072768153255)
| > loss_mel: 14.890629768371582 (15.565337341746122)
| > loss_duration: 1.5025436878204346 (1.3940790870283666)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.361494064331055 (27.806277093921512)
| > grad_norm_1: tensor(70.8742, device='cuda:0') (tensor(242.9156, device='cuda:0'))
| > current_lr_0: 0.00019990001874843754
| > current_lr_1: 0.00019990001874843754
| > step_time: 0.6478 (0.5749538748067767)
| > loader_time: 0.0075 (0.006415768763497742)
--> TIME: 2025-05-14 11:06:01 -- STEP: 379/630 -- GLOBAL_STEP: 879900
| > loss_disc: 2.390655040740967 (2.5809940165768825)
| > loss_disc_real_0: 0.2548055052757263 (0.17247738343194183)
| > loss_disc_real_1: 0.15104927122592926 (0.21169185219701173)
| > loss_disc_real_2: 0.18083569407463074 (0.22947921338528002)
| > loss_disc_real_3: 0.21433882415294647 (0.2302856010465949)
| > loss_disc_real_4: 0.21254436671733856 (0.24004440304471825)
| > loss_disc_real_5: 0.22224779427051544 (0.22845780692188594)
| > loss_0: 2.390655040740967 (2.5809940165768825)
| > grad_norm_0: tensor(41.4302, device='cuda:0') (tensor(20.1861, device='cuda:0'))
| > loss_gen: 2.48391056060791 (2.2324137753735718)
| > loss_kl: 1.6714777946472168 (1.626991783408817)
| > loss_feat: 8.622580528259277 (6.962740003590848)
| > loss_mel: 16.055448532104492 (15.602939849793124)
| > loss_duration: 1.4840173721313477 (1.4114520137731508)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 30.317432403564453 (27.836537363661314)
| > grad_norm_1: tensor(694.2928, device='cuda:0') (tensor(254.4376, device='cuda:0'))
| > current_lr_0: 0.00019990001874843754
| > current_lr_1: 0.00019990001874843754
| > step_time: 0.694 (0.6018294728211181)
| > loader_time: 0.0083 (0.006988478210167397)
--> TIME: 2025-05-14 11:07:19 -- STEP: 479/630 -- GLOBAL_STEP: 880000
| > loss_disc: 2.571549892425537 (2.5889519365943796)
| > loss_disc_real_0: 0.20567536354064941 (0.1731637505063932)
| > loss_disc_real_1: 0.18822085857391357 (0.21332749414854607)
| > loss_disc_real_2: 0.2331099808216095 (0.22976529679119215)
| > loss_disc_real_3: 0.24648365378379822 (0.23053701943669289)
| > loss_disc_real_4: 0.2544920742511749 (0.23977678665786298)
| > loss_disc_real_5: 0.22963400185108185 (0.22996830439393356)
| > loss_0: 2.571549892425537 (2.5889519365943796)
| > grad_norm_0: tensor(7.0889, device='cuda:0') (tensor(19.3145, device='cuda:0'))
| > loss_gen: 2.1419529914855957 (2.2155760451995743)
| > loss_kl: 1.7310141324996948 (1.6257271726843212)
| > loss_feat: 6.424048900604248 (6.890229405341417)
| > loss_mel: 14.890236854553223 (15.595760323558322)
| > loss_duration: 1.4692381620407104 (1.411066096112723)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.656490325927734 (27.738358993371)
| > grad_norm_1: tensor(58.4245, device='cuda:0') (tensor(236.6571, device='cuda:0'))
| > current_lr_0: 0.00019990001874843754
| > current_lr_1: 0.00019990001874843754
| > step_time: 0.7928 (0.6343643695178266)
| > loader_time: 0.0092 (0.007531319381299748)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_880000.pth
--> TIME: 2025-05-14 11:08:50 -- STEP: 579/630 -- GLOBAL_STEP: 880100
| > loss_disc: 2.651272773742676 (2.5869667945954054)
| > loss_disc_real_0: 0.14091095328330994 (0.17374882646329676)
| > loss_disc_real_1: 0.1739829033613205 (0.2131095154786769)
| > loss_disc_real_2: 0.21706551313400269 (0.22901497843043175)
| > loss_disc_real_3: 0.2544777989387512 (0.23037380996660453)
| > loss_disc_real_4: 0.2747708261013031 (0.23965814496054344)
| > loss_disc_real_5: 0.32798558473587036 (0.2279992689457376)
| > loss_0: 2.651272773742676 (2.5869667945954054)
| > grad_norm_0: tensor(54.1990, device='cuda:0') (tensor(20.0509, device='cuda:0'))
| > loss_gen: 2.398569107055664 (2.220596868963027)
| > loss_kl: 1.8298381567001343 (1.626900415964077)
| > loss_feat: 5.993337631225586 (6.88293006465431)
| > loss_mel: 15.421035766601562 (15.584027016924658)
| > loss_duration: 1.504345417022705 (1.4214466507570735)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.147125244140625 (27.735900961261553)
| > grad_norm_1: tensor(294.5937, device='cuda:0') (tensor(243.5549, device='cuda:0'))
| > current_lr_0: 0.00019990001874843754
| > current_lr_1: 0.00019990001874843754
| > step_time: 0.9024 (0.6745736706030395)
| > loader_time: 0.0114 (0.008107296955194292)
> EVALUATION
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.0049570004145304365 (-0.00018044312795003226)
| > avg_loss_disc: 2.6960413455963135 (+0.053681830565134536)
| > avg_loss_disc_real_0: 0.16217241063714027 (-0.05499603475133577)
| > avg_loss_disc_real_1: 0.19486541797717413 (-0.04276509831349054)
| > avg_loss_disc_real_2: 0.21546016881863275 (-0.018588208903869002)
| > avg_loss_disc_real_3: 0.24840495735406876 (-0.018646751840909304)
| > avg_loss_disc_real_4: 0.24688235546151796 (+0.0006406046450138092)
| > avg_loss_disc_real_5: 0.2514403189222018 (+0.008953932672739057)
| > avg_loss_0: 2.6960413455963135 (+0.053681830565134536)
| > avg_loss_gen: 1.8999577263991039 (-0.28328521052996325)
| > avg_loss_kl: 1.6756764749685924 (-0.05561229586601257)
| > avg_loss_feat: 6.405630389849345 (-0.48313613732655813)
| > avg_loss_mel: 15.388654947280884 (-0.10371700922648053)
| > avg_loss_duration: 1.5237827897071838 (-0.0028413931528727954)
| > avg_loss_1: 26.89370314280192 (-0.928591410319008)
> BEST MODEL : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/best_model_880151.pth
> EPOCH: 5/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:09:58)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:10:25 -- STEP: 49/630 -- GLOBAL_STEP: 880200
| > loss_disc: 2.5808541774749756 (2.613171879126101)
| > loss_disc_real_0: 0.18739217519760132 (0.17604328752780452)
| > loss_disc_real_1: 0.17364977300167084 (0.21309592863734889)
| > loss_disc_real_2: 0.2153693586587906 (0.22729782121522085)
| > loss_disc_real_3: 0.2582364082336426 (0.2325771861538595)
| > loss_disc_real_4: 0.2648983597755432 (0.24015130923718822)
| > loss_disc_real_5: 0.26447686553001404 (0.24432858277340325)
| > loss_0: 2.5808541774749756 (2.613171879126101)
| > grad_norm_0: tensor(18.8809, device='cuda:0') (tensor(18.7295, device='cuda:0'))
| > loss_gen: 2.216815233230591 (2.16615781978685)
| > loss_kl: 1.6305887699127197 (1.5532280620263548)
| > loss_feat: 5.958404064178467 (6.8484673208119915)
| > loss_mel: 15.162304878234863 (15.524155811387665)
| > loss_duration: 1.4578380584716797 (1.43496754218121)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.42595100402832 (27.526976799478337)
| > grad_norm_1: tensor(225.8958, device='cuda:0') (tensor(214.2343, device='cuda:0'))
| > current_lr_0: 0.00019987503124609398
| > current_lr_1: 0.00019987503124609398
| > step_time: 0.561 (0.5190563688472826)
| > loader_time: 0.0058 (0.005198794968274175)
--> TIME: 2025-05-14 11:11:22 -- STEP: 149/630 -- GLOBAL_STEP: 880300
| > loss_disc: 2.444486618041992 (2.6206154487277042)
| > loss_disc_real_0: 0.1568424552679062 (0.17546374580804136)
| > loss_disc_real_1: 0.20570430159568787 (0.21426035788835296)
| > loss_disc_real_2: 0.1823878288269043 (0.22978577687836332)
| > loss_disc_real_3: 0.18653647601604462 (0.2315529327864615)
| > loss_disc_real_4: 0.18839657306671143 (0.24138618875669954)
| > loss_disc_real_5: 0.2256668657064438 (0.2381875749002367)
| > loss_0: 2.444486618041992 (2.6206154487277042)
| > grad_norm_0: tensor(7.4330, device='cuda:0') (tensor(13.5805, device='cuda:0'))
| > loss_gen: 2.0472655296325684 (2.137942346950506)
| > loss_kl: 1.8230255842208862 (1.605353257000046)
| > loss_feat: 6.786844730377197 (6.721224301613417)
| > loss_mel: 14.89522647857666 (15.530856894166678)
| > loss_duration: 1.4247243404388428 (1.3776125907897947)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.977087020874023 (27.37298948812805)
| > grad_norm_1: tensor(140.9022, device='cuda:0') (tensor(255.5859, device='cuda:0'))
| > current_lr_0: 0.00019987503124609398
| > current_lr_1: 0.00019987503124609398
| > step_time: 0.5642 (0.5430100828209179)
| > loader_time: 0.0066 (0.00568958256868708)
--> TIME: 2025-05-14 11:12:22 -- STEP: 249/630 -- GLOBAL_STEP: 880400
| > loss_disc: 2.6024587154388428 (2.621635857356121)
| > loss_disc_real_0: 0.13824395835399628 (0.17549544794253077)
| > loss_disc_real_1: 0.20258617401123047 (0.214152647459124)
| > loss_disc_real_2: 0.17793364822864532 (0.23056271708155252)
| > loss_disc_real_3: 0.1813187450170517 (0.23192366311349064)
| > loss_disc_real_4: 0.21314415335655212 (0.2403742038461578)
| > loss_disc_real_5: 0.18180517852306366 (0.2380825970546309)
| > loss_0: 2.6024587154388428 (2.621635857356121)
| > grad_norm_0: tensor(10.8255, device='cuda:0') (tensor(12.6577, device='cuda:0'))
| > loss_gen: 2.0475285053253174 (2.1409421876731183)
| > loss_kl: 1.517427682876587 (1.6175157904146187)
| > loss_feat: 6.564358711242676 (6.7188565702323455)
| > loss_mel: 15.628636360168457 (15.4988029817022)
| > loss_duration: 1.4119194746017456 (1.3861018658641822)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.169870376586914 (27.362219454294227)
| > grad_norm_1: tensor(201.9195, device='cuda:0') (tensor(198.1391, device='cuda:0'))
| > current_lr_0: 0.00019987503124609398
| > current_lr_1: 0.00019987503124609398
| > step_time: 0.6009 (0.5628306252889367)
| > loader_time: 0.0068 (0.0062084676750213735)
--> TIME: 2025-05-14 11:13:27 -- STEP: 349/630 -- GLOBAL_STEP: 880500
| > loss_disc: 2.654087781906128 (2.6246847156808832)
| > loss_disc_real_0: 0.10852912068367004 (0.17596457390525624)
| > loss_disc_real_1: 0.1974671632051468 (0.2148624844528884)
| > loss_disc_real_2: 0.22172674536705017 (0.2315712514357444)
| > loss_disc_real_3: 0.24356280267238617 (0.23138519792809528)
| > loss_disc_real_4: 0.2176276445388794 (0.240990517346087)
| > loss_disc_real_5: 0.24863599240779877 (0.23703978814846466)
| > loss_0: 2.654087781906128 (2.6246847156808832)
| > grad_norm_0: tensor(12.9469, device='cuda:0') (tensor(15.0399, device='cuda:0'))
| > loss_gen: 1.9666544198989868 (2.1448178287905053)
| > loss_kl: 1.7092487812042236 (1.6201342484329355)
| > loss_feat: 6.085273265838623 (6.6502019655397095)
| > loss_mel: 14.914270401000977 (15.47913688779902)
| > loss_duration: 1.418210744857788 (1.408752052012008)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.093658447265625 (27.303043026637212)
| > grad_norm_1: tensor(50.5605, device='cuda:0') (tensor(207.9326, device='cuda:0'))
| > current_lr_0: 0.00019987503124609398
| > current_lr_1: 0.00019987503124609398
| > step_time: 0.6521 (0.5839739979850531)
| > loader_time: 0.0091 (0.006759795213497127)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_880500.pth
--> TIME: 2025-05-14 11:14:43 -- STEP: 449/630 -- GLOBAL_STEP: 880600
| > loss_disc: 2.5423033237457275 (2.621328880632903)
| > loss_disc_real_0: 0.19832423329353333 (0.17641149862837419)
| > loss_disc_real_1: 0.2713968753814697 (0.2147305731750809)
| > loss_disc_real_2: 0.19762085378170013 (0.2307281308290953)
| > loss_disc_real_3: 0.1925215870141983 (0.23089056576546158)
| > loss_disc_real_4: 0.23688653111457825 (0.24061600601752775)
| > loss_disc_real_5: 0.22343724966049194 (0.2362732444547598)
| > loss_0: 2.5423033237457275 (2.621328880632903)
| > grad_norm_0: tensor(12.7709, device='cuda:0') (tensor(15.3498, device='cuda:0'))
| > loss_gen: 2.096867799758911 (2.1456917476547837)
| > loss_kl: 1.6090058088302612 (1.6177067018564135)
| > loss_feat: 5.7997236251831055 (6.631507999912934)
| > loss_mel: 14.687357902526855 (15.467762917346572)
| > loss_duration: 1.450129508972168 (1.4095009307818842)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.643085479736328 (27.272170383308936)
| > grad_norm_1: tensor(48.7569, device='cuda:0') (tensor(203.2927, device='cuda:0'))
| > current_lr_0: 0.00019987503124609398
| > current_lr_1: 0.00019987503124609398
| > step_time: 0.7443 (0.6128710643751317)
| > loader_time: 0.009 (0.007362427849546571)
--> TIME: 2025-05-14 11:16:06 -- STEP: 549/630 -- GLOBAL_STEP: 880700
| > loss_disc: 2.6516427993774414 (2.615751004175625)
| > loss_disc_real_0: 0.1910640001296997 (0.17541471608186684)
| > loss_disc_real_1: 0.27677375078201294 (0.21464949521916377)
| > loss_disc_real_2: 0.2848183214664459 (0.23076651132714768)
| > loss_disc_real_3: 0.25831151008605957 (0.23086688986458623)
| > loss_disc_real_4: 0.2412899285554886 (0.24037479260471567)
| > loss_disc_real_5: 0.19360364973545074 (0.23469062952938838)
| > loss_0: 2.6516427993774414 (2.615751004175625)
| > grad_norm_0: tensor(32.1143, device='cuda:0') (tensor(16.2383, device='cuda:0'))
| > loss_gen: 2.2122201919555664 (2.153483457035486)
| > loss_kl: 1.6132440567016602 (1.6190996246042582)
| > loss_feat: 6.8945770263671875 (6.6190400167023995)
| > loss_mel: 15.804304122924805 (15.443114058350387)
| > loss_duration: 1.4766430854797363 (1.4201181286671118)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.000988006591797 (27.254855362661115)
| > grad_norm_1: tensor(430.0903, device='cuda:0') (tensor(210.0693, device='cuda:0'))
| > current_lr_0: 0.00019987503124609398
| > current_lr_1: 0.00019987503124609398
| > step_time: 0.9437 (0.6493195102080187)
| > loader_time: 0.0125 (0.007908544036642883)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005251924196879069 (+0.0002949237823486328)
| > avg_loss_disc: 2.5466028650601706 (-0.14943848053614284)
| > avg_loss_disc_real_0: 0.17147818145652613 (+0.009305770819385856)
| > avg_loss_disc_real_1: 0.1958782821893692 (+0.0010128642121950693)
| > avg_loss_disc_real_2: 0.19997205461064974 (-0.015488114207983017)
| > avg_loss_disc_real_3: 0.22461191564798355 (-0.023793041706085205)
| > avg_loss_disc_real_4: 0.25991579269369447 (+0.013033437232176509)
| > avg_loss_disc_real_5: 0.24240132297078767 (-0.009038995951414136)
| > avg_loss_0: 2.5466028650601706 (-0.14943848053614284)
| > avg_loss_gen: 2.134630878766378 (+0.23467315236727404)
| > avg_loss_kl: 1.735931654771169 (+0.06025517980257655)
| > avg_loss_feat: 6.794995506604512 (+0.38936511675516705)
| > avg_loss_mel: 15.629175901412964 (+0.24052095413208008)
| > avg_loss_duration: 1.5251294076442719 (+0.0013466179370880127)
| > avg_loss_1: 27.819863319396973 (+0.9261601765950509)
> EPOCH: 6/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:17:41)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:17:52 -- STEP: 19/630 -- GLOBAL_STEP: 880800
| > loss_disc: 2.5543386936187744 (2.573853141383121)
| > loss_disc_real_0: 0.2492377758026123 (0.16963736320796766)
| > loss_disc_real_1: 0.20937031507492065 (0.21806866479547402)
| > loss_disc_real_2: 0.24304956197738647 (0.22562114110118464)
| > loss_disc_real_3: 0.2187308967113495 (0.2310079242053785)
| > loss_disc_real_4: 0.23400583863258362 (0.23856572179417862)
| > loss_disc_real_5: 0.19076158106327057 (0.23715425008221677)
| > loss_0: 2.5543386936187744 (2.573853141383121)
| > grad_norm_0: tensor(27.7770, device='cuda:0') (tensor(16.0218, device='cuda:0'))
| > loss_gen: 2.2157857418060303 (2.2441327948319283)
| > loss_kl: 1.767714500427246 (1.4969992135700427)
| > loss_feat: 7.980673313140869 (7.088567608281186)
| > loss_mel: 16.28488540649414 (15.634557272258558)
| > loss_duration: 1.4206526279449463 (1.4269405352441888)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.66971206665039 (27.891197405363386)
| > grad_norm_1: tensor(456.2064, device='cuda:0') (tensor(193.8302, device='cuda:0'))
| > current_lr_0: 0.0001998500468671882
| > current_lr_1: 0.0001998500468671882
| > step_time: 0.5348 (0.5196915802202726)
| > loader_time: 0.0056 (0.004924974943462171)
--> TIME: 2025-05-14 11:18:47 -- STEP: 119/630 -- GLOBAL_STEP: 880900
| > loss_disc: 2.7107701301574707 (2.6181739358340983)
| > loss_disc_real_0: 0.1688322126865387 (0.17416270346451204)
| > loss_disc_real_1: 0.2221258580684662 (0.21531688866495086)
| > loss_disc_real_2: 0.23626933991909027 (0.23081998464440098)
| > loss_disc_real_3: 0.24669982492923737 (0.23123778953772633)
| > loss_disc_real_4: 0.23925280570983887 (0.2398214812288765)
| > loss_disc_real_5: 0.223138228058815 (0.23695726354582972)
| > loss_0: 2.7107701301574707 (2.6181739358340983)
| > grad_norm_0: tensor(10.3094, device='cuda:0') (tensor(14.2640, device='cuda:0'))
| > loss_gen: 2.099547863006592 (2.1674402120734464)
| > loss_kl: 1.58018159866333 (1.6017327959797962)
| > loss_feat: 5.943609714508057 (6.766867473345845)
| > loss_mel: 15.638017654418945 (15.572656038428555)
| > loss_duration: 1.478529691696167 (1.4063475702991004)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.739885330200195 (27.5150441081584)
| > grad_norm_1: tensor(42.4736, device='cuda:0') (tensor(160.3077, device='cuda:0'))
| > current_lr_0: 0.0001998500468671882
| > current_lr_1: 0.0001998500468671882
| > step_time: 0.5482 (0.537288086754935)
| > loader_time: 0.0058 (0.005605072534384845)
--> TIME: 2025-05-14 11:19:47 -- STEP: 219/630 -- GLOBAL_STEP: 881000
| > loss_disc: 2.5719478130340576 (2.613484688545471)
| > loss_disc_real_0: 0.13709385693073273 (0.17512116064083622)
| > loss_disc_real_1: 0.20168879628181458 (0.21547141392209215)
| > loss_disc_real_2: 0.24986860156059265 (0.2298572078415248)
| > loss_disc_real_3: 0.20967891812324524 (0.22847930794437182)
| > loss_disc_real_4: 0.20771671831607819 (0.2401917176023466)
| > loss_disc_real_5: 0.1926252245903015 (0.23703851989687305)
| > loss_0: 2.5719478130340576 (2.613484688545471)
| > grad_norm_0: tensor(15.2199, device='cuda:0') (tensor(14.5315, device='cuda:0'))
| > loss_gen: 2.0885396003723145 (2.1693097211454577)
| > loss_kl: 1.6459472179412842 (1.611783373301432)
| > loss_feat: 7.840531349182129 (6.807167567074571)
| > loss_mel: 15.853684425354004 (15.615627275754328)
| > loss_duration: 1.504267692565918 (1.3736604125532388)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.932971954345703 (27.57754835363937)
| > grad_norm_1: tensor(145.2742, device='cuda:0') (tensor(182.1982, device='cuda:0'))
| > current_lr_0: 0.0001998500468671882
| > current_lr_1: 0.0001998500468671882
| > step_time: 0.5927 (0.5619635451329899)
| > loader_time: 0.0075 (0.006180482367946677)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_881000.pth
--> TIME: 2025-05-14 11:20:55 -- STEP: 319/630 -- GLOBAL_STEP: 881100
| > loss_disc: 2.6485509872436523 (2.617480477569245)
| > loss_disc_real_0: 0.18019482493400574 (0.17591958633130614)
| > loss_disc_real_1: 0.17571359872817993 (0.21539541294208514)
| > loss_disc_real_2: 0.23674233257770538 (0.23049286162031107)
| > loss_disc_real_3: 0.2248619645833969 (0.22858951551413462)
| > loss_disc_real_4: 0.24740557372570038 (0.24048851645291786)
| > loss_disc_real_5: 0.18244490027427673 (0.23584867000206136)
| > loss_0: 2.6485509872436523 (2.617480477569245)
| > grad_norm_0: tensor(9.2763, device='cuda:0') (tensor(14.8658, device='cuda:0'))
| > loss_gen: 2.0430426597595215 (2.1727565474644743)
| > loss_kl: 1.5849120616912842 (1.6146820873302359)
| > loss_feat: 7.380484580993652 (6.7788335940680895)
| > loss_mel: 15.942156791687012 (15.584018474088568)
| > loss_duration: 1.495469093322754 (1.4009380751642695)
| > amp_scaler: 512.0 (312.1755485893417)
| > loss_1: 28.446067810058594 (27.551228747472493)
| > grad_norm_1: tensor(182.4602, device='cuda:0') (tensor(185.5027, device='cuda:0'))
| > current_lr_0: 0.0001998500468671882
| > current_lr_1: 0.0001998500468671882
| > step_time: 0.6474 (0.583772842413206)
| > loader_time: 0.0084 (0.006744518549091016)
--> TIME: 2025-05-14 11:22:06 -- STEP: 419/630 -- GLOBAL_STEP: 881200
| > loss_disc: 2.5573248863220215 (2.6166642321038096)
| > loss_disc_real_0: 0.15736156702041626 (0.17545509811375185)
| > loss_disc_real_1: 0.1778135895729065 (0.21487108424199225)
| > loss_disc_real_2: 0.2019670605659485 (0.23149011662865596)
| > loss_disc_real_3: 0.21348387002944946 (0.22973147006194175)
| > loss_disc_real_4: 0.24528029561042786 (0.2404151150605559)
| > loss_disc_real_5: 0.19209334254264832 (0.23445161892576832)
| > loss_0: 2.5573248863220215 (2.6166642321038096)
| > grad_norm_0: tensor(19.6890, device='cuda:0') (tensor(16.0559, device='cuda:0'))
| > loss_gen: 2.0384624004364014 (2.171992524996009)
| > loss_kl: 1.6575628519058228 (1.6283515495445966)
| > loss_feat: 7.082214832305908 (6.756600847676715)
| > loss_mel: 16.206844329833984 (15.5753297487136)
| > loss_duration: 1.451568841934204 (1.4027367670951425)
| > amp_scaler: 256.0 (335.4272076372315)
| > loss_1: 28.4366512298584 (27.535011423516103)
| > grad_norm_1: tensor(147.7217, device='cuda:0') (tensor(192.7318, device='cuda:0'))
| > current_lr_0: 0.0001998500468671882
| > current_lr_1: 0.0001998500468671882
| > step_time: 0.7146 (0.6122585310287296)
| > loader_time: 0.0092 (0.0072458780466229935)
--> TIME: 2025-05-14 11:23:26 -- STEP: 519/630 -- GLOBAL_STEP: 881300
| > loss_disc: 2.664377450942993 (2.6176413727174164)
| > loss_disc_real_0: 0.1525922566652298 (0.17642625923733254)
| > loss_disc_real_1: 0.2827359735965729 (0.21459289500938444)
| > loss_disc_real_2: 0.21846087276935577 (0.23111010599802453)
| > loss_disc_real_3: 0.19277901947498322 (0.22980614689848097)
| > loss_disc_real_4: 0.2243584841489792 (0.24038843411471342)
| > loss_disc_real_5: 0.24109067022800446 (0.2347363684046475)
| > loss_0: 2.664377450942993 (2.6176413727174164)
| > grad_norm_0: tensor(8.5522, device='cuda:0') (tensor(16.6106, device='cuda:0'))
| > loss_gen: 1.9831199645996094 (2.169664652361347)
| > loss_kl: 1.6865872144699097 (1.6311982415315047)
| > loss_feat: 6.6585164070129395 (6.701508793987061)
| > loss_mel: 15.166685104370117 (15.564145288485784)
| > loss_duration: 1.4200408458709717 (1.414857113522142)
| > amp_scaler: 256.0 (320.1233140655106)
| > loss_1: 26.914947509765625 (27.481374049692025)
| > grad_norm_1: tensor(59.2001, device='cuda:0') (tensor(198.5373, device='cuda:0'))
| > current_lr_0: 0.0001998500468671882
| > current_lr_1: 0.0001998500468671882
| > step_time: 0.855 (0.6456259123851801)
| > loader_time: 0.0097 (0.007759516868517807)
--> TIME: 2025-05-14 11:25:04 -- STEP: 619/630 -- GLOBAL_STEP: 881400
| > loss_disc: 2.598288059234619 (2.6156480762993217)
| > loss_disc_real_0: 0.20778022706508636 (0.17639655637914414)
| > loss_disc_real_1: 0.2590614855289459 (0.21433616320035387)
| > loss_disc_real_2: 0.2618822753429413 (0.23061503149773654)
| > loss_disc_real_3: 0.19398760795593262 (0.22945730501307424)
| > loss_disc_real_4: 0.22775864601135254 (0.2401416353002696)
| > loss_disc_real_5: 0.22621369361877441 (0.23568902182752366)
| > loss_0: 2.598288059234619 (2.6156480762993217)
| > grad_norm_0: tensor(11.4782, device='cuda:0') (tensor(15.7903, device='cuda:0'))
| > loss_gen: 2.117863416671753 (2.1702799042130128)
| > loss_kl: 1.7954919338226318 (1.6313315552925634)
| > loss_feat: 6.006086349487305 (6.6813294814360935)
| > loss_mel: 15.147285461425781 (15.554567851619689)
| > loss_duration: 1.5159847736358643 (1.424676183930121)
| > amp_scaler: 256.0 (309.7641357027461)
| > loss_1: 26.582712173461914 (27.46218494606326)
| > grad_norm_1: tensor(100.4284, device='cuda:0') (tensor(182.7890, device='cuda:0'))
| > current_lr_0: 0.0001998500468671882
| > current_lr_1: 0.0001998500468671882
| > step_time: 1.164 (0.696242920223846)
| > loader_time: 0.0157 (0.008414761507838531)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005007306734720866 (-0.0002446174621582031)
| > avg_loss_disc: 2.6628320614496865 (+0.1162291963895159)
| > avg_loss_disc_real_0: 0.34198345988988876 (+0.17050527843336263)
| > avg_loss_disc_real_1: 0.1730128526687622 (-0.022865429520606995)
| > avg_loss_disc_real_2: 0.20516874889532724 (+0.0051966942846775055)
| > avg_loss_disc_real_3: 0.21495373422900835 (-0.009658181418975204)
| > avg_loss_disc_real_4: 0.2293908384939035 (-0.030524954199790982)
| > avg_loss_disc_real_5: 0.21033805732925734 (-0.032063265641530336)
| > avg_loss_0: 2.6628320614496865 (+0.1162291963895159)
| > avg_loss_gen: 2.2428608437379203 (+0.10822996497154236)
| > avg_loss_kl: 1.8006977836290996 (+0.06476612885793065)
| > avg_loss_feat: 6.7692839701970415 (-0.025711536407470703)
| > avg_loss_mel: 15.64417298634847 (+0.014997084935506777)
| > avg_loss_duration: 1.531880925099055 (+0.006751517454783196)
| > avg_loss_1: 27.98889668782552 (+0.169033368428547)
> EPOCH: 7/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:25:25)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:26:14 -- STEP: 89/630 -- GLOBAL_STEP: 881500
| > loss_disc: 2.547827959060669 (2.5776336594913785)
| > loss_disc_real_0: 0.12199367582798004 (0.17109343518366973)
| > loss_disc_real_1: 0.17683368921279907 (0.21465947286466533)
| > loss_disc_real_2: 0.22428955137729645 (0.22898724457521116)
| > loss_disc_real_3: 0.21450626850128174 (0.23023754291320114)
| > loss_disc_real_4: 0.19111497700214386 (0.24318140644705696)
| > loss_disc_real_5: 0.2840726673603058 (0.22063256783431837)
| > loss_0: 2.547827959060669 (2.5776336594913785)
| > grad_norm_0: tensor(20.7452, device='cuda:0') (tensor(20.5531, device='cuda:0'))
| > loss_gen: 2.1720337867736816 (2.240115361267261)
| > loss_kl: 1.2746645212173462 (1.5719178660532063)
| > loss_feat: 7.218859672546387 (6.954612228307831)
| > loss_mel: 15.589953422546387 (15.628289362018029)
| > loss_duration: 1.4589660167694092 (1.4436175073130746)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.714475631713867 (27.83855215351233)
| > grad_norm_1: tensor(77.4960, device='cuda:0') (tensor(278.3564, device='cuda:0'))
| > current_lr_0: 0.00019982506561132978
| > current_lr_1: 0.00019982506561132978
| > step_time: 0.6011 (0.5255439174309207)
| > loader_time: 0.0069 (0.005278927556584389)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_881500.pth
--> TIME: 2025-05-14 11:27:15 -- STEP: 189/630 -- GLOBAL_STEP: 881600
| > loss_disc: 2.511181354522705 (2.5799403531210756)
| > loss_disc_real_0: 0.2343229502439499 (0.17210268501251463)
| > loss_disc_real_1: 0.1718575358390808 (0.21376498591489893)
| > loss_disc_real_2: 0.21590396761894226 (0.22912191169917898)
| > loss_disc_real_3: 0.26452934741973877 (0.2284208545609126)
| > loss_disc_real_4: 0.27553656697273254 (0.2407559417385273)
| > loss_disc_real_5: 0.27372512221336365 (0.2236257846708651)
| > loss_0: 2.511181354522705 (2.5799403531210756)
| > grad_norm_0: tensor(21.0380, device='cuda:0') (tensor(23.7535, device='cuda:0'))
| > loss_gen: 2.3426055908203125 (2.248529931855581)
| > loss_kl: 1.7344425916671753 (1.6061441324375294)
| > loss_feat: 6.575538635253906 (6.956214776114813)
| > loss_mel: 15.805710792541504 (15.712169833914944)
| > loss_duration: 1.4294317960739136 (1.3904035532916037)
| > amp_scaler: 128.0 (194.37037037037038)
| > loss_1: 27.88772964477539 (27.91346227050458)
| > grad_norm_1: tensor(242.8207, device='cuda:0') (tensor(315.9441, device='cuda:0'))
| > current_lr_0: 0.00019982506561132978
| > current_lr_1: 0.00019982506561132978
| > step_time: 0.5671 (0.5471017032704024)
| > loader_time: 0.0068 (0.0058676149479295805)
--> TIME: 2025-05-14 11:28:17 -- STEP: 289/630 -- GLOBAL_STEP: 881700
| > loss_disc: 2.5708703994750977 (2.5798210429485273)
| > loss_disc_real_0: 0.1018230989575386 (0.1716459584019588)
| > loss_disc_real_1: 0.21608933806419373 (0.21402369421555506)
| > loss_disc_real_2: 0.23442454636096954 (0.22773936597121217)
| > loss_disc_real_3: 0.20816966891288757 (0.22708838270609766)
| > loss_disc_real_4: 0.2367669939994812 (0.23926259231814875)
| > loss_disc_real_5: 0.26562511920928955 (0.22628066299489624)
| > loss_0: 2.5708703994750977 (2.5798210429485273)
| > grad_norm_0: tensor(17.9494, device='cuda:0') (tensor(22.4479, device='cuda:0'))
| > loss_gen: 2.163170099258423 (2.234045703518351)
| > loss_kl: 1.8626645803451538 (1.6147225336220021)
| > loss_feat: 6.800428867340088 (6.908155774575203)
| > loss_mel: 15.213729858398438 (15.688898805928478)
| > loss_duration: 1.4726064205169678 (1.3947479873380033)
| > amp_scaler: 128.0 (171.40484429065745)
| > loss_1: 27.51259994506836 (27.84057079961968)
| > grad_norm_1: tensor(232.4678, device='cuda:0') (tensor(292.7473, device='cuda:0'))
| > current_lr_0: 0.00019982506561132978
| > current_lr_1: 0.00019982506561132978
| > step_time: 0.6268 (0.5696647794188923)
| > loader_time: 0.0081 (0.006376833239228666)
--> TIME: 2025-05-14 11:29:26 -- STEP: 389/630 -- GLOBAL_STEP: 881800
| > loss_disc: 2.498274087905884 (2.5838719633980087)
| > loss_disc_real_0: 0.19087447226047516 (0.17235524462090673)
| > loss_disc_real_1: 0.17539291083812714 (0.21357593555147053)
| > loss_disc_real_2: 0.23221319913864136 (0.22785177819220143)
| > loss_disc_real_3: 0.19064538180828094 (0.22650164492179312)
| > loss_disc_real_4: 0.2544611990451813 (0.23998409444538057)
| > loss_disc_real_5: 0.22819945216178894 (0.228628196301068)
| > loss_0: 2.498274087905884 (2.5838719633980087)
| > grad_norm_0: tensor(7.4655, device='cuda:0') (tensor(20.0601, device='cuda:0'))
| > loss_gen: 2.187617778778076 (2.2247744912047027)
| > loss_kl: 1.7142047882080078 (1.614018586729976)
| > loss_feat: 7.182023048400879 (6.873481138812852)
| > loss_mel: 15.792935371398926 (15.679076447278492)
| > loss_duration: 1.489730715751648 (1.4120371341705316)
| > amp_scaler: 128.0 (160.24678663239075)
| > loss_1: 28.366512298583984 (27.80338777674501)
| > grad_norm_1: tensor(105.9317, device='cuda:0') (tensor(252.8447, device='cuda:0'))
| > current_lr_0: 0.00019982506561132978
| > current_lr_1: 0.00019982506561132978
| > step_time: 0.7177 (0.5967123379744104)
| > loader_time: 0.0103 (0.0069191786807729526)
--> TIME: 2025-05-14 11:30:45 -- STEP: 489/630 -- GLOBAL_STEP: 881900
| > loss_disc: 2.5944533348083496 (2.58572175117602)
| > loss_disc_real_0: 0.17763419449329376 (0.17234614793142664)
| > loss_disc_real_1: 0.24586424231529236 (0.2141197198099154)
| > loss_disc_real_2: 0.3136477768421173 (0.2281530639023381)
| > loss_disc_real_3: 0.2615189254283905 (0.22708992129820257)
| > loss_disc_real_4: 0.2464628517627716 (0.24008414606375197)
| > loss_disc_real_5: 0.23732653260231018 (0.2280328108915766)
| > loss_0: 2.5944533348083496 (2.58572175117602)
| > grad_norm_0: tensor(13.0404, device='cuda:0') (tensor(20.8884, device='cuda:0'))
| > loss_gen: 2.128565788269043 (2.222586360202003)
| > loss_kl: 1.4861923456192017 (1.6166194153222078)
| > loss_feat: 6.731064319610596 (6.828733087317344)
| > loss_mel: 14.806007385253906 (15.650223172271666)
| > loss_duration: 1.4556609392166138 (1.41225087008837)
| > amp_scaler: 128.0 (153.65235173824135)
| > loss_1: 26.60749053955078 (27.7304129064205)
| > grad_norm_1: tensor(242.9043, device='cuda:0') (tensor(259.6563, device='cuda:0'))
| > current_lr_0: 0.00019982506561132978
| > current_lr_1: 0.00019982506561132978
| > step_time: 0.788 (0.6331557286541394)
| > loader_time: 0.0094 (0.007478687660825764)
--> TIME: 2025-05-14 11:32:14 -- STEP: 589/630 -- GLOBAL_STEP: 882000
| > loss_disc: 2.5998892784118652 (2.592604128330796)
| > loss_disc_real_0: 0.13124489784240723 (0.17249584359912185)
| > loss_disc_real_1: 0.27008870244026184 (0.21415085909676268)
| > loss_disc_real_2: 0.24801139533519745 (0.22864948956893538)
| > loss_disc_real_3: 0.21531856060028076 (0.22785605363712247)
| > loss_disc_real_4: 0.264617919921875 (0.24043615597516854)
| > loss_disc_real_5: 0.23065412044525146 (0.22953565120191044)
| > loss_0: 2.5998892784118652 (2.592604128330796)
| > grad_norm_0: tensor(11.9295, device='cuda:0') (tensor(19.9352, device='cuda:0'))
| > loss_gen: 2.217015027999878 (2.210777482071637)
| > loss_kl: 1.6269490718841553 (1.618880457708102)
| > loss_feat: 6.259328842163086 (6.779872400448965)
| > loss_mel: 15.654276847839355 (15.656596335976152)
| > loss_duration: 1.4820836782455444 (1.4222590320179127)
| > amp_scaler: 128.0 (149.29711375212236)
| > loss_1: 27.239652633666992 (27.688385722187867)
| > grad_norm_1: tensor(71.9185, device='cuda:0') (tensor(243.4369, device='cuda:0'))
| > current_lr_0: 0.00019982506561132978
| > current_lr_1: 0.00019982506561132978
| > step_time: 0.9393 (0.674989886923435)
| > loader_time: 0.0114 (0.008084371255897303)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_882000.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005147238572438558 (+0.00013993183771769148)
| > avg_loss_disc: 2.5932882626851397 (-0.06954379876454686)
| > avg_loss_disc_real_0: 0.17588124920924506 (-0.1661022106806437)
| > avg_loss_disc_real_1: 0.20688872039318085 (+0.03387586772441864)
| > avg_loss_disc_real_2: 0.2263301114241282 (+0.021161362528800964)
| > avg_loss_disc_real_3: 0.2820998951792717 (+0.06714616095026335)
| > avg_loss_disc_real_4: 0.25512872139612836 (+0.025737882902224868)
| > avg_loss_disc_real_5: 0.2308050865928332 (+0.020467029263575853)
| > avg_loss_0: 2.5932882626851397 (-0.06954379876454686)
| > avg_loss_gen: 2.1316262086232505 (-0.1112346351146698)
| > avg_loss_kl: 1.7384624183177948 (-0.0622353653113048)
| > avg_loss_feat: 6.134666224320729 (-0.6346177458763123)
| > avg_loss_mel: 15.712168216705322 (+0.06799523035685162)
| > avg_loss_duration: 1.5210553606351216 (-0.010825564463933457)
| > avg_loss_1: 27.237978140513103 (-0.7509185473124163)
> EPOCH: 8/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:33:13)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:33:45 -- STEP: 59/630 -- GLOBAL_STEP: 882100
| > loss_disc: 2.553854465484619 (2.600319033962185)
| > loss_disc_real_0: 0.13410750031471252 (0.16997764032270948)
| > loss_disc_real_1: 0.2615089416503906 (0.2134487990100505)
| > loss_disc_real_2: 0.20421089231967926 (0.23268611577607817)
| > loss_disc_real_3: 0.22861947119235992 (0.229021019602226)
| > loss_disc_real_4: 0.23075364530086517 (0.2419852614402771)
| > loss_disc_real_5: 0.21390800178050995 (0.23494297922667812)
| > loss_0: 2.553854465484619 (2.600319033962185)
| > grad_norm_0: tensor(10.8459, device='cuda:0') (tensor(14.3603, device='cuda:0'))
| > loss_gen: 2.0959911346435547 (2.2021249613519442)
| > loss_kl: 1.4019174575805664 (1.5463539180109056)
| > loss_feat: 6.881077766418457 (6.938709372181004)
| > loss_mel: 15.045957565307617 (15.567689588514424)
| > loss_duration: 1.4481499195098877 (1.4315803010584944)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.87309455871582 (27.686458135055283)
| > grad_norm_1: tensor(81.6805, device='cuda:0') (tensor(130.3252, device='cuda:0'))
| > current_lr_0: 0.00019980008747812837
| > current_lr_1: 0.00019980008747812837
| > step_time: 0.5436 (0.5250005398766467)
| > loader_time: 0.006 (0.005289461653111346)
--> TIME: 2025-05-14 11:34:42 -- STEP: 159/630 -- GLOBAL_STEP: 882200
| > loss_disc: 2.682387590408325 (2.595844678159029)
| > loss_disc_real_0: 0.07554370164871216 (0.16957944308249462)
| > loss_disc_real_1: 0.17175781726837158 (0.21153411278559728)
| > loss_disc_real_2: 0.20648454129695892 (0.231117751988225)
| > loss_disc_real_3: 0.2697749733924866 (0.23049763266770346)
| > loss_disc_real_4: 0.2798961102962494 (0.24198144158852175)
| > loss_disc_real_5: 0.2883248031139374 (0.2346709406225936)
| > loss_0: 2.682387590408325 (2.595844678159029)
| > grad_norm_0: tensor(14.3538, device='cuda:0') (tensor(13.8214, device='cuda:0'))
| > loss_gen: 2.091317892074585 (2.1944043298937235)
| > loss_kl: 1.6611449718475342 (1.5765326300507074)
| > loss_feat: 6.634852409362793 (6.854992446659496)
| > loss_mel: 16.111896514892578 (15.539310497307927)
| > loss_duration: 1.4773495197296143 (1.3760292784972756)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.9765625 (27.54126921839684)
| > grad_norm_1: tensor(117.4267, device='cuda:0') (tensor(158.9918, device='cuda:0'))
| > current_lr_0: 0.00019980008747812837
| > current_lr_1: 0.00019980008747812837
| > step_time: 0.5624 (0.5456412768214001)
| > loader_time: 0.0064 (0.005800917463482551)
--> TIME: 2025-05-14 11:35:44 -- STEP: 259/630 -- GLOBAL_STEP: 882300
| > loss_disc: 2.5520081520080566 (2.5912634967376817)
| > loss_disc_real_0: 0.12050794064998627 (0.1719521041312273)
| > loss_disc_real_1: 0.24954438209533691 (0.21309530424335288)
| > loss_disc_real_2: 0.1991199105978012 (0.2302075009433459)
| > loss_disc_real_3: 0.22568915784358978 (0.2300990728452859)
| > loss_disc_real_4: 0.2223070114850998 (0.24048343720813514)
| > loss_disc_real_5: 0.1856682002544403 (0.23005703678462497)
| > loss_0: 2.5520081520080566 (2.5912634967376817)
| > grad_norm_0: tensor(35.1083, device='cuda:0') (tensor(16.8442, device='cuda:0'))
| > loss_gen: 2.229531764984131 (2.2181732378411)
| > loss_kl: 1.2978142499923706 (1.5910070674299734)
| > loss_feat: 7.340092182159424 (6.851377004822249)
| > loss_mel: 15.729005813598633 (15.565570249520674)
| > loss_duration: 1.4562560319900513 (1.385999636760549)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.052701950073242 (27.612127274620025)
| > grad_norm_1: tensor(707.5511, device='cuda:0') (tensor(207.0697, device='cuda:0'))
| > current_lr_0: 0.00019980008747812837
| > current_lr_1: 0.00019980008747812837
| > step_time: 0.6126 (0.5688847556537641)
| > loader_time: 0.0072 (0.006355904244087837)
--> TIME: 2025-05-14 11:36:52 -- STEP: 359/630 -- GLOBAL_STEP: 882400
| > loss_disc: 2.4516396522521973 (2.5887880484705836)
| > loss_disc_real_0: 0.1925220787525177 (0.17234426047808613)
| > loss_disc_real_1: 0.17381620407104492 (0.2127200466344615)
| > loss_disc_real_2: 0.20925839245319366 (0.2305616962212374)
| > loss_disc_real_3: 0.15582314133644104 (0.2291696179128955)
| > loss_disc_real_4: 0.22239020466804504 (0.2402184022834374)
| > loss_disc_real_5: 0.209773451089859 (0.22843171589719885)
| > loss_0: 2.4516396522521973 (2.5887880484705836)
| > grad_norm_0: tensor(33.3652, device='cuda:0') (tensor(19.0497, device='cuda:0'))
| > loss_gen: 2.1969475746154785 (2.2187098357670827)
| > loss_kl: 1.4488811492919922 (1.5929200293958017)
| > loss_feat: 7.828907012939453 (6.83108981007653)
| > loss_mel: 16.19223403930664 (15.578991313498664)
| > loss_duration: 1.4602162837982178 (1.4055843044456326)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 29.127185821533203 (27.627295310782856)
| > grad_norm_1: tensor(299.5578, device='cuda:0') (tensor(233.5294, device='cuda:0'))
| > current_lr_0: 0.00019980008747812837
| > current_lr_1: 0.00019980008747812837
| > step_time: 0.6929 (0.5962435820640625)
| > loader_time: 0.0086 (0.006880466652447799)
--> TIME: 2025-05-14 11:38:07 -- STEP: 459/630 -- GLOBAL_STEP: 882500
| > loss_disc: 2.460017681121826 (2.585697766222984)
| > loss_disc_real_0: 0.13925151526927948 (0.17188498684588605)
| > loss_disc_real_1: 0.22955214977264404 (0.21166130838700625)
| > loss_disc_real_2: 0.23086388409137726 (0.2303240862806898)
| > loss_disc_real_3: 0.21860839426517487 (0.22999204747167806)
| > loss_disc_real_4: 0.20394213497638702 (0.23992367228391642)
| > loss_disc_real_5: 0.21734891831874847 (0.22818133838815627)
| > loss_0: 2.460017681121826 (2.585697766222984)
| > grad_norm_0: tensor(8.4188, device='cuda:0') (tensor(19.6827, device='cuda:0'))
| > loss_gen: 2.3496315479278564 (2.2167649843074657)
| > loss_kl: 1.6625547409057617 (1.6020997271818271)
| > loss_feat: 6.3946852684021 (6.798850295330704)
| > loss_mel: 15.487318992614746 (15.559959972605986)
| > loss_duration: 1.4200198650360107 (1.406298381830352)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.314210891723633 (27.58397341709511)
| > grad_norm_1: tensor(139.9465, device='cuda:0') (tensor(240.6744, device='cuda:0'))
| > current_lr_0: 0.00019980008747812837
| > current_lr_1: 0.00019980008747812837
| > step_time: 0.7523 (0.6259674636367099)
| > loader_time: 0.0097 (0.007432814517052345)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_882500.pth
--> TIME: 2025-05-14 11:39:35 -- STEP: 559/630 -- GLOBAL_STEP: 882600
| > loss_disc: 2.53824520111084 (2.587077968662241)
| > loss_disc_real_0: 0.1090468317270279 (0.17243646223877757)
| > loss_disc_real_1: 0.26428335905075073 (0.2116296544191236)
| > loss_disc_real_2: 0.22242240607738495 (0.229640159522698)
| > loss_disc_real_3: 0.27383697032928467 (0.2299260042861024)
| > loss_disc_real_4: 0.2818055748939514 (0.23993386248249915)
| > loss_disc_real_5: 0.2508341073989868 (0.23009443616291278)
| > loss_0: 2.53824520111084 (2.587077968662241)
| > grad_norm_0: tensor(11.5605, device='cuda:0') (tensor(18.5532, device='cuda:0'))
| > loss_gen: 2.276912212371826 (2.2125989578277783)
| > loss_kl: 1.5991120338439941 (1.6029638504086325)
| > loss_feat: 7.482673645019531 (6.762315439623454)
| > loss_mel: 15.139538764953613 (15.576502045919728)
| > loss_duration: 1.4784051179885864 (1.4166535249976215)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.976642608642578 (27.57103385993535)
| > grad_norm_1: tensor(149.0688, device='cuda:0') (tensor(223.2904, device='cuda:0'))
| > current_lr_0: 0.00019980008747812837
| > current_lr_1: 0.00019980008747812837
| > step_time: 0.8483 (0.6629174838978829)
| > loader_time: 0.011 (0.008001655073626527)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.00537031888961792 (+0.00022308031717936227)
| > avg_loss_disc: 2.7363478342692056 (+0.1430595715840659)
| > avg_loss_disc_real_0: 0.15558235409359136 (-0.020298895115653692)
| > avg_loss_disc_real_1: 0.26525014266371727 (+0.05836142227053642)
| > avg_loss_disc_real_2: 0.31807700047890347 (+0.09174688905477527)
| > avg_loss_disc_real_3: 0.24156367282072702 (-0.04053622235854468)
| > avg_loss_disc_real_4: 0.23980327447255453 (-0.015325446923573821)
| > avg_loss_disc_real_5: 0.2609216471513112 (+0.030116560558478028)
| > avg_loss_0: 2.7363478342692056 (+0.1430595715840659)
| > avg_loss_gen: 2.1286415457725525 (-0.0029846628506979833)
| > avg_loss_kl: 1.6381353040536244 (-0.1003271142641704)
| > avg_loss_feat: 6.391209880510966 (+0.256543656190237)
| > avg_loss_mel: 15.396269162495932 (-0.3158990542093907)
| > avg_loss_duration: 1.5247027079264324 (+0.0036473472913107763)
| > avg_loss_1: 27.07895835240682 (-0.15901978810628492)
> EPOCH: 9/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:40:58)
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:41:14 -- STEP: 29/630 -- GLOBAL_STEP: 882700
| > loss_disc: 2.563443183898926 (2.6061846141157483)
| > loss_disc_real_0: 0.18966831266880035 (0.17538325822558892)
| > loss_disc_real_1: 0.1876741349697113 (0.21576009896294823)
| > loss_disc_real_2: 0.20854692161083221 (0.232468424172237)
| > loss_disc_real_3: 0.2574041485786438 (0.23643836327667894)
| > loss_disc_real_4: 0.2575233280658722 (0.24282282642249403)
| > loss_disc_real_5: 0.2288496345281601 (0.23147336573436342)
| > loss_0: 2.563443183898926 (2.6061846141157483)
| > grad_norm_0: tensor(7.9772, device='cuda:0') (tensor(26.5852, device='cuda:0'))
| > loss_gen: 2.367332935333252 (2.235730294523567)
| > loss_kl: 1.4079865217208862 (1.5710049086603626)
| > loss_feat: 6.8308892250061035 (7.00314107434503)
| > loss_mel: 15.678466796875 (15.690871468905744)
| > loss_duration: 1.4138176441192627 (1.4372085168443878)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.69849395751953 (27.937956316717738)
| > grad_norm_1: tensor(140.9540, device='cuda:0') (tensor(370.9848, device='cuda:0'))
| > current_lr_0: 0.0001997751124671936
| > current_lr_1: 0.0001997751124671936
| > step_time: 0.5238 (0.5184189040085367)
| > loader_time: 0.0057 (0.005228404341072872)
--> TIME: 2025-05-14 11:42:09 -- STEP: 129/630 -- GLOBAL_STEP: 882800
| > loss_disc: 2.569969415664673 (2.5854126057883566)
| > loss_disc_real_0: 0.20051103830337524 (0.17433966355499367)
| > loss_disc_real_1: 0.20785725116729736 (0.21148981165516284)
| > loss_disc_real_2: 0.17588695883750916 (0.22826679767102234)
| > loss_disc_real_3: 0.22887787222862244 (0.2302031674126322)
| > loss_disc_real_4: 0.2108207494020462 (0.23918264261049818)
| > loss_disc_real_5: 0.25586816668510437 (0.23073692227056783)
| > loss_0: 2.569969415664673 (2.5854126057883566)
| > grad_norm_0: tensor(12.3960, device='cuda:0') (tensor(22.7179, device='cuda:0'))
| > loss_gen: 2.086500883102417 (2.230066511982172)
| > loss_kl: 1.7700105905532837 (1.540034105611402)
| > loss_feat: 6.384365081787109 (6.984329408453417)
| > loss_mel: 15.439699172973633 (15.641834332961444)
| > loss_duration: 1.482862949371338 (1.415788564571115)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.163436889648438 (27.812052881994912)
| > grad_norm_1: tensor(189.8733, device='cuda:0') (tensor(291.2256, device='cuda:0'))
| > current_lr_0: 0.0001997751124671936
| > current_lr_1: 0.0001997751124671936
| > step_time: 0.5449 (0.5360242618146795)
| > loader_time: 0.0058 (0.005646635395611901)
--> TIME: 2025-05-14 11:43:10 -- STEP: 229/630 -- GLOBAL_STEP: 882900
| > loss_disc: 2.6763012409210205 (2.5835751591811524)
| > loss_disc_real_0: 0.13961070775985718 (0.17182785757374042)
| > loss_disc_real_1: 0.27818626165390015 (0.21214895444926216)
| > loss_disc_real_2: 0.2595091462135315 (0.22607532351818668)
| > loss_disc_real_3: 0.23428156971931458 (0.22871021711670156)
| > loss_disc_real_4: 0.2173181176185608 (0.23951819532563073)
| > loss_disc_real_5: 0.1862059086561203 (0.23163908147395437)
| > loss_0: 2.6763012409210205 (2.5835751591811524)
| > grad_norm_0: tensor(14.2352, device='cuda:0') (tensor(20.0661, device='cuda:0'))
| > loss_gen: 2.066584825515747 (2.2239941748989733)
| > loss_kl: 1.5523616075515747 (1.5596942693385492)
| > loss_feat: 6.714180946350098 (6.963616743879027)
| > loss_mel: 16.016599655151367 (15.666510161354031)
| > loss_duration: 1.453287124633789 (1.3787434043842637)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.803014755249023 (27.792558670043945)
| > grad_norm_1: tensor(261.6899, device='cuda:0') (tensor(275.9023, device='cuda:0'))
| > current_lr_0: 0.0001997751124671936
| > current_lr_1: 0.0001997751124671936
| > step_time: 0.6048 (0.560742591666343)
| > loader_time: 0.0077 (0.006174135416355715)
--> TIME: 2025-05-14 11:44:15 -- STEP: 329/630 -- GLOBAL_STEP: 883000
| > loss_disc: 2.5140204429626465 (2.591126320209909)
| > loss_disc_real_0: 0.2082597017288208 (0.17279831495554984)
| > loss_disc_real_1: 0.27946433424949646 (0.21308444757410822)
| > loss_disc_real_2: 0.23179961740970612 (0.2277792446700273)
| > loss_disc_real_3: 0.21520480513572693 (0.22959177454191862)
| > loss_disc_real_4: 0.19686315953731537 (0.23929914664533725)
| > loss_disc_real_5: 0.2035311907529831 (0.2323732129255689)
| > loss_0: 2.5140204429626465 (2.591126320209909)
| > grad_norm_0: tensor(35.6672, device='cuda:0') (tensor(19.5515, device='cuda:0'))
| > loss_gen: 2.283479690551758 (2.2141661346864545)
| > loss_kl: 1.4062812328338623 (1.5729047686858022)
| > loss_feat: 6.12084436416626 (6.889201870080548)
| > loss_mel: 14.787065505981445 (15.627272771122245)
| > loss_duration: 1.480415940284729 (1.404184820079514)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.07808494567871 (27.70773029037522)
| > grad_norm_1: tensor(304.1145, device='cuda:0') (tensor(250.5397, device='cuda:0'))
| > current_lr_0: 0.0001997751124671936
| > current_lr_1: 0.0001997751124671936
| > step_time: 0.6704 (0.5839318852294181)
| > loader_time: 0.0076 (0.006670432250188112)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_883000.pth
--> TIME: 2025-05-14 11:45:31 -- STEP: 429/630 -- GLOBAL_STEP: 883100
| > loss_disc: 2.5723767280578613 (2.58635832768776)
| > loss_disc_real_0: 0.19266735017299652 (0.1722710507993516)
| > loss_disc_real_1: 0.222127765417099 (0.21316066005707898)
| > loss_disc_real_2: 0.23131732642650604 (0.2279569030433268)
| > loss_disc_real_3: 0.22517482936382294 (0.22902195631485164)
| > loss_disc_real_4: 0.23645678162574768 (0.23946066787748627)
| > loss_disc_real_5: 0.22149087488651276 (0.23054980547417017)
| > loss_0: 2.5723767280578613 (2.58635832768776)
| > grad_norm_0: tensor(27.0952, device='cuda:0') (tensor(20.4489, device='cuda:0'))
| > loss_gen: 2.3018953800201416 (2.2164768227886187)
| > loss_kl: 1.688676118850708 (1.5774592144505963)
| > loss_feat: 6.652895450592041 (6.852709296700004)
| > loss_mel: 16.681596755981445 (15.617829822993778)
| > loss_duration: 1.4515771865844727 (1.4052783487004274)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.776641845703125 (27.66975347256605)
| > grad_norm_1: tensor(424.9033, device='cuda:0') (tensor(257.1778, device='cuda:0'))
| > current_lr_0: 0.0001997751124671936
| > current_lr_1: 0.0001997751124671936
| > step_time: 0.7511 (0.6144370927121536)
| > loader_time: 0.0104 (0.007236507389095277)
--> TIME: 2025-05-14 11:46:51 -- STEP: 529/630 -- GLOBAL_STEP: 883200
| > loss_disc: 2.6279189586639404 (2.587208228661118)
| > loss_disc_real_0: 0.19204801321029663 (0.17267212230141774)
| > loss_disc_real_1: 0.23587709665298462 (0.2128828645090525)
| > loss_disc_real_2: 0.19614115357398987 (0.22812554352900932)
| > loss_disc_real_3: 0.2393680363893509 (0.2294240884609619)
| > loss_disc_real_4: 0.22305932641029358 (0.23924983643516476)
| > loss_disc_real_5: 0.23704954981803894 (0.23052567015410824)
| > loss_0: 2.6279189586639404 (2.587208228661118)
| > grad_norm_0: tensor(9.0028, device='cuda:0') (tensor(20.7988, device='cuda:0'))
| > loss_gen: 2.2694780826568604 (2.21693196684291)
| > loss_kl: 1.6190674304962158 (1.5788707730900815)
| > loss_feat: 6.848050117492676 (6.849933796433735)
| > loss_mel: 16.379560470581055 (15.620555037586811)
| > loss_duration: 1.4406639337539673 (1.4169058234119234)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.556819915771484 (27.68319737483062)
| > grad_norm_1: tensor(330.2668, device='cuda:0') (tensor(260.6106, device='cuda:0'))
| > current_lr_0: 0.0001997751124671936
| > current_lr_1: 0.0001997751124671936
| > step_time: 0.8013 (0.6460546442150846)
| > loader_time: 0.0103 (0.007766573100099039)
--> TIME: 2025-05-14 11:48:33 -- STEP: 629/630 -- GLOBAL_STEP: 883300
| > loss_disc: 2.738759756088257 (2.5906382971613517)
| > loss_disc_real_0: 0.1015167310833931 (0.17350687335921977)
| > loss_disc_real_1: 0.21391308307647705 (0.21311840462381404)
| > loss_disc_real_2: 0.24846535921096802 (0.2281235674890691)
| > loss_disc_real_3: 0.25047171115875244 (0.2289030490078873)
| > loss_disc_real_4: 0.2543833255767822 (0.23917116468775254)
| > loss_disc_real_5: 0.26853594183921814 (0.2312880771053994)
| > loss_0: 2.738759756088257 (2.5906382971613517)
| > grad_norm_0: tensor(10.3421, device='cuda:0') (tensor(19.7826, device='cuda:0'))
| > loss_gen: 2.1854214668273926 (2.2078654769873207)
| > loss_kl: 1.5624473094940186 (1.5845221874255249)
| > loss_feat: 6.473028182983398 (6.807920428641462)
| > loss_mel: 16.011436462402344 (15.605492629762296)
| > loss_duration: 1.5069324970245361 (1.4261769977396728)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.739267349243164 (27.631977715060138)
| > grad_norm_1: tensor(117.1080, device='cuda:0') (tensor(243.1039, device='cuda:0'))
| > current_lr_0: 0.0001997751124671936
| > current_lr_1: 0.0001997751124671936
| > step_time: 1.6334 (0.7024156872911564)
| > loader_time: 0.0156 (0.008460559602382643)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.0052361687024434405 (-0.00013415018717447946)
| > avg_loss_disc: 2.6885334054629006 (-0.04781442880630493)
| > avg_loss_disc_real_0: 0.17716650664806366 (+0.021584152554472297)
| > avg_loss_disc_real_1: 0.227289367467165 (-0.03796077519655228)
| > avg_loss_disc_real_2: 0.22167498618364334 (-0.09640201429526013)
| > avg_loss_disc_real_3: 0.2418598048388958 (+0.00029613201816877655)
| > avg_loss_disc_real_4: 0.25695061186949414 (+0.017147337396939605)
| > avg_loss_disc_real_5: 0.26752542952696484 (+0.006603782375653622)
| > avg_loss_0: 2.6885334054629006 (-0.04781442880630493)
| > avg_loss_gen: 2.066851844390233 (-0.06178970138231943)
| > avg_loss_kl: 1.824983835220337 (+0.18684853116671252)
| > avg_loss_feat: 6.677076776822408 (+0.28586689631144147)
| > avg_loss_mel: 15.63687547047933 (+0.24060630798339844)
| > avg_loss_duration: 1.527563323577245 (+0.002860615650812637)
| > avg_loss_1: 27.733351230621338 (+0.6543928782145194)
> EPOCH: 10/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:48:41)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:49:35 -- STEP: 99/630 -- GLOBAL_STEP: 883400
| > loss_disc: 2.402559518814087 (2.5645662750860665)
| > loss_disc_real_0: 0.1192263811826706 (0.1730596799441059)
| > loss_disc_real_1: 0.22304171323776245 (0.21280017705878826)
| > loss_disc_real_2: 0.21670548617839813 (0.22766985616298638)
| > loss_disc_real_3: 0.210807666182518 (0.22960763146178892)
| > loss_disc_real_4: 0.2500951290130615 (0.2394342302071928)
| > loss_disc_real_5: 0.16140705347061157 (0.21855859360610597)
| > loss_0: 2.402559518814087 (2.5645662750860665)
| > grad_norm_0: tensor(6.9270, device='cuda:0') (tensor(20.9836, device='cuda:0'))
| > loss_gen: 2.243626117706299 (2.249715001896174)
| > loss_kl: 1.6120104789733887 (1.547223884649951)
| > loss_feat: 7.31284236907959 (6.982223322897246)
| > loss_mel: 15.379871368408203 (15.456639925638834)
| > loss_duration: 1.4685300588607788 (1.4413464815929682)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.01688003540039 (27.677148857502022)
| > grad_norm_1: tensor(233.2499, device='cuda:0') (tensor(273.6893, device='cuda:0'))
| > current_lr_0: 0.00019975014057813518
| > current_lr_1: 0.00019975014057813518
| > step_time: 0.5457 (0.5240365302923947)
| > loader_time: 0.0064 (0.0054024084649904784)
--> TIME: 2025-05-14 11:50:34 -- STEP: 199/630 -- GLOBAL_STEP: 883500
| > loss_disc: 2.459517240524292 (2.581563809409214)
| > loss_disc_real_0: 0.14198563992977142 (0.17346050916005618)
| > loss_disc_real_1: 0.2268611639738083 (0.21096735975550646)
| > loss_disc_real_2: 0.16700191795825958 (0.22656618350714294)
| > loss_disc_real_3: 0.23609955608844757 (0.22923066568135017)
| > loss_disc_real_4: 0.21719688177108765 (0.23847516644839664)
| > loss_disc_real_5: 0.2328587919473648 (0.22875858779678393)
| > loss_0: 2.459517240524292 (2.581563809409214)
| > grad_norm_0: tensor(13.1133, device='cuda:0') (tensor(18.8380, device='cuda:0'))
| > loss_gen: 2.2983238697052 (2.2206296501447214)
| > loss_kl: 1.7633143663406372 (1.5798233435980633)
| > loss_feat: 7.187002658843994 (6.905227701867645)
| > loss_mel: 16.08978271484375 (15.497299199128271)
| > loss_duration: 1.4402453899383545 (1.3969681161132885)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.778669357299805 (27.59994814503732)
| > grad_norm_1: tensor(56.8639, device='cuda:0') (tensor(275.0194, device='cuda:0'))
| > current_lr_0: 0.00019975014057813518
| > current_lr_1: 0.00019975014057813518
| > step_time: 0.5911 (0.550374428830554)
| > loader_time: 0.0069 (0.005941999617533468)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_883500.pth
--> TIME: 2025-05-14 11:51:41 -- STEP: 299/630 -- GLOBAL_STEP: 883600
| > loss_disc: 2.631441354751587 (2.5876156964828354)
| > loss_disc_real_0: 0.21969319880008698 (0.17387715485383043)
| > loss_disc_real_1: 0.17371055483818054 (0.21223407243705517)
| > loss_disc_real_2: 0.23359239101409912 (0.22692293686212903)
| > loss_disc_real_3: 0.28880801796913147 (0.22878294056873258)
| > loss_disc_real_4: 0.2904047667980194 (0.2385051168725642)
| > loss_disc_real_5: 0.16801497340202332 (0.2303392372551969)
| > loss_0: 2.631441354751587 (2.5876156964828354)
| > grad_norm_0: tensor(17.3040, device='cuda:0') (tensor(16.9307, device='cuda:0'))
| > loss_gen: 2.30556058883667 (2.2037869069887246)
| > loss_kl: 1.6958894729614258 (1.5897734787153157)
| > loss_feat: 6.86480188369751 (6.843963304092254)
| > loss_mel: 15.957942008972168 (15.472382551850284)
| > loss_duration: 1.4324266910552979 (1.3990240647242622)
| > amp_scaler: 256.0 (166.9565217391305)
| > loss_1: 28.256622314453125 (27.50893037215523)
| > grad_norm_1: tensor(272.4738, device='cuda:0') (tensor(228.9751, device='cuda:0'))
| > current_lr_0: 0.00019975014057813518
| > current_lr_1: 0.00019975014057813518
| > step_time: 0.6368 (0.5765222083764724)
| > loader_time: 0.0081 (0.006509759354352152)
--> TIME: 2025-05-14 11:52:51 -- STEP: 399/630 -- GLOBAL_STEP: 883700
| > loss_disc: 2.72636342048645 (2.585255146026611)
| > loss_disc_real_0: 0.28972554206848145 (0.17343270507895558)
| > loss_disc_real_1: 0.2089729756116867 (0.21168066783432374)
| > loss_disc_real_2: 0.19422300159931183 (0.22756956812731902)
| > loss_disc_real_3: 0.18524032831192017 (0.22879229441173093)
| > loss_disc_real_4: 0.22998526692390442 (0.23901293958936418)
| > loss_disc_real_5: 0.21651652455329895 (0.2294204461208561)
| > loss_0: 2.72636342048645 (2.585255146026611)
| > grad_norm_0: tensor(10.7325, device='cuda:0') (tensor(18.8269, device='cuda:0'))
| > loss_gen: 1.8914556503295898 (2.2143673663748835)
| > loss_kl: 1.3622523546218872 (1.5990337100542877)
| > loss_feat: 6.261260509490967 (6.873181155450959)
| > loss_mel: 15.704572677612305 (15.52476387693171)
| > loss_duration: 1.4423136711120605 (1.4005243891761414)
| > amp_scaler: 256.0 (189.27318295739354)
| > loss_1: 26.661853790283203 (27.611870548181365)
| > grad_norm_1: tensor(315.1255, device='cuda:0') (tensor(253.6616, device='cuda:0'))
| > current_lr_0: 0.00019975014057813518
| > current_lr_1: 0.00019975014057813518
| > step_time: 0.7167 (0.6029710572465015)
| > loader_time: 0.0086 (0.007024334785633518)
--> TIME: 2025-05-14 11:54:08 -- STEP: 499/630 -- GLOBAL_STEP: 883800
| > loss_disc: 2.61417555809021 (2.582651842572168)
| > loss_disc_real_0: 0.1032891795039177 (0.17341528228206005)
| > loss_disc_real_1: 0.17175567150115967 (0.21132088828839377)
| > loss_disc_real_2: 0.1738840490579605 (0.22733980151479374)
| > loss_disc_real_3: 0.27104049921035767 (0.2289854468467957)
| > loss_disc_real_4: 0.2436918020248413 (0.23929718187552892)
| > loss_disc_real_5: 0.17385122179985046 (0.2281823643373105)
| > loss_0: 2.61417555809021 (2.582651842572168)
| > grad_norm_0: tensor(26.7197, device='cuda:0') (tensor(19.8994, device='cuda:0'))
| > loss_gen: 2.1473636627197266 (2.2202366320546987)
| > loss_kl: 1.7159128189086914 (1.5947489688296117)
| > loss_feat: 6.567203521728516 (6.865843732753593)
| > loss_mel: 15.784765243530273 (15.529598006743468)
| > loss_duration: 1.5048470497131348 (1.4139640221375978)
| > amp_scaler: 256.0 (202.64529058116239)
| > loss_1: 27.7200927734375 (27.624391418181823)
| > grad_norm_1: tensor(66.7834, device='cuda:0') (tensor(265.6888, device='cuda:0'))
| > current_lr_0: 0.00019975014057813518
| > current_lr_1: 0.00019975014057813518
| > step_time: 0.8108 (0.6331633312668729)
| > loader_time: 0.0113 (0.007542318237090636)
--> TIME: 2025-05-14 11:55:39 -- STEP: 599/630 -- GLOBAL_STEP: 883900
| > loss_disc: 2.662499189376831 (2.585578936368276)
| > loss_disc_real_0: 0.20336422324180603 (0.17345761450533076)
| > loss_disc_real_1: 0.2275066077709198 (0.2123175692155284)
| > loss_disc_real_2: 0.20345532894134521 (0.22788666300662172)
| > loss_disc_real_3: 0.23687027394771576 (0.22946046198250256)
| > loss_disc_real_4: 0.23243500292301178 (0.23952774046756986)
| > loss_disc_real_5: 0.26020124554634094 (0.22893084131666336)
| > loss_0: 2.662499189376831 (2.585578936368276)
| > grad_norm_0: tensor(10.3379, device='cuda:0') (tensor(20.0154, device='cuda:0'))
| > loss_gen: 2.1345369815826416 (2.2193235523115615)
| > loss_kl: 1.6114603281021118 (1.5957697604056786)
| > loss_feat: 6.492807388305664 (6.855512054615307)
| > loss_mel: 15.914438247680664 (15.530793428819049)
| > loss_duration: 1.4909552335739136 (1.4236902428389784)
| > amp_scaler: 256.0 (211.5525876460769)
| > loss_1: 27.64419937133789 (27.625089075410106)
| > grad_norm_1: tensor(240.1212, device='cuda:0') (tensor(264.8867, device='cuda:0'))
| > current_lr_0: 0.00019975014057813518
| > current_lr_1: 0.00019975014057813518
| > step_time: 0.975 (0.6770913489473877)
| > loader_time: 0.0136 (0.008179953579910615)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004942953586578369 (-0.0002932151158650713)
| > avg_loss_disc: 2.6834535201390586 (-0.0050798853238420705)
| > avg_loss_disc_real_0: 0.17610391477743784 (-0.001062591870625823)
| > avg_loss_disc_real_1: 0.2804714081188043 (+0.053182040651639284)
| > avg_loss_disc_real_2: 0.24566576878229776 (+0.02399078259865442)
| > avg_loss_disc_real_3: 0.238702525695165 (-0.00315727914373079)
| > avg_loss_disc_real_4: 0.24666460355122885 (-0.010286008318265288)
| > avg_loss_disc_real_5: 0.2190790002544721 (-0.048446429272492736)
| > avg_loss_0: 2.6834535201390586 (-0.0050798853238420705)
| > avg_loss_gen: 2.1230838100115457 (+0.05623196562131261)
| > avg_loss_kl: 1.7536093890666962 (-0.07137444615364075)
| > avg_loss_feat: 6.364585955937703 (-0.3124908208847046)
| > avg_loss_mel: 15.788508097330729 (+0.15163262685139856)
| > avg_loss_duration: 1.5375177562236786 (+0.009954432646433586)
| > avg_loss_1: 27.56730540593465 (-0.16604582468668738)
> EPOCH: 11/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 11:56:24)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 11:57:03 -- STEP: 69/630 -- GLOBAL_STEP: 884000
| > loss_disc: 2.678880453109741 (2.616738205370696)
| > loss_disc_real_0: 0.18669801950454712 (0.17202409993911136)
| > loss_disc_real_1: 0.22140488028526306 (0.21793784071569858)
| > loss_disc_real_2: 0.22421804070472717 (0.22859460137028625)
| > loss_disc_real_3: 0.21206186711788177 (0.2297762360261834)
| > loss_disc_real_4: 0.23161719739437103 (0.24290299026862436)
| > loss_disc_real_5: 0.2520788311958313 (0.23833643202332483)
| > loss_0: 2.678880453109741 (2.616738205370696)
| > grad_norm_0: tensor(9.4600, device='cuda:0') (tensor(16.7413, device='cuda:0'))
| > loss_gen: 2.1153578758239746 (2.1873715442159893)
| > loss_kl: 1.6255253553390503 (1.5667917728424072)
| > loss_feat: 6.258321762084961 (6.891404614932295)
| > loss_mel: 15.898225784301758 (15.542951597683672)
| > loss_duration: 1.4326725006103516 (1.4377189425454622)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.33010482788086 (27.6262383668319)
| > grad_norm_1: tensor(99.4749, device='cuda:0') (tensor(175.6596, device='cuda:0'))
| > current_lr_0: 0.00019972517181056292
| > current_lr_1: 0.00019972517181056292
| > step_time: 0.5232 (0.5349938282068225)
| > loader_time: 0.0052 (0.005171996959741565)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_884000.pth
--> TIME: 2025-05-14 11:58:02 -- STEP: 169/630 -- GLOBAL_STEP: 884100
| > loss_disc: 2.5358691215515137 (2.5927432951842544)
| > loss_disc_real_0: 0.10022391378879547 (0.16976661129287018)
| > loss_disc_real_1: 0.23908327519893646 (0.2158630939983052)
| > loss_disc_real_2: 0.26090797781944275 (0.22809961006133514)
| > loss_disc_real_3: 0.2505696415901184 (0.23073536748364126)
| > loss_disc_real_4: 0.26826804876327515 (0.24021572641719727)
| > loss_disc_real_5: 0.237457737326622 (0.23280147361684833)
| > loss_0: 2.5358691215515137 (2.5927432951842544)
| > grad_norm_0: tensor(18.2201, device='cuda:0') (tensor(17.8804, device='cuda:0'))
| > loss_gen: 2.264943838119507 (2.2121578539616955)
| > loss_kl: 1.5977495908737183 (1.5782042501946172)
| > loss_feat: 6.891236782073975 (6.8893540596820895)
| > loss_mel: 15.323399543762207 (15.5197583542773)
| > loss_duration: 1.4931495189666748 (1.3870768441251045)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.570478439331055 (27.586551271246734)
| > grad_norm_1: tensor(174.0382, device='cuda:0') (tensor(320.7776, device='cuda:0'))
| > current_lr_0: 0.00019972517181056292
| > current_lr_1: 0.00019972517181056292
| > step_time: 0.5577 (0.5481400024256059)
| > loader_time: 0.0065 (0.005757393921620746)
--> TIME: 2025-05-14 11:59:03 -- STEP: 269/630 -- GLOBAL_STEP: 884200
| > loss_disc: 2.6004109382629395 (2.592318234390486)
| > loss_disc_real_0: 0.10343347489833832 (0.16995569670288985)
| > loss_disc_real_1: 0.2299455851316452 (0.21488127610940472)
| > loss_disc_real_2: 0.24572591483592987 (0.22877275018665427)
| > loss_disc_real_3: 0.24973361194133759 (0.23079392646325123)
| > loss_disc_real_4: 0.23756961524486542 (0.23981416297446395)
| > loss_disc_real_5: 0.2566702663898468 (0.23396352504044218)
| > loss_0: 2.6004109382629395 (2.592318234390486)
| > grad_norm_0: tensor(32.5937, device='cuda:0') (tensor(18.5187, device='cuda:0'))
| > loss_gen: 2.1316349506378174 (2.211174574483284)
| > loss_kl: 1.7142695188522339 (1.5873506507908988)
| > loss_feat: 6.72344446182251 (6.860982995937304)
| > loss_mel: 15.850495338439941 (15.533393629421532)
| > loss_duration: 1.4615111351013184 (1.3924989469875633)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.88135528564453 (27.585400747986974)
| > grad_norm_1: tensor(297.5385, device='cuda:0') (tensor(291.6959, device='cuda:0'))
| > current_lr_0: 0.00019972517181056292
| > current_lr_1: 0.00019972517181056292
| > step_time: 0.6018 (0.563288384653822)
| > loader_time: 0.0082 (0.00624800348813649)
--> TIME: 2025-05-14 12:00:07 -- STEP: 369/630 -- GLOBAL_STEP: 884300
| > loss_disc: 2.722782850265503 (2.5898159907116143)
| > loss_disc_real_0: 0.16743190586566925 (0.1697630271880931)
| > loss_disc_real_1: 0.20802128314971924 (0.21389747760321706)
| > loss_disc_real_2: 0.2659345269203186 (0.22905053622354338)
| > loss_disc_real_3: 0.27041253447532654 (0.2301722941844444)
| > loss_disc_real_4: 0.2777172327041626 (0.23993102862906004)
| > loss_disc_real_5: 0.20184287428855896 (0.23196150782470135)
| > loss_0: 2.722782850265503 (2.5898159907116143)
| > grad_norm_0: tensor(9.4666, device='cuda:0') (tensor(19.8130, device='cuda:0'))
| > loss_gen: 2.1679978370666504 (2.21697894344485)
| > loss_kl: 1.5442323684692383 (1.5933860973290959)
| > loss_feat: 6.124301910400391 (6.855373422627848)
| > loss_mel: 15.831212043762207 (15.546840471303883)
| > loss_duration: 1.4299852848052979 (1.410718732086946)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.097728729248047 (27.6232976319021)
| > grad_norm_1: tensor(74.0428, device='cuda:0') (tensor(289.0562, device='cuda:0'))
| > current_lr_0: 0.00019972517181056292
| > current_lr_1: 0.00019972517181056292
| > step_time: 0.6547 (0.5824423947631507)
| > loader_time: 0.0086 (0.006827709797598159)
--> TIME: 2025-05-14 12:01:19 -- STEP: 469/630 -- GLOBAL_STEP: 884400
| > loss_disc: 2.7046666145324707 (2.5917866657029327)
| > loss_disc_real_0: 0.15252311527729034 (0.17032922818653118)
| > loss_disc_real_1: 0.2614155411720276 (0.2136111495527885)
| > loss_disc_real_2: 0.34025344252586365 (0.22811359951872306)
| > loss_disc_real_3: 0.25476503372192383 (0.2300992967096219)
| > loss_disc_real_4: 0.2465476244688034 (0.23975118839029055)
| > loss_disc_real_5: 0.2502236068248749 (0.2330055489723108)
| > loss_0: 2.7046666145324707 (2.5917866657029327)
| > grad_norm_0: tensor(11.0816, device='cuda:0') (tensor(18.6911, device='cuda:0'))
| > loss_gen: 2.1728668212890625 (2.2067499132807056)
| > loss_kl: 1.5857478380203247 (1.5997371381279757)
| > loss_feat: 6.103460788726807 (6.82404905595759)
| > loss_mel: 15.534159660339355 (15.534717773323628)
| > loss_duration: 1.498314619064331 (1.4107015742930262)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.894548416137695 (27.575955437698852)
| > grad_norm_1: tensor(140.9828, device='cuda:0') (tensor(256.8576, device='cuda:0'))
| > current_lr_0: 0.00019972517181056292
| > current_lr_1: 0.00019972517181056292
| > step_time: 0.7262 (0.6080312190025345)
| > loader_time: 0.0095 (0.007354912219017045)
--> TIME: 2025-05-14 12:02:43 -- STEP: 569/630 -- GLOBAL_STEP: 884500
| > loss_disc: 2.6410770416259766 (2.5905113911586817)
| > loss_disc_real_0: 0.19034382700920105 (0.17052233407702727)
| > loss_disc_real_1: 0.22495438158512115 (0.2134225544747233)
| > loss_disc_real_2: 0.24273420870304108 (0.22854941069870296)
| > loss_disc_real_3: 0.23613256216049194 (0.23040653458798077)
| > loss_disc_real_4: 0.23440320789813995 (0.2397958633403158)
| > loss_disc_real_5: 0.2465791255235672 (0.23184778055532954)
| > loss_0: 2.6410770416259766 (2.5905113911586817)
| > grad_norm_0: tensor(12.1286, device='cuda:0') (tensor(19.0029, device='cuda:0'))
| > loss_gen: 2.1631224155426025 (2.2069369659272966)
| > loss_kl: 1.5607396364212036 (1.6010719590111648)
| > loss_feat: 7.122102737426758 (6.793783448492495)
| > loss_mel: 15.265911102294922 (15.520684302586453)
| > loss_duration: 1.4555472135543823 (1.4206631902232112)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.56742286682129 (27.543139861631474)
| > grad_norm_1: tensor(76.9817, device='cuda:0') (tensor(251.9868, device='cuda:0'))
| > current_lr_0: 0.00019972517181056292
| > current_lr_1: 0.00019972517181056292
| > step_time: 0.8801 (0.6453771779742518)
| > loader_time: 0.0109 (0.007957087669305519)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_884500.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004794597625732422 (-0.00014835596084594727)
| > avg_loss_disc: 2.557807505130768 (-0.12564601500829076)
| > avg_loss_disc_real_0: 0.14896872453391552 (-0.027135190243522317)
| > avg_loss_disc_real_1: 0.19215047607819238 (-0.0883209320406119)
| > avg_loss_disc_real_2: 0.18734862158695856 (-0.0583171471953392)
| > avg_loss_disc_real_3: 0.23405992736419043 (-0.004642598330974579)
| > avg_loss_disc_real_4: 0.2578390588363012 (+0.011174455285072354)
| > avg_loss_disc_real_5: 0.228733508537213 (+0.009654508282740892)
| > avg_loss_0: 2.557807505130768 (-0.12564601500829076)
| > avg_loss_gen: 2.0631913542747498 (-0.05989245573679591)
| > avg_loss_kl: 1.6985377669334412 (-0.055071622133255005)
| > avg_loss_feat: 6.740227262179057 (+0.37564130624135394)
| > avg_loss_mel: 14.997974793116251 (-0.7905333042144775)
| > avg_loss_duration: 1.5250209669272106 (-0.012496789296468025)
| > avg_loss_1: 27.02495225270589 (-0.5423531532287598)
> BEST MODEL : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/best_model_884561.pth
> EPOCH: 12/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:04:02)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:04:24 -- STEP: 39/630 -- GLOBAL_STEP: 884600
| > loss_disc: 2.763981819152832 (2.5682885280022245)
| > loss_disc_real_0: 0.12843723595142365 (0.1677219330882415)
| > loss_disc_real_1: 0.26216545701026917 (0.22080894464101547)
| > loss_disc_real_2: 0.31982478499412537 (0.22823985723348764)
| > loss_disc_real_3: 0.2764507532119751 (0.2293832886677522)
| > loss_disc_real_4: 0.27843180298805237 (0.23703272602497003)
| > loss_disc_real_5: 0.23857061564922333 (0.22696920579824692)
| > loss_0: 2.763981819152832 (2.5682885280022245)
| > grad_norm_0: tensor(21.1845, device='cuda:0') (tensor(20.1578, device='cuda:0'))
| > loss_gen: 2.086263656616211 (2.253436871064015)
| > loss_kl: 1.7450308799743652 (1.5143474493271265)
| > loss_feat: 5.997071266174316 (7.138967318412585)
| > loss_mel: 15.511563301086426 (15.485749244689941)
| > loss_duration: 1.4358415603637695 (1.432421488639636)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.775772094726562 (27.824922170394505)
| > grad_norm_1: tensor(328.9138, device='cuda:0') (tensor(296.4546, device='cuda:0'))
| > current_lr_0: 0.0001997002061640866
| > current_lr_1: 0.0001997002061640866
| > step_time: 0.5341 (0.533401758242876)
| > loader_time: 0.0052 (0.005174007171239608)
--> TIME: 2025-05-14 12:05:19 -- STEP: 139/630 -- GLOBAL_STEP: 884700
| > loss_disc: 2.53690242767334 (2.5700868479639505)
| > loss_disc_real_0: 0.19141164422035217 (0.16702817241064935)
| > loss_disc_real_1: 0.22395898401737213 (0.21519536208763396)
| > loss_disc_real_2: 0.23445428907871246 (0.22738525700226103)
| > loss_disc_real_3: 0.24603784084320068 (0.2291958804825227)
| > loss_disc_real_4: 0.2672739028930664 (0.23858757274185152)
| > loss_disc_real_5: 0.24628518521785736 (0.22854290881174075)
| > loss_0: 2.53690242767334 (2.5700868479639505)
| > grad_norm_0: tensor(23.8217, device='cuda:0') (tensor(21.5583, device='cuda:0'))
| > loss_gen: 2.204418182373047 (2.243989546521962)
| > loss_kl: 1.5891884565353394 (1.581955298245382)
| > loss_feat: 5.459821701049805 (7.040067988333942)
| > loss_mel: 14.4974365234375 (15.514507341727937)
| > loss_duration: 1.445218801498413 (1.4095007824383197)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.19608497619629 (27.79002097699282)
| > grad_norm_1: tensor(380.0193, device='cuda:0') (tensor(304.7204, device='cuda:0'))
| > current_lr_0: 0.0001997002061640866
| > current_lr_1: 0.0001997002061640866
| > step_time: 0.5524 (0.5378072038828897)
| > loader_time: 0.0071 (0.005510606354089092)
--> TIME: 2025-05-14 12:06:20 -- STEP: 239/630 -- GLOBAL_STEP: 884800
| > loss_disc: 2.6035449504852295 (2.5674683000253347)
| > loss_disc_real_0: 0.29680174589157104 (0.16795312055234635)
| > loss_disc_real_1: 0.19797401130199432 (0.21283764164567492)
| > loss_disc_real_2: 0.23252125084400177 (0.22642739484998473)
| > loss_disc_real_3: 0.20823626220226288 (0.22772240738489638)
| > loss_disc_real_4: 0.24920544028282166 (0.23921567731571997)
| > loss_disc_real_5: 0.22677624225616455 (0.23008451227363683)
| > loss_0: 2.6035449504852295 (2.5674683000253347)
| > grad_norm_0: tensor(20.1778, device='cuda:0') (tensor(19.1741, device='cuda:0'))
| > loss_gen: 2.1884195804595947 (2.236340889870872)
| > loss_kl: 1.8028326034545898 (1.6047442991863234)
| > loss_feat: 7.242447376251221 (7.036347133843969)
| > loss_mel: 15.44315242767334 (15.51766929865881)
| > loss_duration: 1.4544017314910889 (1.3767328940674852)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.131254196166992 (27.77183462486107)
| > grad_norm_1: tensor(253.5353, device='cuda:0') (tensor(268.3881, device='cuda:0'))
| > current_lr_0: 0.0001997002061640866
| > current_lr_1: 0.0001997002061640866
| > step_time: 0.6259 (0.5616334661779044)
| > loader_time: 0.0082 (0.006066745295185423)
--> TIME: 2025-05-14 12:07:24 -- STEP: 339/630 -- GLOBAL_STEP: 884900
| > loss_disc: 2.555312156677246 (2.571364733321828)
| > loss_disc_real_0: 0.13925252854824066 (0.1682559563874496)
| > loss_disc_real_1: 0.21500788629055023 (0.21308374958755696)
| > loss_disc_real_2: 0.19399037957191467 (0.22741555767600866)
| > loss_disc_real_3: 0.23587672412395477 (0.22811935965114638)
| > loss_disc_real_4: 0.23042893409729004 (0.23970352535226705)
| > loss_disc_real_5: 0.19972403347492218 (0.22961468396812765)
| > loss_0: 2.555312156677246 (2.571364733321828)
| > grad_norm_0: tensor(12.6440, device='cuda:0') (tensor(18.2797, device='cuda:0'))
| > loss_gen: 2.234213352203369 (2.2269906006028175)
| > loss_kl: 1.546760082244873 (1.6047572147178086)
| > loss_feat: 7.346099853515625 (6.969138461931617)
| > loss_mel: 16.075281143188477 (15.524023666494363)
| > loss_duration: 1.4275009632110596 (1.4007120758382974)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.62985610961914 (27.72562212086004)
| > grad_norm_1: tensor(289.2224, device='cuda:0') (tensor(242.2399, device='cuda:0'))
| > current_lr_0: 0.0001997002061640866
| > current_lr_1: 0.0001997002061640866
| > step_time: 0.6865 (0.5822425247293654)
| > loader_time: 0.0094 (0.006581487908827517)
--> TIME: 2025-05-14 12:08:38 -- STEP: 439/630 -- GLOBAL_STEP: 885000
| > loss_disc: 2.491370916366577 (2.5788045575787097)
| > loss_disc_real_0: 0.09459161013364792 (0.1695458350495217)
| > loss_disc_real_1: 0.2107626348733902 (0.21402347515547193)
| > loss_disc_real_2: 0.23131747543811798 (0.22800016253847197)
| > loss_disc_real_3: 0.17960003018379211 (0.22923925647974558)
| > loss_disc_real_4: 0.2352275401353836 (0.23951468940883672)
| > loss_disc_real_5: 0.18408913910388947 (0.22813653531813133)
| > loss_0: 2.491370916366577 (2.5788045575787097)
| > grad_norm_0: tensor(33.6881, device='cuda:0') (tensor(19.3947, device='cuda:0'))
| > loss_gen: 2.2209556102752686 (2.222613448705655)
| > loss_kl: 1.651607871055603 (1.606145866096427)
| > loss_feat: 7.24776029586792 (6.922782721986532)
| > loss_mel: 15.903871536254883 (15.516976906118197)
| > loss_duration: 1.475872278213501 (1.4028833648338406)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.50006675720215 (27.671402368567247)
| > grad_norm_1: tensor(617.4520, device='cuda:0') (tensor(252.6434, device='cuda:0'))
| > current_lr_0: 0.0001997002061640866
| > current_lr_1: 0.0001997002061640866
| > step_time: 0.7455 (0.614229076272534)
| > loader_time: 0.01 (0.007122834885582021)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_885000.pth
--> TIME: 2025-05-14 12:10:03 -- STEP: 539/630 -- GLOBAL_STEP: 885100
| > loss_disc: 2.5153088569641113 (2.582812913052447)
| > loss_disc_real_0: 0.11160492897033691 (0.16999680682989135)
| > loss_disc_real_1: 0.22218012809753418 (0.21342576127879473)
| > loss_disc_real_2: 0.21904107928276062 (0.22830962236272603)
| > loss_disc_real_3: 0.23607313632965088 (0.22999418611208008)
| > loss_disc_real_4: 0.24963924288749695 (0.23936277296193675)
| > loss_disc_real_5: 0.23147204518318176 (0.22991274651105417)
| > loss_0: 2.5153088569641113 (2.582812913052447)
| > grad_norm_0: tensor(12.7924, device='cuda:0') (tensor(18.3799, device='cuda:0'))
| > loss_gen: 2.2771925926208496 (2.2126361881425995)
| > loss_kl: 1.7846060991287231 (1.6079690000785305)
| > loss_feat: 6.644561290740967 (6.858169362805991)
| > loss_mel: 15.226245880126953 (15.49857690206043)
| > loss_duration: 1.4587171077728271 (1.4136788201464794)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.391324996948242 (27.591030315477013)
| > grad_norm_1: tensor(124.3206, device='cuda:0') (tensor(231.4140, device='cuda:0'))
| > current_lr_0: 0.0001997002061640866
| > current_lr_1: 0.0001997002061640866
| > step_time: 0.8773 (0.6497818826523247)
| > loader_time: 0.0105 (0.007668808351421178)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.0051910877227783194 (+0.00039649009704589757)
| > avg_loss_disc: 2.6609639326731362 (+0.10315642754236842)
| > avg_loss_disc_real_0: 0.1488983022669951 (-7.042226692041686e-05)
| > avg_loss_disc_real_1: 0.2295402263601621 (+0.037389750281969725)
| > avg_loss_disc_real_2: 0.2663899337251981 (+0.07904131213823953)
| > avg_loss_disc_real_3: 0.2401322883864244 (+0.006072361022233963)
| > avg_loss_disc_real_4: 0.23128235464294752 (-0.02655670419335368)
| > avg_loss_disc_real_5: 0.2643620806435744 (+0.03562857210636142)
| > avg_loss_0: 2.6609639326731362 (+0.10315642754236842)
| > avg_loss_gen: 2.048099935054779 (-0.015091419219970703)
| > avg_loss_kl: 1.6365828116734822 (-0.06195495525995898)
| > avg_loss_feat: 6.365891059239705 (-0.374336202939352)
| > avg_loss_mel: 15.483813206354776 (+0.4858384132385254)
| > avg_loss_duration: 1.5297860105832417 (+0.004765043656031143)
| > avg_loss_1: 27.064173539479572 (+0.03922128677368164)
> EPOCH: 13/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:11:46)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:11:51 -- STEP: 9/630 -- GLOBAL_STEP: 885200
| > loss_disc: 2.4626641273498535 (2.465575509601169)
| > loss_disc_real_0: 0.16523875296115875 (0.16188357522090277)
| > loss_disc_real_1: 0.21069692075252533 (0.1955033557282554)
| > loss_disc_real_2: 0.2458229511976242 (0.21028228104114532)
| > loss_disc_real_3: 0.19290126860141754 (0.20618083079655966)
| > loss_disc_real_4: 0.22590917348861694 (0.23100743525558048)
| > loss_disc_real_5: 0.21218334138393402 (0.2356828467713462)
| > loss_0: 2.4626641273498535 (2.465575509601169)
| > grad_norm_0: tensor(8.8402, device='cuda:0') (tensor(27.4056, device='cuda:0'))
| > loss_gen: 2.362391948699951 (2.3588616847991943)
| > loss_kl: 1.225560188293457 (1.4179459545347426)
| > loss_feat: 7.935507774353027 (7.652467674679226)
| > loss_mel: 14.991159439086914 (15.539214028252495)
| > loss_duration: 1.4234752655029297 (1.414964000384013)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.938095092773438 (28.383453157212998)
| > grad_norm_1: tensor(252.0452, device='cuda:0') (tensor(375.3961, device='cuda:0'))
| > current_lr_0: 0.00019967524363831608
| > current_lr_1: 0.00019967524363831608
| > step_time: 0.5231 (0.5185727543301053)
| > loader_time: 0.0049 (0.004576894972059462)
--> TIME: 2025-05-14 12:12:46 -- STEP: 109/630 -- GLOBAL_STEP: 885300
| > loss_disc: 2.651432991027832 (2.561039204991192)
| > loss_disc_real_0: 0.1519671380519867 (0.16589504808460903)
| > loss_disc_real_1: 0.2486102283000946 (0.2144629167854239)
| > loss_disc_real_2: 0.22213779389858246 (0.22481837349200468)
| > loss_disc_real_3: 0.24767988920211792 (0.22690250170887064)
| > loss_disc_real_4: 0.2397587150335312 (0.23833036682474504)
| > loss_disc_real_5: 0.2353455275297165 (0.22587049308173154)
| > loss_0: 2.651432991027832 (2.561039204991192)
| > grad_norm_0: tensor(12.4971, device='cuda:0') (tensor(24.5425, device='cuda:0'))
| > loss_gen: 2.234114170074463 (2.259984959156141)
| > loss_kl: 1.7476603984832764 (1.5935800228643855)
| > loss_feat: 6.925206661224365 (7.073546339612489)
| > loss_mel: 15.389328002929688 (15.484761833050928)
| > loss_duration: 1.4649901390075684 (1.3924597042416214)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.76129913330078 (27.804332803148743)
| > grad_norm_1: tensor(59.1416, device='cuda:0') (tensor(321.2398, device='cuda:0'))
| > current_lr_0: 0.00019967524363831608
| > current_lr_1: 0.00019967524363831608
| > step_time: 0.5498 (0.5350920279091649)
| > loader_time: 0.0065 (0.005446543387316783)
--> TIME: 2025-05-14 12:13:47 -- STEP: 209/630 -- GLOBAL_STEP: 885400
| > loss_disc: 2.5555615425109863 (2.571830342260845)
| > loss_disc_real_0: 0.18167045712471008 (0.16770598998195246)
| > loss_disc_real_1: 0.1947217881679535 (0.2138305772719771)
| > loss_disc_real_2: 0.19245506823062897 (0.2247541812760978)
| > loss_disc_real_3: 0.2212258130311966 (0.22736130055913514)
| > loss_disc_real_4: 0.2184542715549469 (0.238456024935371)
| > loss_disc_real_5: 0.19774813950061798 (0.23113258960144373)
| > loss_0: 2.5555615425109863 (2.571830342260845)
| > grad_norm_0: tensor(22.5188, device='cuda:0') (tensor(21.1319, device='cuda:0'))
| > loss_gen: 2.2158753871917725 (2.235779422321959)
| > loss_kl: 1.732455849647522 (1.614722405324142)
| > loss_feat: 6.772927761077881 (6.976216916262248)
| > loss_mel: 16.742538452148438 (15.545727191359232)
| > loss_duration: 1.4608774185180664 (1.3609839506696857)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.92467498779297 (27.733429885937266)
| > grad_norm_1: tensor(184.9080, device='cuda:0') (tensor(276.6636, device='cuda:0'))
| > current_lr_0: 0.00019967524363831608
| > current_lr_1: 0.00019967524363831608
| > step_time: 0.6034 (0.5637198760749049)
| > loader_time: 0.0071 (0.0059745277514298)
--> TIME: 2025-05-14 12:14:50 -- STEP: 309/630 -- GLOBAL_STEP: 885500
| > loss_disc: 2.511476993560791 (2.576811675500715)
| > loss_disc_real_0: 0.1775956004858017 (0.1697829640364956)
| > loss_disc_real_1: 0.19470460712909698 (0.21339428149959416)
| > loss_disc_real_2: 0.18265634775161743 (0.2244476784973083)
| > loss_disc_real_3: 0.1998147964477539 (0.2284088978682521)
| > loss_disc_real_4: 0.23221470415592194 (0.23820158255717516)
| > loss_disc_real_5: 0.22949279844760895 (0.2321302641460425)
| > loss_0: 2.511476993560791 (2.576811675500715)
| > grad_norm_0: tensor(11.0397, device='cuda:0') (tensor(19.7746, device='cuda:0'))
| > loss_gen: 2.196183681488037 (2.2236699961535757)
| > loss_kl: 1.6544864177703857 (1.609632953470965)
| > loss_feat: 6.476459503173828 (6.919362403042494)
| > loss_mel: 15.29267406463623 (15.577699192133537)
| > loss_duration: 1.411482334136963 (1.391888761597544)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.031286239624023 (27.72225333031713)
| > grad_norm_1: tensor(43.9727, device='cuda:0') (tensor(246.9501, device='cuda:0'))
| > current_lr_0: 0.00019967524363831608
| > current_lr_1: 0.00019967524363831608
| > step_time: 0.6329 (0.5828710520537533)
| > loader_time: 0.0083 (0.006535887332410099)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_885500.pth
--> TIME: 2025-05-14 12:16:03 -- STEP: 409/630 -- GLOBAL_STEP: 885600
| > loss_disc: 2.3304011821746826 (2.5730755795476488)
| > loss_disc_real_0: 0.13971199095249176 (0.1710647523293869)
| > loss_disc_real_1: 0.15258252620697021 (0.21245730524395381)
| > loss_disc_real_2: 0.22354058921337128 (0.22505166776897273)
| > loss_disc_real_3: 0.20964165031909943 (0.22791371026365564)
| > loss_disc_real_4: 0.22628401219844818 (0.23907064815896648)
| > loss_disc_real_5: 0.26859521865844727 (0.2296888278136918)
| > loss_0: 2.3304011821746826 (2.5730755795476488)
| > grad_norm_0: tensor(43.2699, device='cuda:0') (tensor(21.5438, device='cuda:0'))
| > loss_gen: 2.632258176803589 (2.238142419269443)
| > loss_kl: 1.7899531126022339 (1.6140901004772605)
| > loss_feat: 7.898254871368408 (6.92395017316114)
| > loss_mel: 15.159200668334961 (15.616958669461948)
| > loss_duration: 1.480552315711975 (1.3949417904711585)
| > amp_scaler: 256.0 (256.62591687041555)
| > loss_1: 28.96021842956543 (27.788083172077656)
| > grad_norm_1: tensor(759.9622, device='cuda:0') (tensor(267.8400, device='cuda:0'))
| > current_lr_0: 0.00019967524363831608
| > current_lr_1: 0.00019967524363831608
| > step_time: 0.7084 (0.6064427808327886)
| > loader_time: 0.0084 (0.007065184250437541)
--> TIME: 2025-05-14 12:17:19 -- STEP: 509/630 -- GLOBAL_STEP: 885700
| > loss_disc: 2.6787991523742676 (2.5738420931435755)
| > loss_disc_real_0: 0.27554529905319214 (0.17063130865748136)
| > loss_disc_real_1: 0.25057747960090637 (0.2127773158676732)
| > loss_disc_real_2: 0.26729968190193176 (0.22555428154927573)
| > loss_disc_real_3: 0.19335362315177917 (0.22860534421821474)
| > loss_disc_real_4: 0.27297651767730713 (0.2394700216345328)
| > loss_disc_real_5: 0.2653614282608032 (0.22951014178909346)
| > loss_0: 2.6787991523742676 (2.5738420931435755)
| > grad_norm_0: tensor(17.8897, device='cuda:0') (tensor(21.5979, device='cuda:0'))
| > loss_gen: 2.1333200931549072 (2.237065792083743)
| > loss_kl: 1.8236888647079468 (1.6110793759640167)
| > loss_feat: 6.485538005828857 (6.891522437509713)
| > loss_mel: 15.62446117401123 (15.604280707878308)
| > loss_duration: 1.4566161632537842 (1.4082876804535422)
| > amp_scaler: 256.0 (256.50294695481307)
| > loss_1: 27.523624420166016 (27.752236008409902)
| > grad_norm_1: tensor(124.3000, device='cuda:0') (tensor(265.1223, device='cuda:0'))
| > current_lr_0: 0.00019967524363831608
| > current_lr_1: 0.00019967524363831608
| > step_time: 0.8671 (0.6351334697371138)
| > loader_time: 0.0104 (0.007577636152915728)
--> TIME: 2025-05-14 12:18:52 -- STEP: 609/630 -- GLOBAL_STEP: 885800
| > loss_disc: 2.6608455181121826 (2.5747817604021117)
| > loss_disc_real_0: 0.26173755526542664 (0.1703338851824965)
| > loss_disc_real_1: 0.20325879752635956 (0.21199882923578003)
| > loss_disc_real_2: 0.2144782990217209 (0.22619501999250577)
| > loss_disc_real_3: 0.2691251039505005 (0.22849306532706337)
| > loss_disc_real_4: 0.26970934867858887 (0.23910473000827093)
| > loss_disc_real_5: 0.20763996243476868 (0.23056393467831884)
| > loss_0: 2.6608455181121826 (2.5747817604021117)
| > grad_norm_0: tensor(13.5756, device='cuda:0') (tensor(20.8121, device='cuda:0'))
| > loss_gen: 2.3565917015075684 (2.229768458845582)
| > loss_kl: 1.5846567153930664 (1.6132372457209876)
| > loss_feat: 6.405854225158691 (6.859130121804223)
| > loss_mel: 16.06343650817871 (15.59259310536001)
| > loss_duration: 1.4844671487808228 (1.418787815496447)
| > amp_scaler: 256.0 (256.42036124794714)
| > loss_1: 27.89500617980957 (27.713516758384774)
| > grad_norm_1: tensor(175.3095, device='cuda:0') (tensor(250.8929, device='cuda:0'))
| > current_lr_0: 0.00019967524363831608
| > current_lr_1: 0.00019967524363831608
| > step_time: 1.0706 (0.6797729008303476)
| > loader_time: 0.0154 (0.00822519355611065)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005126059055328369 (-6.50286674499503e-05)
| > avg_loss_disc: 2.7093708515167236 (+0.04840691884358739)
| > avg_loss_disc_real_0: 0.12843917993207773 (-0.020459122334917368)
| > avg_loss_disc_real_1: 0.18193157141407332 (-0.04760865494608879)
| > avg_loss_disc_real_2: 0.22413905709981918 (-0.04225087662537891)
| > avg_loss_disc_real_3: 0.22696412975589433 (-0.013168158630530058)
| > avg_loss_disc_real_4: 0.2359038069844246 (+0.004621452341477067)
| > avg_loss_disc_real_5: 0.22522488112250963 (-0.039137199521064786)
| > avg_loss_0: 2.7093708515167236 (+0.04840691884358739)
| > avg_loss_gen: 1.8399384915828705 (-0.20816144347190857)
| > avg_loss_kl: 1.7054350972175598 (+0.06885228554407763)
| > avg_loss_feat: 6.654959479967753 (+0.2890684207280483)
| > avg_loss_mel: 15.696065664291382 (+0.2122524579366054)
| > avg_loss_duration: 1.5195974310239155 (-0.010188579559326172)
| > avg_loss_1: 27.415995756785076 (+0.35182221730550367)
> EPOCH: 14/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:19:26)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:20:10 -- STEP: 79/630 -- GLOBAL_STEP: 885900
| > loss_disc: 2.8201327323913574 (2.586397985868816)
| > loss_disc_real_0: 0.1421985775232315 (0.16526290425394158)
| > loss_disc_real_1: 0.2609029710292816 (0.21580207225265383)
| > loss_disc_real_2: 0.33797866106033325 (0.2299657224477092)
| > loss_disc_real_3: 0.31356728076934814 (0.2293207017304022)
| > loss_disc_real_4: 0.3177231252193451 (0.2403133151274693)
| > loss_disc_real_5: 0.2512146830558777 (0.2287988349606719)
| > loss_0: 2.8201327323913574 (2.586397985868816)
| > grad_norm_0: tensor(22.3192, device='cuda:0') (tensor(22.5841, device='cuda:0'))
| > loss_gen: 2.1935250759124756 (2.2243895047827618)
| > loss_kl: 1.6877334117889404 (1.5817777823798265)
| > loss_feat: 6.601104736328125 (7.04671932775763)
| > loss_mel: 16.34673309326172 (15.596877918967717)
| > loss_duration: 1.460214376449585 (1.43852832196634)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.289310455322266 (27.888292819638796)
| > grad_norm_1: tensor(155.7949, device='cuda:0') (tensor(279.5413, device='cuda:0'))
| > current_lr_0: 0.0001996502842328613
| > current_lr_1: 0.0001996502842328613
| > step_time: 0.5343 (0.529182536692559)
| > loader_time: 0.0054 (0.005442438246328619)
--> TIME: 2025-05-14 12:21:09 -- STEP: 179/630 -- GLOBAL_STEP: 886000
| > loss_disc: 2.5658884048461914 (2.5822805172904237)
| > loss_disc_real_0: 0.15086740255355835 (0.16624218258777804)
| > loss_disc_real_1: 0.2376812845468521 (0.21336636067935208)
| > loss_disc_real_2: 0.20542874932289124 (0.2306045770811635)
| > loss_disc_real_3: 0.25740358233451843 (0.22831376820969182)
| > loss_disc_real_4: 0.21081732213497162 (0.23798524559210132)
| > loss_disc_real_5: 0.21048976480960846 (0.22952288946958893)
| > loss_0: 2.5658884048461914 (2.5822805172904237)
| > grad_norm_0: tensor(9.2602, device='cuda:0') (tensor(21.6135, device='cuda:0'))
| > loss_gen: 2.353459358215332 (2.214914408475993)
| > loss_kl: 1.6327491998672485 (1.6341353228638291)
| > loss_feat: 8.066092491149902 (7.018603668532558)
| > loss_mel: 15.803858757019043 (15.59798507051095)
| > loss_duration: 1.4576807022094727 (1.385781821591894)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.313838958740234 (27.85142025867654)
| > grad_norm_1: tensor(196.2119, device='cuda:0') (tensor(286.2505, device='cuda:0'))
| > current_lr_0: 0.0001996502842328613
| > current_lr_1: 0.0001996502842328613
| > step_time: 0.5749 (0.5558316467860555)
| > loader_time: 0.007 (0.005936175085312825)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_886000.pth
--> TIME: 2025-05-14 12:22:13 -- STEP: 279/630 -- GLOBAL_STEP: 886100
| > loss_disc: 2.7149240970611572 (2.5882875842432824)
| > loss_disc_real_0: 0.19704517722129822 (0.16902326883274163)
| > loss_disc_real_1: 0.2127717286348343 (0.21481611312610707)
| > loss_disc_real_2: 0.18765975534915924 (0.2292893273108322)
| > loss_disc_real_3: 0.24077259004116058 (0.22701179564640087)
| > loss_disc_real_4: 0.2700187861919403 (0.24009599715578087)
| > loss_disc_real_5: 0.29839736223220825 (0.23107124325622366)
| > loss_0: 2.7149240970611572 (2.5882875842432824)
| > grad_norm_0: tensor(9.8481, device='cuda:0') (tensor(21.6431, device='cuda:0'))
| > loss_gen: 2.051884651184082 (2.213821015904881)
| > loss_kl: 1.6524511575698853 (1.6372078836605115)
| > loss_feat: 6.422399997711182 (6.944630166535736)
| > loss_mel: 16.317947387695312 (15.656827742053617)
| > loss_duration: 1.4806774854660034 (1.3908400864584045)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.92535972595215 (27.843326896749517)
| > grad_norm_1: tensor(66.6394, device='cuda:0') (tensor(275.3741, device='cuda:0'))
| > current_lr_0: 0.0001996502842328613
| > current_lr_1: 0.0001996502842328613
| > step_time: 0.6349 (0.5730287174170161)
| > loader_time: 0.0084 (0.006426401035760037)
--> TIME: 2025-05-14 12:23:20 -- STEP: 379/630 -- GLOBAL_STEP: 886200
| > loss_disc: 2.648956298828125 (2.5872765134695666)
| > loss_disc_real_0: 0.16981440782546997 (0.16926793838632453)
| > loss_disc_real_1: 0.15014101564884186 (0.2133288282635659)
| > loss_disc_real_2: 0.22353559732437134 (0.2286996146698426)
| > loss_disc_real_3: 0.22865600883960724 (0.22788137964176944)
| > loss_disc_real_4: 0.23394666612148285 (0.24022799101228134)
| > loss_disc_real_5: 0.235648974776268 (0.23157472704048207)
| > loss_0: 2.648956298828125 (2.5872765134695666)
| > grad_norm_0: tensor(31.0091, device='cuda:0') (tensor(20.9807, device='cuda:0'))
| > loss_gen: 2.2165770530700684 (2.2061728355437924)
| > loss_kl: 1.7611721754074097 (1.6307365475984237)
| > loss_feat: 7.392507076263428 (6.875703404006354)
| > loss_mel: 15.803804397583008 (15.641702166333362)
| > loss_duration: 1.4895012378692627 (1.4087954193432286)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.663562774658203 (27.763110359614632)
| > grad_norm_1: tensor(222.8993, device='cuda:0') (tensor(260.6510, device='cuda:0'))
| > current_lr_0: 0.0001996502842328613
| > current_lr_1: 0.0001996502842328613
| > step_time: 0.6809 (0.5943922876997176)
| > loader_time: 0.0087 (0.006945388612772354)
--> TIME: 2025-05-14 12:24:32 -- STEP: 479/630 -- GLOBAL_STEP: 886300
| > loss_disc: 2.5526700019836426 (2.5847730532070803)
| > loss_disc_real_0: 0.11484114080667496 (0.16928403998777614)
| > loss_disc_real_1: 0.22475802898406982 (0.2136101659721771)
| > loss_disc_real_2: 0.22396859526634216 (0.227931973145252)
| > loss_disc_real_3: 0.19919507205486298 (0.22809914283314428)
| > loss_disc_real_4: 0.2678989768028259 (0.23992421025398628)
| > loss_disc_real_5: 0.30342698097229004 (0.2308112381333349)
| > loss_0: 2.5526700019836426 (2.5847730532070803)
| > grad_norm_0: tensor(47.3099, device='cuda:0') (tensor(21.4174, device='cuda:0'))
| > loss_gen: 2.3915112018585205 (2.2097438949632746)
| > loss_kl: 1.6384249925613403 (1.6231023986553599)
| > loss_feat: 7.391449451446533 (6.8457007746606875)
| > loss_mel: 15.496665954589844 (15.613424102050526)
| > loss_duration: 1.4675326347351074 (1.408568128165721)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.38558578491211 (27.700539276346035)
| > grad_norm_1: tensor(354.9580, device='cuda:0') (tensor(265.3764, device='cuda:0'))
| > current_lr_0: 0.0001996502842328613
| > current_lr_1: 0.0001996502842328613
| > step_time: 0.7399 (0.6175135695113028)
| > loader_time: 0.011 (0.007483981596403181)
--> TIME: 2025-05-14 12:25:55 -- STEP: 579/630 -- GLOBAL_STEP: 886400
| > loss_disc: 2.7336974143981934 (2.5847058831513037)
| > loss_disc_real_0: 0.20301011204719543 (0.16984132238517352)
| > loss_disc_real_1: 0.2269745022058487 (0.2132589089618241)
| > loss_disc_real_2: 0.19036339223384857 (0.22771889763998446)
| > loss_disc_real_3: 0.199787437915802 (0.22790767916434787)
| > loss_disc_real_4: 0.1979357898235321 (0.2396811348014545)
| > loss_disc_real_5: 0.2181648463010788 (0.2311877641756094)
| > loss_0: 2.7336974143981934 (2.5847058831513037)
| > grad_norm_0: tensor(9.7366, device='cuda:0') (tensor(20.9015, device='cuda:0'))
| > loss_gen: 2.0012638568878174 (2.2075399889229486)
| > loss_kl: 1.6757537126541138 (1.6234749003807285)
| > loss_feat: 6.652374267578125 (6.824316276787478)
| > loss_mel: 15.36051082611084 (15.61795308964652)
| > loss_duration: 1.4851713180541992 (1.4187875745210003)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.17507553100586 (27.69207182572913)
| > grad_norm_1: tensor(170.2027, device='cuda:0') (tensor(253.5978, device='cuda:0'))
| > current_lr_0: 0.0001996502842328613
| > current_lr_1: 0.0001996502842328613
| > step_time: 0.8984 (0.6506772222502453)
| > loader_time: 0.0114 (0.008078420718099171)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005083858966827393 (-4.220008850097656e-05)
| > avg_loss_disc: 2.7636141180992126 (+0.054243266582489014)
| > avg_loss_disc_real_0: 0.1564705471197764 (+0.028031367187698664)
| > avg_loss_disc_real_1: 0.25150263806184137 (+0.06957106664776805)
| > avg_loss_disc_real_2: 0.26089292640487355 (+0.036753869305054365)
| > avg_loss_disc_real_3: 0.29326031481226283 (+0.0662961850563685)
| > avg_loss_disc_real_4: 0.2659508449335893 (+0.03004703794916469)
| > avg_loss_disc_real_5: 0.2536012791097164 (+0.028376397987206786)
| > avg_loss_0: 2.7636141180992126 (+0.054243266582489014)
| > avg_loss_gen: 2.1175711353619895 (+0.277632643779119)
| > avg_loss_kl: 1.6776643494764965 (-0.027770747741063362)
| > avg_loss_feat: 6.814855297406514 (+0.1598958174387608)
| > avg_loss_mel: 15.7494109471639 (+0.053345282872518496)
| > avg_loss_duration: 1.5226512849330902 (+0.0030538539091746753)
| > avg_loss_1: 27.8821538289388 (+0.46615807215372485)
> EPOCH: 15/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:26:57)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:27:23 -- STEP: 49/630 -- GLOBAL_STEP: 886500
| > loss_disc: 2.548855781555176 (2.545114969720646)
| > loss_disc_real_0: 0.2467813640832901 (0.1674837664682038)
| > loss_disc_real_1: 0.24433402717113495 (0.21855146696372907)
| > loss_disc_real_2: 0.21555599570274353 (0.22697971639584522)
| > loss_disc_real_3: 0.2022068053483963 (0.22870403710676698)
| > loss_disc_real_4: 0.25544223189353943 (0.23922632360944943)
| > loss_disc_real_5: 0.26061293482780457 (0.21603344061544963)
| > loss_0: 2.548855781555176 (2.545114969720646)
| > grad_norm_0: tensor(25.1396, device='cuda:0') (tensor(19.9309, device='cuda:0'))
| > loss_gen: 2.29929256439209 (2.2893909142941844)
| > loss_kl: 1.5461143255233765 (1.5368111680965035)
| > loss_feat: 7.177511692047119 (7.145213350957754)
| > loss_mel: 15.046630859375 (15.573283682064135)
| > loss_duration: 1.4648265838623047 (1.4353715862546645)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.53437614440918 (27.980070814794423)
| > grad_norm_1: tensor(184.2177, device='cuda:0') (tensor(274.7009, device='cuda:0'))
| > current_lr_0: 0.00019962532794733217
| > current_lr_1: 0.00019962532794733217
| > step_time: 0.5322 (0.5179532206788352)
| > loader_time: 0.0056 (0.004985390877237125)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_886500.pth
--> TIME: 2025-05-14 12:28:23 -- STEP: 149/630 -- GLOBAL_STEP: 886600
| > loss_disc: 2.5771162509918213 (2.572962506505466)
| > loss_disc_real_0: 0.2151453047990799 (0.16799434269434657)
| > loss_disc_real_1: 0.14614242315292358 (0.21579696208038587)
| > loss_disc_real_2: 0.25157856941223145 (0.22919810448316918)
| > loss_disc_real_3: 0.24491466581821442 (0.22844175894388422)
| > loss_disc_real_4: 0.20430012047290802 (0.23876099708496323)
| > loss_disc_real_5: 0.19876350462436676 (0.2239793198520705)
| > loss_0: 2.5771162509918213 (2.572962506505466)
| > grad_norm_0: tensor(16.5817, device='cuda:0') (tensor(20.6717, device='cuda:0'))
| > loss_gen: 2.1446616649627686 (2.2450496246350697)
| > loss_kl: 1.7574779987335205 (1.5873308865816005)
| > loss_feat: 7.242183208465576 (6.988911087880998)
| > loss_mel: 16.08262825012207 (15.493016262182453)
| > loss_duration: 1.4229449033737183 (1.3705260825637202)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.6498966217041 (27.684834025850233)
| > grad_norm_1: tensor(410.6871, device='cuda:0') (tensor(289.4895, device='cuda:0'))
| > current_lr_0: 0.00019962532794733217
| > current_lr_1: 0.00019962532794733217
| > step_time: 0.5593 (0.5406352225566069)
| > loader_time: 0.0063 (0.005580121238759698)
--> TIME: 2025-05-14 12:29:23 -- STEP: 249/630 -- GLOBAL_STEP: 886700
| > loss_disc: 2.3599419593811035 (2.572367424945754)
| > loss_disc_real_0: 0.19344991445541382 (0.1690989119341096)
| > loss_disc_real_1: 0.18329238891601562 (0.21507471716068835)
| > loss_disc_real_2: 0.21175450086593628 (0.2293098411526546)
| > loss_disc_real_3: 0.20994052290916443 (0.2272743450470239)
| > loss_disc_real_4: 0.23611000180244446 (0.23788367929946946)
| > loss_disc_real_5: 0.17887508869171143 (0.22361589594179368)
| > loss_0: 2.3599419593811035 (2.572367424945754)
| > grad_norm_0: tensor(15.8453, device='cuda:0') (tensor(21.4941, device='cuda:0'))
| > loss_gen: 2.408759117126465 (2.246497108754383)
| > loss_kl: 1.4837905168533325 (1.5961554938530826)
| > loss_feat: 7.051994323730469 (6.9737948241482774)
| > loss_mel: 14.707138061523438 (15.532015172353232)
| > loss_duration: 1.4301645755767822 (1.3833689105558582)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.08184814453125 (27.731831577408265)
| > grad_norm_1: tensor(501.5488, device='cuda:0') (tensor(299.2126, device='cuda:0'))
| > current_lr_0: 0.00019962532794733217
| > current_lr_1: 0.00019962532794733217
| > step_time: 0.6014 (0.559791208749794)
| > loader_time: 0.0076 (0.0060632879954265265)
--> TIME: 2025-05-14 12:30:28 -- STEP: 349/630 -- GLOBAL_STEP: 886800
| > loss_disc: 2.567476987838745 (2.5771886885678503)
| > loss_disc_real_0: 0.23791305720806122 (0.17000058274129073)
| > loss_disc_real_1: 0.23616929352283478 (0.2139391797490653)
| > loss_disc_real_2: 0.24059385061264038 (0.22827650935397106)
| > loss_disc_real_3: 0.24128906428813934 (0.22876454514043038)
| > loss_disc_real_4: 0.2703116834163666 (0.23925282509415743)
| > loss_disc_real_5: 0.2342381477355957 (0.2252796941508878)
| > loss_0: 2.567476987838745 (2.5771886885678503)
| > grad_norm_0: tensor(13.7893, device='cuda:0') (tensor(21.3674, device='cuda:0'))
| > loss_gen: 2.1972978115081787 (2.232710318100828)
| > loss_kl: 1.521230697631836 (1.6003914653059406)
| > loss_feat: 6.651496410369873 (6.896436330582146)
| > loss_mel: 15.129722595214844 (15.533544797268842)
| > loss_duration: 1.4238643646240234 (1.4045243457941754)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.923612594604492 (27.6676073320274)
| > grad_norm_1: tensor(325.4695, device='cuda:0') (tensor(289.5601, device='cuda:0'))
| > current_lr_0: 0.00019962532794733217
| > current_lr_1: 0.00019962532794733217
| > step_time: 0.6664 (0.5828046511783985)
| > loader_time: 0.0092 (0.006621205021112218)
--> TIME: 2025-05-14 12:31:42 -- STEP: 449/630 -- GLOBAL_STEP: 886900
| > loss_disc: 2.705989360809326 (2.587277611539198)
| > loss_disc_real_0: 0.24988456070423126 (0.17136856365973813)
| > loss_disc_real_1: 0.231417715549469 (0.21439444603925292)
| > loss_disc_real_2: 0.24847924709320068 (0.22929106934829915)
| > loss_disc_real_3: 0.22963199019432068 (0.22993661008592703)
| > loss_disc_real_4: 0.21741093695163727 (0.23951068799320469)
| > loss_disc_real_5: 0.2811969220638275 (0.22846879275777027)
| > loss_0: 2.705989360809326 (2.587277611539198)
| > grad_norm_0: tensor(11.7888, device='cuda:0') (tensor(20.4515, device='cuda:0'))
| > loss_gen: 2.2736518383026123 (2.219600769618569)
| > loss_kl: 1.5499913692474365 (1.6001018982687611)
| > loss_feat: 5.406331539154053 (6.826806637651405)
| > loss_mel: 15.123176574707031 (15.527543917530629)
| > loss_duration: 1.4369227886199951 (1.4049085864510995)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.790071487426758 (27.57896184602665)
| > grad_norm_1: tensor(170.8358, device='cuda:0') (tensor(269.0911, device='cuda:0'))
| > current_lr_0: 0.00019962532794733217
| > current_lr_1: 0.00019962532794733217
| > step_time: 0.7057 (0.6151517733168232)
| > loader_time: 0.0092 (0.007191254991731027)
--> TIME: 2025-05-14 12:33:02 -- STEP: 549/630 -- GLOBAL_STEP: 887000
| > loss_disc: 2.6228814125061035 (2.5921540916074597)
| > loss_disc_real_0: 0.17930692434310913 (0.17282070712150768)
| > loss_disc_real_1: 0.13240420818328857 (0.21487536103564753)
| > loss_disc_real_2: 0.19940029084682465 (0.2296085788415429)
| > loss_disc_real_3: 0.18404202163219452 (0.23039243469364223)
| > loss_disc_real_4: 0.28140631318092346 (0.2393315623095344)
| > loss_disc_real_5: 0.23174382746219635 (0.22787622548300496)
| > loss_0: 2.6228814125061035 (2.5921540916074597)
| > grad_norm_0: tensor(39.8988, device='cuda:0') (tensor(21.1133, device='cuda:0'))
| > loss_gen: 2.2301316261291504 (2.215504864525923)
| > loss_kl: 1.4824739694595337 (1.6030279824642533)
| > loss_feat: 7.6162519454956055 (6.786246865173506)
| > loss_mel: 16.141599655151367 (15.519052020839004)
| > loss_duration: 1.4764764308929443 (1.4156719474410315)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.94693374633789 (27.539503677729485)
| > grad_norm_1: tensor(577.6204, device='cuda:0') (tensor(269.8983, device='cuda:0'))
| > current_lr_0: 0.00019962532794733217
| > current_lr_1: 0.00019962532794733217
| > step_time: 0.883 (0.6461484414849344)
| > loader_time: 0.0138 (0.007757374497710682)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_887000.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.00494140386581421 (-0.00014245510101318273)
| > avg_loss_disc: 2.6272661685943604 (-0.1363479495048523)
| > avg_loss_disc_real_0: 0.17897279312213263 (+0.02250224600235623)
| > avg_loss_disc_real_1: 0.21402526025970778 (-0.03747737780213359)
| > avg_loss_disc_real_2: 0.27699776738882065 (+0.0161048409839471)
| > avg_loss_disc_real_3: 0.25850720206896466 (-0.034753112743298176)
| > avg_loss_disc_real_4: 0.2728126347064972 (+0.006861789772907911)
| > avg_loss_disc_real_5: 0.24803300450245538 (-0.005568274607261031)
| > avg_loss_0: 2.6272661685943604 (-0.1363479495048523)
| > avg_loss_gen: 2.2105817596117654 (+0.09301062424977591)
| > avg_loss_kl: 1.7033178210258484 (+0.025653471549351936)
| > avg_loss_feat: 6.209191004435222 (-0.6056642929712925)
| > avg_loss_mel: 15.330597400665283 (-0.41881354649861713)
| > avg_loss_duration: 1.5214268267154694 (-0.0012244582176208496)
| > avg_loss_1: 26.975114345550537 (-0.9070394833882638)
> EPOCH: 16/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:34:37)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:34:48 -- STEP: 19/630 -- GLOBAL_STEP: 887100
| > loss_disc: 2.706984758377075 (2.6372329937784293)
| > loss_disc_real_0: 0.1465105414390564 (0.1688332298868581)
| > loss_disc_real_1: 0.2944331467151642 (0.21537950713383525)
| > loss_disc_real_2: 0.2256295084953308 (0.2292730572976564)
| > loss_disc_real_3: 0.15533585846424103 (0.23943039774894714)
| > loss_disc_real_4: 0.22621484100818634 (0.2563487863854358)
| > loss_disc_real_5: 0.2284860908985138 (0.2499271199891442)
| > loss_0: 2.706984758377075 (2.6372329937784293)
| > grad_norm_0: tensor(8.6218, device='cuda:0') (tensor(16.1199, device='cuda:0'))
| > loss_gen: 1.9953391551971436 (2.172485778206273)
| > loss_kl: 1.7241029739379883 (1.4950682364012067)
| > loss_feat: 7.936678886413574 (6.838115215301514)
| > loss_mel: 16.07206153869629 (15.727952103865775)
| > loss_duration: 1.401944875717163 (1.4172737661160921)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.130126953125 (27.650895068519993)
| > grad_norm_1: tensor(136.9735, device='cuda:0') (tensor(182.7776, device='cuda:0'))
| > current_lr_0: 0.00019960037478133875
| > current_lr_1: 0.00019960037478133875
| > step_time: 0.5155 (0.5188208755693937)
| > loader_time: 0.0049 (0.005140768854241622)
--> TIME: 2025-05-14 12:35:43 -- STEP: 119/630 -- GLOBAL_STEP: 887200
| > loss_disc: 2.415386199951172 (2.6119349884385836)
| > loss_disc_real_0: 0.1527746021747589 (0.17006184523846926)
| > loss_disc_real_1: 0.1519836187362671 (0.21378012840487376)
| > loss_disc_real_2: 0.217324361205101 (0.22858899631420104)
| > loss_disc_real_3: 0.2212873101234436 (0.23325328441227183)
| > loss_disc_real_4: 0.24494829773902893 (0.2411991758506839)
| > loss_disc_real_5: 0.18569672107696533 (0.23952305467188859)
| > loss_0: 2.415386199951172 (2.6119349884385836)
| > grad_norm_0: tensor(9.5264, device='cuda:0') (tensor(13.9824, device='cuda:0'))
| > loss_gen: 2.4184131622314453 (2.1722052477988876)
| > loss_kl: 1.5501067638397217 (1.5699063198907033)
| > loss_feat: 7.144192218780518 (6.783076146069695)
| > loss_mel: 15.31580638885498 (15.55987749981279)
| > loss_duration: 1.4987539052963257 (1.402452083194957)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.92727279663086 (27.48751725268965)
| > grad_norm_1: tensor(226.8189, device='cuda:0') (tensor(158.7488, device='cuda:0'))
| > current_lr_0: 0.00019960037478133875
| > current_lr_1: 0.00019960037478133875
| > step_time: 0.5597 (0.5337528180675347)
| > loader_time: 0.0065 (0.005526368357554203)
--> TIME: 2025-05-14 12:36:43 -- STEP: 219/630 -- GLOBAL_STEP: 887300
| > loss_disc: 2.638266086578369 (2.6005397126010554)
| > loss_disc_real_0: 0.16823187470436096 (0.17360068279314264)
| > loss_disc_real_1: 0.23646531999111176 (0.21368307582863935)
| > loss_disc_real_2: 0.2739797830581665 (0.2281674467809669)
| > loss_disc_real_3: 0.2792148292064667 (0.23186842552875275)
| > loss_disc_real_4: 0.25924423336982727 (0.24016638460768958)
| > loss_disc_real_5: 0.24973316490650177 (0.23298136304774786)
| > loss_0: 2.638266086578369 (2.6005397126010554)
| > grad_norm_0: tensor(15.2779, device='cuda:0') (tensor(19.6571, device='cuda:0'))
| > loss_gen: 2.276791572570801 (2.2098615093318297)
| > loss_kl: 1.590544581413269 (1.5886369241427065)
| > loss_feat: 6.766689300537109 (6.836290938669144)
| > loss_mel: 16.578439712524414 (15.545607301198185)
| > loss_duration: 1.4775593280792236 (1.3673387771327743)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.69002342224121 (27.54773532745501)
| > grad_norm_1: tensor(159.5070, device='cuda:0') (tensor(245.9693, device='cuda:0'))
| > current_lr_0: 0.00019960037478133875
| > current_lr_1: 0.00019960037478133875
| > step_time: 0.5848 (0.5581906146654803)
| > loader_time: 0.0074 (0.006061982890786646)
--> TIME: 2025-05-14 12:37:47 -- STEP: 319/630 -- GLOBAL_STEP: 887400
| > loss_disc: 2.6821658611297607 (2.5920872733137057)
| > loss_disc_real_0: 0.242845356464386 (0.17217540862418265)
| > loss_disc_real_1: 0.19577118754386902 (0.2134193209551718)
| > loss_disc_real_2: 0.23395967483520508 (0.22878398566410463)
| > loss_disc_real_3: 0.26458796858787537 (0.2313294185553225)
| > loss_disc_real_4: 0.28443488478660583 (0.23948718546699954)
| > loss_disc_real_5: 0.25694146752357483 (0.2301571603198784)
| > loss_0: 2.6821658611297607 (2.5920872733137057)
| > grad_norm_0: tensor(70.1628, device='cuda:0') (tensor(20.6815, device='cuda:0'))
| > loss_gen: 2.3214335441589355 (2.213360487480523)
| > loss_kl: 1.7362627983093262 (1.5855372606026343)
| > loss_feat: 5.972080707550049 (6.8272540083499536)
| > loss_mel: 14.721064567565918 (15.519853487283832)
| > loss_duration: 1.5035208463668823 (1.3960032257540473)
| > amp_scaler: 128.0 (250.38244514106583)
| > loss_1: 26.254364013671875 (27.54200841491125)
| > grad_norm_1: tensor(362.6942, device='cuda:0') (tensor(256.5316, device='cuda:0'))
| > current_lr_0: 0.00019960037478133875
| > current_lr_1: 0.00019960037478133875
| > step_time: 0.7084 (0.580252997180138)
| > loader_time: 0.0089 (0.006645544943017275)
--> TIME: 2025-05-14 12:38:58 -- STEP: 419/630 -- GLOBAL_STEP: 887500
| > loss_disc: 2.3933238983154297 (2.594735847737167)
| > loss_disc_real_0: 0.1605975329875946 (0.1735411277996611)
| > loss_disc_real_1: 0.2174765020608902 (0.21412457088297474)
| > loss_disc_real_2: 0.23158171772956848 (0.22875296418735125)
| > loss_disc_real_3: 0.2159254252910614 (0.23037210825235008)
| > loss_disc_real_4: 0.21253208816051483 (0.23929910511134064)
| > loss_disc_real_5: 0.2355954498052597 (0.23116250510431985)
| > loss_0: 2.3933238983154297 (2.594735847737167)
| > grad_norm_0: tensor(9.2454, device='cuda:0') (tensor(20.5511, device='cuda:0'))
| > loss_gen: 2.245349884033203 (2.2163944708134498)
| > loss_kl: 1.5433820486068726 (1.5920569330525003)
| > loss_feat: 6.579614162445068 (6.826871915193617)
| > loss_mel: 15.413187980651855 (15.543999669659962)
| > loss_duration: 1.4599082469940186 (1.3989012978241944)
| > amp_scaler: 128.0 (221.1742243436754)
| > loss_1: 27.24144172668457 (27.578224227650352)
| > grad_norm_1: tensor(327.5768, device='cuda:0') (tensor(254.3087, device='cuda:0'))
| > current_lr_0: 0.00019960037478133875
| > current_lr_1: 0.00019960037478133875
| > step_time: 0.741 (0.6085347281435513)
| > loader_time: 0.0088 (0.0071991605235170375)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_887500.pth
--> TIME: 2025-05-14 12:40:20 -- STEP: 519/630 -- GLOBAL_STEP: 887600
| > loss_disc: 2.701235771179199 (2.594418387881592)
| > loss_disc_real_0: 0.1849256008863449 (0.17361741257483324)
| > loss_disc_real_1: 0.26189619302749634 (0.21393263842443966)
| > loss_disc_real_2: 0.23175102472305298 (0.2282198941431983)
| > loss_disc_real_3: 0.24830250442028046 (0.22993499353556737)
| > loss_disc_real_4: 0.24035459756851196 (0.2389886988782699)
| > loss_disc_real_5: 0.2340366691350937 (0.23170621664423013)
| > loss_0: 2.701235771179199 (2.594418387881592)
| > grad_norm_0: tensor(16.2044, device='cuda:0') (tensor(19.5486, device='cuda:0'))
| > loss_gen: 2.0069026947021484 (2.2083269456448105)
| > loss_kl: 1.5804369449615479 (1.5935964584350588)
| > loss_feat: 7.952576160430908 (6.764521556552895)
| > loss_mel: 14.78344440460205 (15.493141782536442)
| > loss_duration: 1.4243139028549194 (1.4114150447422824)
| > amp_scaler: 128.0 (203.22157996146436)
| > loss_1: 27.7476749420166 (27.471001718774698)
| > grad_norm_1: tensor(110.4612, device='cuda:0') (tensor(237.4316, device='cuda:0'))
| > current_lr_0: 0.00019960037478133875
| > current_lr_1: 0.00019960037478133875
| > step_time: 0.8268 (0.6384134246664472)
| > loader_time: 0.0103 (0.00772906911625798)
--> TIME: 2025-05-14 12:41:53 -- STEP: 619/630 -- GLOBAL_STEP: 887700
| > loss_disc: 2.7141013145446777 (2.593405575282352)
| > loss_disc_real_0: 0.26260945200920105 (0.1739745041496919)
| > loss_disc_real_1: 0.2771717309951782 (0.21395088412072238)
| > loss_disc_real_2: 0.21421268582344055 (0.22823965019863912)
| > loss_disc_real_3: 0.2617532014846802 (0.22983895369800883)
| > loss_disc_real_4: 0.2557218372821808 (0.2394049426176629)
| > loss_disc_real_5: 0.18317589163780212 (0.2306707408489819)
| > loss_0: 2.7141013145446777 (2.593405575282352)
| > grad_norm_0: tensor(38.3052, device='cuda:0') (tensor(19.7416, device='cuda:0'))
| > loss_gen: 2.328406810760498 (2.2128958499874534)
| > loss_kl: 1.6793949604034424 (1.5951537877947148)
| > loss_feat: 6.973641872406006 (6.763974751332272)
| > loss_mel: 15.250446319580078 (15.504323110441785)
| > loss_duration: 1.5281071662902832 (1.421662236646611)
| > amp_scaler: 128.0 (191.06946688206799)
| > loss_1: 27.759998321533203 (27.49800969556769)
| > grad_norm_1: tensor(647.9454, device='cuda:0') (tensor(240.3706, device='cuda:0'))
| > current_lr_0: 0.00019960037478133875
| > current_lr_1: 0.00019960037478133875
| > step_time: 1.0842 (0.6833348971383831)
| > loader_time: 0.0137 (0.0083313712395836)
> EVALUATION
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004980901877085368 (+3.9498011271158276e-05)
| > avg_loss_disc: 2.7026121020317078 (+0.07534593343734741)
| > avg_loss_disc_real_0: 0.34090377390384674 (+0.1619309807817141)
| > avg_loss_disc_real_1: 0.2451299193004767 (+0.031104659040768923)
| > avg_loss_disc_real_2: 0.22851191833615303 (-0.04848584905266762)
| > avg_loss_disc_real_3: 0.2187331939737002 (-0.03977400809526446)
| > avg_loss_disc_real_4: 0.22371958817044893 (-0.04909304653604826)
| > avg_loss_disc_real_5: 0.16605907492339608 (-0.0819739295790593)
| > avg_loss_0: 2.7026121020317078 (+0.07534593343734741)
| > avg_loss_gen: 2.2717518409093223 (+0.061170081297556855)
| > avg_loss_kl: 1.638478289047877 (-0.06483953197797132)
| > avg_loss_feat: 6.6160658200581866 (+0.4068748156229649)
| > avg_loss_mel: 15.705338637034098 (+0.3747412363688145)
| > avg_loss_duration: 1.5283117095629375 (+0.006884882847468132)
| > avg_loss_1: 27.75994602839152 (+0.7848316828409843)
> EPOCH: 17/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:42:16)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:43:05 -- STEP: 89/630 -- GLOBAL_STEP: 887800
| > loss_disc: 2.5499958992004395 (2.5619311600588683)
| > loss_disc_real_0: 0.17036795616149902 (0.17013325207353977)
| > loss_disc_real_1: 0.18993037939071655 (0.21660182432512218)
| > loss_disc_real_2: 0.28138116002082825 (0.22519283515683722)
| > loss_disc_real_3: 0.20456573367118835 (0.22765200526526805)
| > loss_disc_real_4: 0.21829722821712494 (0.2377387936530488)
| > loss_disc_real_5: 0.17607367038726807 (0.21717688031076046)
| > loss_0: 2.5499958992004395 (2.5619311600588683)
| > grad_norm_0: tensor(18.8606, device='cuda:0') (tensor(27.9227, device='cuda:0'))
| > loss_gen: 2.3080031871795654 (2.282733974831828)
| > loss_kl: 1.8939917087554932 (1.575272798538208)
| > loss_feat: 7.268620491027832 (7.105276364958688)
| > loss_mel: 15.719191551208496 (15.470960317033061)
| > loss_duration: 1.4521772861480713 (1.433372518989477)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.641983032226562 (27.867616139101177)
| > grad_norm_1: tensor(290.7354, device='cuda:0') (tensor(397.5861, device='cuda:0'))
| > current_lr_0: 0.00019957542473449108
| > current_lr_1: 0.00019957542473449108
| > step_time: 0.5441 (0.5299753874875188)
| > loader_time: 0.0061 (0.005387324965401983)
--> TIME: 2025-05-14 12:44:03 -- STEP: 189/630 -- GLOBAL_STEP: 887900
| > loss_disc: 2.3775649070739746 (2.5766263664084113)
| > loss_disc_real_0: 0.19284561276435852 (0.17006934615512373)
| > loss_disc_real_1: 0.21806840598583221 (0.2141462082743014)
| > loss_disc_real_2: 0.19572913646697998 (0.2256081567081825)
| > loss_disc_real_3: 0.22458818554878235 (0.22862102800891512)
| > loss_disc_real_4: 0.21237720549106598 (0.2401027720441263)
| > loss_disc_real_5: 0.22456054389476776 (0.22837747716241413)
| > loss_0: 2.3775649070739746 (2.5766263664084113)
| > grad_norm_0: tensor(17.1473, device='cuda:0') (tensor(22.2514, device='cuda:0'))
| > loss_gen: 2.314544916152954 (2.2355259934430407)
| > loss_kl: 1.752254605293274 (1.6008941307269706)
| > loss_feat: 6.475306987762451 (6.926504518619921)
| > loss_mel: 15.15851879119873 (15.462215918081778)
| > loss_duration: 1.449163794517517 (1.3959830923685952)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.149789810180664 (27.621123611611665)
| > grad_norm_1: tensor(262.3934, device='cuda:0') (tensor(385.1904, device='cuda:0'))
| > current_lr_0: 0.00019957542473449108
| > current_lr_1: 0.00019957542473449108
| > step_time: 0.5817 (0.5532513245072948)
| > loader_time: 0.0065 (0.005913870675223214)
--> TIME: 2025-05-14 12:45:07 -- STEP: 289/630 -- GLOBAL_STEP: 888000
| > loss_disc: 2.4583778381347656 (2.5852401091565698)
| > loss_disc_real_0: 0.13651369512081146 (0.17067831682498888)
| > loss_disc_real_1: 0.2146834284067154 (0.21440626180708208)
| > loss_disc_real_2: 0.23147225379943848 (0.22711405544751243)
| > loss_disc_real_3: 0.19949156045913696 (0.23008262404727275)
| > loss_disc_real_4: 0.2412722110748291 (0.24035893829223606)
| > loss_disc_real_5: 0.20612382888793945 (0.22904158301110086)
| > loss_0: 2.4583778381347656 (2.5852401091565698)
| > grad_norm_0: tensor(12.2912, device='cuda:0') (tensor(21.5246, device='cuda:0'))
| > loss_gen: 2.1112284660339355 (2.2259894922942842)
| > loss_kl: 1.7224363088607788 (1.617750734193927)
| > loss_feat: 6.631711006164551 (6.90372073361618)
| > loss_mel: 14.492987632751465 (15.48466954016768)
| > loss_duration: 1.4684414863586426 (1.396390423230234)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.426803588867188 (27.6285209457767)
| > grad_norm_1: tensor(288.9578, device='cuda:0') (tensor(351.3963, device='cuda:0'))
| > current_lr_0: 0.00019957542473449108
| > current_lr_1: 0.00019957542473449108
| > step_time: 0.6378 (0.5781134899099803)
| > loader_time: 0.0078 (0.006468574893515828)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_888000.pth
--> TIME: 2025-05-14 12:46:21 -- STEP: 389/630 -- GLOBAL_STEP: 888100
| > loss_disc: 2.4875271320343018 (2.591052705034191)
| > loss_disc_real_0: 0.17763638496398926 (0.17171998925334683)
| > loss_disc_real_1: 0.20309945940971375 (0.2143771173408528)
| > loss_disc_real_2: 0.23456935584545135 (0.2270776038764375)
| > loss_disc_real_3: 0.2041630744934082 (0.22935991276505674)
| > loss_disc_real_4: 0.20490524172782898 (0.24068517128728656)
| > loss_disc_real_5: 0.22369495034217834 (0.22991834502370315)
| > loss_0: 2.4875271320343018 (2.591052705034191)
| > grad_norm_0: tensor(22.6032, device='cuda:0') (tensor(21.3235, device='cuda:0'))
| > loss_gen: 2.155590534210205 (2.216468978970095)
| > loss_kl: 1.7372721433639526 (1.620044723574484)
| > loss_feat: 7.390008926391602 (6.861532273819638)
| > loss_mel: 15.710389137268066 (15.529803116707692)
| > loss_duration: 1.4816405773162842 (1.413100950209218)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.474899291992188 (27.6409501073293)
| > grad_norm_1: tensor(356.4127, device='cuda:0') (tensor(323.6909, device='cuda:0'))
| > current_lr_0: 0.00019957542473449108
| > current_lr_1: 0.00019957542473449108
| > step_time: 0.7191 (0.6086485165250335)
| > loader_time: 0.0089 (0.007040550898770133)
--> TIME: 2025-05-14 12:47:38 -- STEP: 489/630 -- GLOBAL_STEP: 888200
| > loss_disc: 2.636627435684204 (2.593052513516508)
| > loss_disc_real_0: 0.12084424495697021 (0.17185789907393031)
| > loss_disc_real_1: 0.22624064981937408 (0.21367511579839243)
| > loss_disc_real_2: 0.24625319242477417 (0.22701976964810144)
| > loss_disc_real_3: 0.25332722067832947 (0.22961594923142276)
| > loss_disc_real_4: 0.2666339874267578 (0.24080073556163803)
| > loss_disc_real_5: 0.21638967096805573 (0.23140710968608016)
| > loss_0: 2.636627435684204 (2.593052513516508)
| > grad_norm_0: tensor(8.9530, device='cuda:0') (tensor(19.5140, device='cuda:0'))
| > loss_gen: 2.1298129558563232 (2.2037551027621736)
| > loss_kl: 1.6009615659713745 (1.6161328673606514)
| > loss_feat: 6.57973051071167 (6.769837836790184)
| > loss_mel: 15.354209899902344 (15.516061995414624)
| > loss_duration: 1.4555860757827759 (1.412397533838003)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.120298385620117 (27.51818537175777)
| > grad_norm_1: tensor(63.2868, device='cuda:0') (tensor(281.5376, device='cuda:0'))
| > current_lr_0: 0.00019957542473449108
| > current_lr_1: 0.00019957542473449108
| > step_time: 0.7742 (0.6389971496137378)
| > loader_time: 0.0095 (0.007573597270286888)
--> TIME: 2025-05-14 12:49:05 -- STEP: 589/630 -- GLOBAL_STEP: 888300
| > loss_disc: 2.6080002784729004 (2.591908007607191)
| > loss_disc_real_0: 0.14031240344047546 (0.1720858296483806)
| > loss_disc_real_1: 0.16609102487564087 (0.21330608561609715)
| > loss_disc_real_2: 0.26946163177490234 (0.22755008710766486)
| > loss_disc_real_3: 0.26465538144111633 (0.22946703454229747)
| > loss_disc_real_4: 0.2734817862510681 (0.24036320092722596)
| > loss_disc_real_5: 0.1817501038312912 (0.23065326881479528)
| > loss_0: 2.6080002784729004 (2.591908007607191)
| > grad_norm_0: tensor(30.0364, device='cuda:0') (tensor(19.1278, device='cuda:0'))
| > loss_gen: 2.571183919906616 (2.2072297342766736)
| > loss_kl: 1.5327606201171875 (1.6193774017696667)
| > loss_feat: 6.70917272567749 (6.767303250641492)
| > loss_mel: 16.3351993560791 (15.532841240408466)
| > loss_duration: 1.4748294353485107 (1.4216355805890872)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.623146057128906 (27.5483872263055)
| > grad_norm_1: tensor(575.3492, device='cuda:0') (tensor(268.0723, device='cuda:0'))
| > current_lr_0: 0.00019957542473449108
| > current_lr_1: 0.00019957542473449108
| > step_time: 0.953 (0.6752657048366274)
| > loader_time: 0.0118 (0.008122650998152783)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.00526962677637736 (+0.0002887248992919922)
| > avg_loss_disc: 2.581980884075165 (-0.12063121795654297)
| > avg_loss_disc_real_0: 0.14490332454442978 (-0.19600044935941696)
| > avg_loss_disc_real_1: 0.2144248473147551 (-0.030705071985721588)
| > avg_loss_disc_real_2: 0.22296464691559473 (-0.005547271420558303)
| > avg_loss_disc_real_3: 0.2260539991160234 (+0.007320805142323195)
| > avg_loss_disc_real_4: 0.272722952067852 (+0.04900336389740309)
| > avg_loss_disc_real_5: 0.2715800888836384 (+0.1055210139602423)
| > avg_loss_0: 2.581980884075165 (-0.12063121795654297)
| > avg_loss_gen: 2.17368154724439 (-0.09807029366493225)
| > avg_loss_kl: 1.7562777896722157 (+0.11779950062433864)
| > avg_loss_feat: 7.00927738348643 (+0.3932115634282436)
| > avg_loss_mel: 15.478299935658773 (-0.22703870137532434)
| > avg_loss_duration: 1.5309225420157115 (+0.002610832452774048)
| > avg_loss_1: 27.948458989461262 (+0.18851296106974047)
> EPOCH: 18/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:50:00)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:50:32 -- STEP: 59/630 -- GLOBAL_STEP: 888400
| > loss_disc: 2.5736026763916016 (2.560464915582689)
| > loss_disc_real_0: 0.21300539374351501 (0.16996250238458985)
| > loss_disc_real_1: 0.21387389302253723 (0.21284721993793876)
| > loss_disc_real_2: 0.19681531190872192 (0.22485327821666912)
| > loss_disc_real_3: 0.2578384280204773 (0.22558661310349482)
| > loss_disc_real_4: 0.2985841631889343 (0.24158070299584986)
| > loss_disc_real_5: 0.2789400815963745 (0.2259814595266924)
| > loss_0: 2.5736026763916016 (2.560464915582689)
| > grad_norm_0: tensor(14.4683, device='cuda:0') (tensor(24.5433, device='cuda:0'))
| > loss_gen: 2.18131685256958 (2.2473193750543103)
| > loss_kl: 1.839187741279602 (1.593208115989879)
| > loss_feat: 5.806538105010986 (7.018519797567594)
| > loss_mel: 14.816390991210938 (15.475194704734673)
| > loss_duration: 1.4258641004562378 (1.4303876666699427)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.06929588317871 (27.76462955798133)
| > grad_norm_1: tensor(54.0669, device='cuda:0') (tensor(329.2239, device='cuda:0'))
| > current_lr_0: 0.00019955047780639926
| > current_lr_1: 0.00019955047780639926
| > step_time: 0.5179 (0.5196535870180294)
| > loader_time: 0.0054 (0.005039801031856215)
--> TIME: 2025-05-14 12:51:28 -- STEP: 159/630 -- GLOBAL_STEP: 888500
| > loss_disc: 2.646879196166992 (2.576286345907727)
| > loss_disc_real_0: 0.20258107781410217 (0.16824398091379203)
| > loss_disc_real_1: 0.1563894897699356 (0.2129154789653964)
| > loss_disc_real_2: 0.2074776589870453 (0.22757234475897542)
| > loss_disc_real_3: 0.265572726726532 (0.22677700184051347)
| > loss_disc_real_4: 0.25683045387268066 (0.24055404839275768)
| > loss_disc_real_5: 0.27932310104370117 (0.23249859011398172)
| > loss_0: 2.646879196166992 (2.576286345907727)
| > grad_norm_0: tensor(20.5621, device='cuda:0') (tensor(21.0693, device='cuda:0'))
| > loss_gen: 2.133047580718994 (2.225431895855838)
| > loss_kl: 1.2549076080322266 (1.6133553415724324)
| > loss_feat: 6.81824254989624 (6.953969946447408)
| > loss_mel: 16.266738891601562 (15.567599950346557)
| > loss_duration: 1.4584145545959473 (1.3727444005462355)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.931350708007812 (27.733101418933025)
| > grad_norm_1: tensor(155.1346, device='cuda:0') (tensor(284.1598, device='cuda:0'))
| > current_lr_0: 0.00019955047780639926
| > current_lr_1: 0.00019955047780639926
| > step_time: 0.5723 (0.5403856661334733)
| > loader_time: 0.0067 (0.0056887032850733345)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_888500.pth
--> TIME: 2025-05-14 12:52:32 -- STEP: 259/630 -- GLOBAL_STEP: 888600
| > loss_disc: 2.6609249114990234 (2.5802479683202213)
| > loss_disc_real_0: 0.16175229847431183 (0.16923002518972374)
| > loss_disc_real_1: 0.20795461535453796 (0.2111066597366425)
| > loss_disc_real_2: 0.23334433138370514 (0.2281232263936039)
| > loss_disc_real_3: 0.22292397916316986 (0.22817671857055088)
| > loss_disc_real_4: 0.2443845272064209 (0.23992850438738422)
| > loss_disc_real_5: 0.26516425609588623 (0.23197617442221255)
| > loss_0: 2.6609249114990234 (2.5802479683202213)
| > grad_norm_0: tensor(39.4373, device='cuda:0') (tensor(20.4722, device='cuda:0'))
| > loss_gen: 2.0407297611236572 (2.2104363703819776)
| > loss_kl: 1.5817761421203613 (1.616907538364293)
| > loss_feat: 6.028005599975586 (6.847992497521478)
| > loss_mel: 15.323936462402344 (15.547039267639397)
| > loss_duration: 1.4555151462554932 (1.3837927934285756)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.429962158203125 (27.606168393462777)
| > grad_norm_1: tensor(322.4675, device='cuda:0') (tensor(268.3615, device='cuda:0'))
| > current_lr_0: 0.00019955047780639926
| > current_lr_1: 0.00019955047780639926
| > step_time: 0.605 (0.5636146749768944)
| > loader_time: 0.0077 (0.006257347158483557)
--> TIME: 2025-05-14 12:53:38 -- STEP: 359/630 -- GLOBAL_STEP: 888700
| > loss_disc: 2.5963168144226074 (2.5838919416443558)
| > loss_disc_real_0: 0.21948736906051636 (0.17078367830319002)
| > loss_disc_real_1: 0.20612025260925293 (0.21236288375260107)
| > loss_disc_real_2: 0.22390104830265045 (0.22810366135453783)
| > loss_disc_real_3: 0.1888786405324936 (0.22833589570269944)
| > loss_disc_real_4: 0.22873631119728088 (0.2397676275052068)
| > loss_disc_real_5: 0.21292810142040253 (0.23111918564460404)
| > loss_0: 2.5963168144226074 (2.5838919416443558)
| > grad_norm_0: tensor(7.8425, device='cuda:0') (tensor(20.5426, device='cuda:0'))
| > loss_gen: 2.1693406105041504 (2.209589446819592)
| > loss_kl: 1.6738003492355347 (1.6119554745121583)
| > loss_feat: 6.666990756988525 (6.829036335427117)
| > loss_mel: 15.48983097076416 (15.535051568969047)
| > loss_duration: 1.4729878902435303 (1.404029903637666)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.472949981689453 (27.589662642200004)
| > grad_norm_1: tensor(58.7840, device='cuda:0') (tensor(262.8585, device='cuda:0'))
| > current_lr_0: 0.00019955047780639926
| > current_lr_1: 0.00019955047780639926
| > step_time: 0.6516 (0.585495578877442)
| > loader_time: 0.0096 (0.00676246273816462)
--> TIME: 2025-05-14 12:54:51 -- STEP: 459/630 -- GLOBAL_STEP: 888800
| > loss_disc: 2.5793886184692383 (2.5926084211968647)
| > loss_disc_real_0: 0.17783376574516296 (0.171490069535563)
| > loss_disc_real_1: 0.15372687578201294 (0.21292298137816987)
| > loss_disc_real_2: 0.19435448944568634 (0.22858360286371904)
| > loss_disc_real_3: 0.20921829342842102 (0.22934832753439094)
| > loss_disc_real_4: 0.23269221186637878 (0.2398946016767186)
| > loss_disc_real_5: 0.23088085651397705 (0.2329723620077104)
| > loss_0: 2.5793886184692383 (2.5926084211968647)
| > grad_norm_0: tensor(15.8700, device='cuda:0') (tensor(19.2716, device='cuda:0'))
| > loss_gen: 2.0623021125793457 (2.1956279010294812)
| > loss_kl: 1.5338791608810425 (1.6065784101912137)
| > loss_feat: 6.813322067260742 (6.748926312315698)
| > loss_mel: 15.815780639648438 (15.513801770012883)
| > loss_duration: 1.421539068222046 (1.4049081708870685)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.64682388305664 (27.469842495222228)
| > grad_norm_1: tensor(60.1291, device='cuda:0') (tensor(236.9455, device='cuda:0'))
| > current_lr_0: 0.00019955047780639926
| > current_lr_1: 0.00019955047780639926
| > step_time: 0.719 (0.6134292881992652)
| > loader_time: 0.0089 (0.007266292904456976)
--> TIME: 2025-05-14 12:56:13 -- STEP: 559/630 -- GLOBAL_STEP: 888900
| > loss_disc: 2.6562306880950928 (2.59128858322321)
| > loss_disc_real_0: 0.11002179235219955 (0.17144685763739095)
| > loss_disc_real_1: 0.23113292455673218 (0.21332494921195916)
| > loss_disc_real_2: 0.28554654121398926 (0.22884576643728827)
| > loss_disc_real_3: 0.25053802132606506 (0.22978145657157215)
| > loss_disc_real_4: 0.236097052693367 (0.23972373321145932)
| > loss_disc_real_5: 0.25179800391197205 (0.23196957936120588)
| > loss_0: 2.6562306880950928 (2.59128858322321)
| > grad_norm_0: tensor(7.7300, device='cuda:0') (tensor(20.1380, device='cuda:0'))
| > loss_gen: 2.03551983833313 (2.20112913281845)
| > loss_kl: 1.7419190406799316 (1.6062841751281176)
| > loss_feat: 5.511699676513672 (6.726798547188582)
| > loss_mel: 14.359760284423828 (15.516155601187554)
| > loss_duration: 1.4929349422454834 (1.4157987485418166)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 25.141834259033203 (27.466166129479028)
| > grad_norm_1: tensor(151.6452, device='cuda:0') (tensor(242.7287, device='cuda:0'))
| > current_lr_0: 0.00019955047780639926
| > current_lr_1: 0.00019955047780639926
| > step_time: 0.8769 (0.6476624280694137)
| > loader_time: 0.0106 (0.007820950424521895)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005068759123484293 (-0.00020086765289306727)
| > avg_loss_disc: 2.6937841971715293 (+0.11180331309636449)
| > avg_loss_disc_real_0: 0.18928499644001326 (+0.04438167189558348)
| > avg_loss_disc_real_1: 0.22208202257752419 (+0.0076571752627690726)
| > avg_loss_disc_real_2: 0.2725022087494532 (+0.04953756183385846)
| > avg_loss_disc_real_3: 0.25029823059837025 (+0.024244231482346862)
| > avg_loss_disc_real_4: 0.2839995237688223 (+0.011276571700970295)
| > avg_loss_disc_real_5: 0.27731331313649815 (+0.00573322425285977)
| > avg_loss_0: 2.6937841971715293 (+0.11180331309636449)
| > avg_loss_gen: 2.170070936282476 (-0.0036106109619140625)
| > avg_loss_kl: 1.829207181930542 (+0.07292939225832629)
| > avg_loss_feat: 6.344914714495341 (-0.6643626689910889)
| > avg_loss_mel: 15.876675923665365 (+0.3983759880065918)
| > avg_loss_duration: 1.5264968772729237 (-0.004425664742787827)
| > avg_loss_1: 27.747365474700928 (-0.2010935147603341)
> EPOCH: 19/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 12:57:35)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 12:57:52 -- STEP: 29/630 -- GLOBAL_STEP: 889000
| > loss_disc: 2.590909242630005 (2.5795447168679067)
| > loss_disc_real_0: 0.1576915681362152 (0.16511391771250755)
| > loss_disc_real_1: 0.21973180770874023 (0.2168621575010234)
| > loss_disc_real_2: 0.2391888052225113 (0.22502537431388064)
| > loss_disc_real_3: 0.23298846185207367 (0.22811251621821832)
| > loss_disc_real_4: 0.24795733392238617 (0.2454695444682549)
| > loss_disc_real_5: 0.22364114224910736 (0.23637578251032992)
| > loss_0: 2.590909242630005 (2.5795447168679067)
| > grad_norm_0: tensor(40.1398, device='cuda:0') (tensor(20.7325, device='cuda:0'))
| > loss_gen: 2.2605226039886475 (2.2356680426104307)
| > loss_kl: 1.5167500972747803 (1.5869983270250518)
| > loss_feat: 6.630181312561035 (7.0456174982005155)
| > loss_mel: 15.114002227783203 (15.564793323648386)
| > loss_duration: 1.3951181173324585 (1.4278571482362419)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.916574478149414 (27.86093409308072)
| > grad_norm_1: tensor(522.2332, device='cuda:0') (tensor(220.8007, device='cuda:0'))
| > current_lr_0: 0.00019952553399667344
| > current_lr_1: 0.00019952553399667344
| > step_time: 0.5117 (0.5158034521957924)
| > loader_time: 0.005 (0.00483957652387948)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_889000.pth
--> TIME: 2025-05-14 12:58:49 -- STEP: 129/630 -- GLOBAL_STEP: 889100
| > loss_disc: 2.363527774810791 (2.571724527566008)
| > loss_disc_real_0: 0.13539338111877441 (0.16665327352608827)
| > loss_disc_real_1: 0.18041850626468658 (0.21541002323461134)
| > loss_disc_real_2: 0.21635273098945618 (0.22798422163771104)
| > loss_disc_real_3: 0.2334437072277069 (0.2282935591169106)
| > loss_disc_real_4: 0.2143842875957489 (0.2401376194501108)
| > loss_disc_real_5: 0.14879140257835388 (0.2284002577842668)
| > loss_0: 2.363527774810791 (2.571724527566008)
| > grad_norm_0: tensor(11.6834, device='cuda:0') (tensor(20.6800, device='cuda:0'))
| > loss_gen: 2.1157703399658203 (2.2379879286122866)
| > loss_kl: 1.7909820079803467 (1.5966280319894006)
| > loss_feat: 6.370931625366211 (6.95439228531002)
| > loss_mel: 15.848233222961426 (15.487481028534646)
| > loss_duration: 1.4693900346755981 (1.4081898687421812)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.595308303833008 (27.68467904615772)
| > grad_norm_1: tensor(159.4355, device='cuda:0') (tensor(264.8995, device='cuda:0'))
| > current_lr_0: 0.00019952553399667344
| > current_lr_1: 0.00019952553399667344
| > step_time: 0.5855 (0.5320322273313534)
| > loader_time: 0.0062 (0.00543661450230798)
--> TIME: 2025-05-14 12:59:49 -- STEP: 229/630 -- GLOBAL_STEP: 889200
| > loss_disc: 2.7781081199645996 (2.577650429379991)
| > loss_disc_real_0: 0.23051223158836365 (0.1700720659184664)
| > loss_disc_real_1: 0.2446359395980835 (0.21217707541311673)
| > loss_disc_real_2: 0.17089858651161194 (0.227864234598443)
| > loss_disc_real_3: 0.20648270845413208 (0.23046323396753535)
| > loss_disc_real_4: 0.20459529757499695 (0.23959295874599806)
| > loss_disc_real_5: 0.28023985028266907 (0.22877189744768184)
| > loss_0: 2.7781081199645996 (2.577650429379991)
| > grad_norm_0: tensor(13.6816, device='cuda:0') (tensor(21.7080, device='cuda:0'))
| > loss_gen: 2.016106367111206 (2.2348173221646412)
| > loss_kl: 1.6796629428863525 (1.6184382964429895)
| > loss_feat: 7.306788444519043 (6.926261129337627)
| > loss_mel: 15.506938934326172 (15.567352153328308)
| > loss_duration: 1.4659395217895508 (1.3761513316475142)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.975433349609375 (27.723020128808166)
| > grad_norm_1: tensor(89.7759, device='cuda:0') (tensor(319.3794, device='cuda:0'))
| > current_lr_0: 0.00019952553399667344
| > current_lr_1: 0.00019952553399667344
| > step_time: 0.5989 (0.5557611530004108)
| > loader_time: 0.0072 (0.005954796570357277)
--> TIME: 2025-05-14 13:00:53 -- STEP: 329/630 -- GLOBAL_STEP: 889300
| > loss_disc: 2.6767759323120117 (2.5837484101756356)
| > loss_disc_real_0: 0.16442786157131195 (0.1717355566320086)
| > loss_disc_real_1: 0.17137210071086884 (0.21251433960934904)
| > loss_disc_real_2: 0.2134445458650589 (0.22793599079988647)
| > loss_disc_real_3: 0.2516078054904938 (0.22960993778923)
| > loss_disc_real_4: 0.24742287397384644 (0.23975097888508828)
| > loss_disc_real_5: 0.25979140400886536 (0.22959302021558525)
| > loss_0: 2.6767759323120117 (2.5837484101756356)
| > grad_norm_0: tensor(31.4626, device='cuda:0') (tensor(21.7846, device='cuda:0'))
| > loss_gen: 2.0274658203125 (2.226559367223349)
| > loss_kl: 1.5632933378219604 (1.6204527428084956)
| > loss_feat: 5.786581039428711 (6.885932789022797)
| > loss_mel: 15.196398735046387 (15.577847228586492)
| > loss_duration: 1.4762506484985352 (1.4008600534276756)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.04998779296875 (27.711652048453008)
| > grad_norm_1: tensor(298.8946, device='cuda:0') (tensor(297.0088, device='cuda:0'))
| > current_lr_0: 0.00019952553399667344
| > current_lr_1: 0.00019952553399667344
| > step_time: 0.6521 (0.5767761110172439)
| > loader_time: 0.0083 (0.006530610986031296)
--> TIME: 2025-05-14 13:02:04 -- STEP: 429/630 -- GLOBAL_STEP: 889400
| > loss_disc: 2.4734487533569336 (2.58723122256619)
| > loss_disc_real_0: 0.20759037137031555 (0.17305529331202274)
| > loss_disc_real_1: 0.20263825356960297 (0.2125439767515187)
| > loss_disc_real_2: 0.21966727077960968 (0.22817788719436227)
| > loss_disc_real_3: 0.18008588254451752 (0.2297750450931229)
| > loss_disc_real_4: 0.22066742181777954 (0.23978937940025108)
| > loss_disc_real_5: 0.26552534103393555 (0.2306872760499274)
| > loss_0: 2.4734487533569336 (2.58723122256619)
| > grad_norm_0: tensor(15.5653, device='cuda:0') (tensor(20.9800, device='cuda:0'))
| > loss_gen: 2.2871599197387695 (2.2175296103204025)
| > loss_kl: 1.7116414308547974 (1.6181486895034363)
| > loss_feat: 6.389497756958008 (6.833505122533765)
| > loss_mel: 15.19674015045166 (15.574777449761237)
| > loss_duration: 1.4636836051940918 (1.4027363867748588)
| > amp_scaler: 256.0 (132.17715617715615)
| > loss_1: 27.048721313476562 (27.646697113286088)
| > grad_norm_1: tensor(156.6583, device='cuda:0') (tensor(280.2215, device='cuda:0'))
| > current_lr_0: 0.00019952553399667344
| > current_lr_1: 0.00019952553399667344
| > step_time: 0.7257 (0.6043010902849386)
| > loader_time: 0.0093 (0.00706701512103314)
--> TIME: 2025-05-14 13:03:23 -- STEP: 529/630 -- GLOBAL_STEP: 889500
| > loss_disc: 2.4065282344818115 (2.587455870749143)
| > loss_disc_real_0: 0.21900907158851624 (0.17309846664252487)
| > loss_disc_real_1: 0.21733465790748596 (0.2125209259372803)
| > loss_disc_real_2: 0.2171430140733719 (0.22767641396738855)
| > loss_disc_real_3: 0.20233076810836792 (0.22958245915704054)
| > loss_disc_real_4: 0.1892474889755249 (0.23992247682325332)
| > loss_disc_real_5: 0.2159021645784378 (0.23083711408487115)
| > loss_0: 2.4065282344818115 (2.587455870749143)
| > grad_norm_0: tensor(7.9319, device='cuda:0') (tensor(20.8437, device='cuda:0'))
| > loss_gen: 2.2578577995300293 (2.2142051996941357)
| > loss_kl: 1.440342903137207 (1.6175911913296674)
| > loss_feat: 7.340822696685791 (6.790940895873791)
| > loss_mel: 15.052369117736816 (15.556594872069043)
| > loss_duration: 1.4429988861083984 (1.4141893165999413)
| > amp_scaler: 256.0 (155.58412098298675)
| > loss_1: 27.534391403198242 (27.59352135973752)
| > grad_norm_1: tensor(93.1010, device='cuda:0') (tensor(270.2060, device='cuda:0'))
| > current_lr_0: 0.00019952553399667344
| > current_lr_1: 0.00019952553399667344
| > step_time: 0.8314 (0.6364851015952673)
| > loader_time: 0.0105 (0.007616278354522186)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_889500.pth
--> TIME: 2025-05-14 13:05:07 -- STEP: 629/630 -- GLOBAL_STEP: 889600
| > loss_disc: 2.6009788513183594 (2.5895648161822917)
| > loss_disc_real_0: 0.1545337438583374 (0.17307518716362597)
| > loss_disc_real_1: 0.20161819458007812 (0.2131461382551868)
| > loss_disc_real_2: 0.22860611975193024 (0.2279288996668423)
| > loss_disc_real_3: 0.2575063407421112 (0.22968208477114266)
| > loss_disc_real_4: 0.24608057737350464 (0.23976983220001094)
| > loss_disc_real_5: 0.20875312387943268 (0.23155998702742905)
| > loss_0: 2.6009788513183594 (2.5895648161822917)
| > grad_norm_0: tensor(19.1763, device='cuda:0') (tensor(19.9746, device='cuda:0'))
| > loss_gen: 2.1046643257141113 (2.2089163248792913)
| > loss_kl: 1.6744731664657593 (1.6207419370429872)
| > loss_feat: 6.413708686828613 (6.760587987914939)
| > loss_mel: 15.63590145111084 (15.540377154448832)
| > loss_duration: 1.5016183853149414 (1.4233437990725315)
| > amp_scaler: 256.0 (171.54848966613673)
| > loss_1: 27.330364227294922 (27.55396709836343)
| > grad_norm_1: tensor(570.8367, device='cuda:0') (tensor(258.0587, device='cuda:0'))
| > current_lr_0: 0.00019952553399667344
| > current_lr_1: 0.00019952553399667344
| > step_time: 1.4728 (0.6933493788556945)
| > loader_time: 0.0154 (0.008366999072755657)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004905978838602701 (-0.0001627802848815918)
| > avg_loss_disc: 2.574891904989878 (-0.1188922921816511)
| > avg_loss_disc_real_0: 0.14558221958577633 (-0.04370277685423693)
| > avg_loss_disc_real_1: 0.18828151499231657 (-0.03380050758520761)
| > avg_loss_disc_real_2: 0.23399348556995392 (-0.03850872317949927)
| > avg_loss_disc_real_3: 0.2563805530468623 (+0.00608232244849205)
| > avg_loss_disc_real_4: 0.2570451460778713 (-0.026954377690950992)
| > avg_loss_disc_real_5: 0.22339637453357378 (-0.053916938602924375)
| > avg_loss_0: 2.574891904989878 (-0.1188922921816511)
| > avg_loss_gen: 2.0290775100390115 (-0.14099342624346445)
| > avg_loss_kl: 1.805339405934016 (-0.02386777599652601)
| > avg_loss_feat: 6.4542390902837115 (+0.10932437578837018)
| > avg_loss_mel: 15.601918776830038 (-0.27475714683532715)
| > avg_loss_duration: 1.5196883082389832 (-0.006808569033940559)
| > avg_loss_1: 27.410262902577717 (-0.3371025721232108)
> EPOCH: 20/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:05:16)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 13:06:10 -- STEP: 99/630 -- GLOBAL_STEP: 889700
| > loss_disc: 2.590895175933838 (2.5736076253833176)
| > loss_disc_real_0: 0.2382826805114746 (0.16927323106563452)
| > loss_disc_real_1: 0.2458665370941162 (0.21589062776830462)
| > loss_disc_real_2: 0.24303796887397766 (0.22678103681766626)
| > loss_disc_real_3: 0.2635914385318756 (0.23000964958860418)
| > loss_disc_real_4: 0.268966943025589 (0.23943327006065485)
| > loss_disc_real_5: 0.19301468133926392 (0.22188927248270826)
| > loss_0: 2.590895175933838 (2.5736076253833176)
| > grad_norm_0: tensor(18.4359, device='cuda:0') (tensor(24.5780, device='cuda:0'))
| > loss_gen: 2.0932204723358154 (2.2561730423358943)
| > loss_kl: 1.712169885635376 (1.5895781601318206)
| > loss_feat: 6.261690616607666 (7.032969388094815)
| > loss_mel: 15.263885498046875 (15.431144897383874)
| > loss_duration: 1.4583438634872437 (1.437170572955199)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.789310455322266 (27.74703596095846)
| > grad_norm_1: tensor(201.6091, device='cuda:0') (tensor(306.8849, device='cuda:0'))
| > current_lr_0: 0.00019950059330492385
| > current_lr_1: 0.00019950059330492385
| > step_time: 0.5272 (0.5258030289351338)
| > loader_time: 0.0055 (0.005274442711261785)
--> TIME: 2025-05-14 13:07:08 -- STEP: 199/630 -- GLOBAL_STEP: 889800
| > loss_disc: 2.5452048778533936 (2.57918024662152)
| > loss_disc_real_0: 0.13652047514915466 (0.17013856836000277)
| > loss_disc_real_1: 0.22965626418590546 (0.21297749360302584)
| > loss_disc_real_2: 0.2447318434715271 (0.22657942277702256)
| > loss_disc_real_3: 0.17585359513759613 (0.22909916825030915)
| > loss_disc_real_4: 0.22929739952087402 (0.24037866249455878)
| > loss_disc_real_5: 0.20664286613464355 (0.22684975672307325)
| > loss_0: 2.5452048778533936 (2.57918024662152)
| > grad_norm_0: tensor(21.1164, device='cuda:0') (tensor(23.2706, device='cuda:0'))
| > loss_gen: 2.0664432048797607 (2.237087375554608)
| > loss_kl: 1.8620758056640625 (1.6123637811622429)
| > loss_feat: 6.914305210113525 (6.938940053010107)
| > loss_mel: 14.997748374938965 (15.550708952860617)
| > loss_duration: 1.4187031984329224 (1.389777066719592)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.259273529052734 (27.72887715862025)
| > grad_norm_1: tensor(92.6195, device='cuda:0') (tensor(296.8266, device='cuda:0'))
| > current_lr_0: 0.00019950059330492385
| > current_lr_1: 0.00019950059330492385
| > step_time: 0.583 (0.5504077523197961)
| > loader_time: 0.0066 (0.005859957268489664)
--> TIME: 2025-05-14 13:08:11 -- STEP: 299/630 -- GLOBAL_STEP: 889900
| > loss_disc: 2.4735970497131348 (2.581119595562734)
| > loss_disc_real_0: 0.1745806634426117 (0.1699305063854889)
| > loss_disc_real_1: 0.18337048590183258 (0.21197526595464927)
| > loss_disc_real_2: 0.22236987948417664 (0.22795522347541158)
| > loss_disc_real_3: 0.23794417083263397 (0.22962115680094947)
| > loss_disc_real_4: 0.24126966297626495 (0.24006666437439297)
| > loss_disc_real_5: 0.16836833953857422 (0.2287525951762662)
| > loss_0: 2.4735970497131348 (2.581119595562734)
| > grad_norm_0: tensor(22.7322, device='cuda:0') (tensor(22.0362, device='cuda:0'))
| > loss_gen: 2.024405002593994 (2.228528640740693)
| > loss_kl: 1.8207894563674927 (1.6186624498271618)
| > loss_feat: 6.218670845031738 (6.8776375585575185)
| > loss_mel: 15.099265098571777 (15.556015630230856)
| > loss_duration: 1.426448106765747 (1.3951621442335502)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.58957862854004 (27.67600636817141)
| > grad_norm_1: tensor(91.7583, device='cuda:0') (tensor(277.1255, device='cuda:0'))
| > current_lr_0: 0.00019950059330492385
| > current_lr_1: 0.00019950059330492385
| > step_time: 0.6441 (0.5721827669685904)
| > loader_time: 0.0076 (0.006405781742721098)
--> TIME: 2025-05-14 13:09:20 -- STEP: 399/630 -- GLOBAL_STEP: 890000
| > loss_disc: 2.428149461746216 (2.580251048979604)
| > loss_disc_real_0: 0.15929198265075684 (0.16953378884042405)
| > loss_disc_real_1: 0.18587559461593628 (0.21166132517476435)
| > loss_disc_real_2: 0.2402307689189911 (0.22814044472119563)
| > loss_disc_real_3: 0.22948922216892242 (0.22876714289487154)
| > loss_disc_real_4: 0.21245668828487396 (0.24035482097389108)
| > loss_disc_real_5: 0.24807339906692505 (0.22962557694368196)
| > loss_0: 2.428149461746216 (2.580251048979604)
| > grad_norm_0: tensor(17.4480, device='cuda:0') (tensor(21.0722, device='cuda:0'))
| > loss_gen: 2.209634304046631 (2.223511025421601)
| > loss_kl: 1.7735557556152344 (1.6156069040298455)
| > loss_feat: 6.905001163482666 (6.852013917793906)
| > loss_mel: 15.148090362548828 (15.548378516558119)
| > loss_duration: 1.4345260858535767 (1.3977735622186105)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.470808029174805 (27.637283870152064)
| > grad_norm_1: tensor(259.6781, device='cuda:0') (tensor(263.7760, device='cuda:0'))
| > current_lr_0: 0.00019950059330492385
| > current_lr_1: 0.00019950059330492385
| > step_time: 0.7499 (0.5994937240629264)
| > loader_time: 0.0089 (0.006986218885072789)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_890000.pth
--> TIME: 2025-05-14 13:10:41 -- STEP: 499/630 -- GLOBAL_STEP: 890100
| > loss_disc: 2.6379899978637695 (2.580936297147212)
| > loss_disc_real_0: 0.20770806074142456 (0.16954508507418958)
| > loss_disc_real_1: 0.21752803027629852 (0.2122427569720932)
| > loss_disc_real_2: 0.22132600843906403 (0.22822263218716293)
| > loss_disc_real_3: 0.2607405185699463 (0.22892867446781878)
| > loss_disc_real_4: 0.26229915022850037 (0.24001411356046826)
| > loss_disc_real_5: 0.2713824212551117 (0.22958678180325723)
| > loss_0: 2.6379899978637695 (2.580936297147212)
| > grad_norm_0: tensor(38.6316, device='cuda:0') (tensor(20.2698, device='cuda:0'))
| > loss_gen: 2.2652556896209717 (2.2177909488429526)
| > loss_kl: 1.547715425491333 (1.616075665535095)
| > loss_feat: 6.704491138458252 (6.824603232687605)
| > loss_mel: 15.44037914276123 (15.548832901016265)
| > loss_duration: 1.4956343173980713 (1.4113035202026363)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.453474044799805 (27.61860620808267)
| > grad_norm_1: tensor(291.7560, device='cuda:0') (tensor(249.4420, device='cuda:0'))
| > current_lr_0: 0.00019950059330492385
| > current_lr_1: 0.00019950059330492385
| > step_time: 0.7876 (0.6314497911380618)
| > loader_time: 0.0092 (0.0075120491111923555)
--> TIME: 2025-05-14 13:12:09 -- STEP: 599/630 -- GLOBAL_STEP: 890200
| > loss_disc: 2.5139780044555664 (2.582350433171292)
| > loss_disc_real_0: 0.24922560155391693 (0.17060617173404644)
| > loss_disc_real_1: 0.22217553853988647 (0.21206389877553383)
| > loss_disc_real_2: 0.2228655368089676 (0.22816944080024013)
| > loss_disc_real_3: 0.1878199726343155 (0.22916866107556183)
| > loss_disc_real_4: 0.2748103737831116 (0.2398672553653112)
| > loss_disc_real_5: 0.23270824551582336 (0.22968215812526283)
| > loss_0: 2.5139780044555664 (2.582350433171292)
| > grad_norm_0: tensor(24.3224, device='cuda:0') (tensor(19.8137, device='cuda:0'))
| > loss_gen: 2.228741407394409 (2.212858126040095)
| > loss_kl: 1.6225045919418335 (1.6130148835094615)
| > loss_feat: 6.7371015548706055 (6.788416984284264)
| > loss_mel: 15.664457321166992 (15.529481604421676)
| > loss_duration: 1.4686429500579834 (1.4213281258915809)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.721446990966797 (27.565099652502095)
| > grad_norm_1: tensor(411.2791, device='cuda:0') (tensor(240.4827, device='cuda:0'))
| > current_lr_0: 0.00019950059330492385
| > current_lr_1: 0.00019950059330492385
| > step_time: 0.9831 (0.670422851342788)
| > loader_time: 0.0137 (0.008092246986987794)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005043009916941325 (+0.00013703107833862391)
| > avg_loss_disc: 2.613993247350057 (+0.039101342360178926)
| > avg_loss_disc_real_0: 0.14637026749551296 (+0.0007880479097366333)
| > avg_loss_disc_real_1: 0.22183498119314513 (+0.03355346620082855)
| > avg_loss_disc_real_2: 0.26584797849257785 (+0.031854492922623934)
| > avg_loss_disc_real_3: 0.2246942718823751 (-0.03168628116448721)
| > avg_loss_disc_real_4: 0.24090424428383508 (-0.01614090179403624)
| > avg_loss_disc_real_5: 0.23028654977679253 (+0.006890175243218749)
| > avg_loss_0: 2.613993247350057 (+0.039101342360178926)
| > avg_loss_gen: 2.0592347284158072 (+0.030157218376795747)
| > avg_loss_kl: 1.7402965525786083 (-0.06504285335540771)
| > avg_loss_feat: 6.505826433499654 (+0.05158734321594238)
| > avg_loss_mel: 15.421603202819824 (-0.1803155740102138)
| > avg_loss_duration: 1.5321314632892609 (+0.01244315505027771)
| > avg_loss_1: 27.259092489878338 (-0.15117041269937914)
> EPOCH: 21/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:12:52)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 13:13:30 -- STEP: 69/630 -- GLOBAL_STEP: 890300
| > loss_disc: 2.508545160293579 (2.5649721207826035)
| > loss_disc_real_0: 0.23360514640808105 (0.16719615135503849)
| > loss_disc_real_1: 0.2734556496143341 (0.2102138296417568)
| > loss_disc_real_2: 0.23973044753074646 (0.22856635589530502)
| > loss_disc_real_3: 0.20335926115512848 (0.23146339473517044)
| > loss_disc_real_4: 0.20599783957004547 (0.24395426395146744)
| > loss_disc_real_5: 0.21644015610218048 (0.23067968673464181)
| > loss_0: 2.508545160293579 (2.5649721207826035)
| > grad_norm_0: tensor(15.8712, device='cuda:0') (tensor(22.7369, device='cuda:0'))
| > loss_gen: 2.2786574363708496 (2.249529220055842)
| > loss_kl: 1.5427473783493042 (1.5933972562568774)
| > loss_feat: 6.732856273651123 (7.0688609247622285)
| > loss_mel: 15.42770004272461 (15.6303014340608)
| > loss_duration: 1.4504637718200684 (1.4364581833715024)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.43242645263672 (27.978546888931938)
| > grad_norm_1: tensor(148.5102, device='cuda:0') (tensor(261.2692, device='cuda:0'))
| > current_lr_0: 0.00019947565573076072
| > current_lr_1: 0.00019947565573076072
| > step_time: 0.5355 (0.5228606928949768)
| > loader_time: 0.0059 (0.005174132360928301)
--> TIME: 2025-05-14 13:14:28 -- STEP: 169/630 -- GLOBAL_STEP: 890400
| > loss_disc: 2.4551620483398438 (2.5701521232988718)
| > loss_disc_real_0: 0.10624021291732788 (0.16693725481012162)
| > loss_disc_real_1: 0.17764896154403687 (0.2122394036082827)
| > loss_disc_real_2: 0.23406459391117096 (0.22865848490119686)
| > loss_disc_real_3: 0.23854319751262665 (0.22988474598297706)
| > loss_disc_real_4: 0.24986986815929413 (0.24128370692391368)
| > loss_disc_real_5: 0.19320213794708252 (0.23029426868850664)
| > loss_0: 2.4551620483398438 (2.5701521232988718)
| > grad_norm_0: tensor(26.1028, device='cuda:0') (tensor(20.4732, device='cuda:0'))
| > loss_gen: 2.12597393989563 (2.2340155762328195)
| > loss_kl: 1.3987858295440674 (1.5906513710699137)
| > loss_feat: 7.193950176239014 (6.933978580158843)
| > loss_mel: 15.365257263183594 (15.499361269572782)
| > loss_duration: 1.4817063808441162 (1.3944758430740538)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.565673828125 (27.652482715584117)
| > grad_norm_1: tensor(415.8255, device='cuda:0') (tensor(276.3165, device='cuda:0'))
| > current_lr_0: 0.00019947565573076072
| > current_lr_1: 0.00019947565573076072
| > step_time: 0.5739 (0.5478757274221383)
| > loader_time: 0.0067 (0.005845233533509384)
--> TIME: 2025-05-14 13:15:28 -- STEP: 269/630 -- GLOBAL_STEP: 890500
| > loss_disc: 2.4458203315734863 (2.57897971642505)
| > loss_disc_real_0: 0.23860493302345276 (0.16846065976584262)
| > loss_disc_real_1: 0.22499124705791473 (0.2130362128901216)
| > loss_disc_real_2: 0.26217782497406006 (0.22859816419369225)
| > loss_disc_real_3: 0.2120673507452011 (0.2298431434152738)
| > loss_disc_real_4: 0.24788525700569153 (0.23972026161766408)
| > loss_disc_real_5: 0.20378857851028442 (0.23193680730450994)
| > loss_0: 2.4458203315734863 (2.57897971642505)
| > grad_norm_0: tensor(18.1430, device='cuda:0') (tensor(19.7424, device='cuda:0'))
| > loss_gen: 2.515760898590088 (2.2213605185866783)
| > loss_kl: 1.4314452409744263 (1.5999211223595204)
| > loss_feat: 7.062121391296387 (6.882727211735949)
| > loss_mel: 15.448692321777344 (15.520778248301227)
| > loss_duration: 1.4811010360717773 (1.3973063031093782)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.93912124633789 (27.622093455942146)
| > grad_norm_1: tensor(348.9461, device='cuda:0') (tensor(253.4501, device='cuda:0'))
| > current_lr_0: 0.00019947565573076072
| > current_lr_1: 0.00019947565573076072
| > step_time: 0.6041 (0.5645456606570669)
| > loader_time: 0.0078 (0.006341916477813153)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_890500.pth
--> TIME: 2025-05-14 13:16:37 -- STEP: 369/630 -- GLOBAL_STEP: 890600
| > loss_disc: 2.484107494354248 (2.582454612261556)
| > loss_disc_real_0: 0.2134668529033661 (0.17003881055003583)
| > loss_disc_real_1: 0.13450048863887787 (0.21396088836396612)
| > loss_disc_real_2: 0.23096150159835815 (0.2285680651745499)
| > loss_disc_real_3: 0.21473662555217743 (0.22943926632888917)
| > loss_disc_real_4: 0.22460848093032837 (0.2399316241101521)
| > loss_disc_real_5: 0.2695274353027344 (0.23198615830280594)
| > loss_0: 2.484107494354248 (2.582454612261556)
| > grad_norm_0: tensor(23.6464, device='cuda:0') (tensor(18.9903, device='cuda:0'))
| > loss_gen: 2.21671462059021 (2.216879278340636)
| > loss_kl: 1.7019157409667969 (1.6069722466352512)
| > loss_feat: 7.393097877502441 (6.842825034123449)
| > loss_mel: 15.27727222442627 (15.520653308568608)
| > loss_duration: 1.4420671463012695 (1.41395967213442)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.03106689453125 (27.601289552724786)
| > grad_norm_1: tensor(257.9543, device='cuda:0') (tensor(236.8113, device='cuda:0'))
| > current_lr_0: 0.00019947565573076072
| > current_lr_1: 0.00019947565573076072
| > step_time: 0.6742 (0.5875417682213507)
| > loader_time: 0.009 (0.0068599408881128)
--> TIME: 2025-05-14 13:17:52 -- STEP: 469/630 -- GLOBAL_STEP: 890700
| > loss_disc: 2.6222591400146484 (2.581015937109746)
| > loss_disc_real_0: 0.11639268696308136 (0.1699355181092138)
| > loss_disc_real_1: 0.18316853046417236 (0.21304069284691232)
| > loss_disc_real_2: 0.25803396105766296 (0.22901954681380218)
| > loss_disc_real_3: 0.233738973736763 (0.22955902073301995)
| > loss_disc_real_4: 0.26477935910224915 (0.24024308642853043)
| > loss_disc_real_5: 0.18794257938861847 (0.2299705050838019)
| > loss_0: 2.6222591400146484 (2.581015937109746)
| > grad_norm_0: tensor(20.7237, device='cuda:0') (tensor(19.8349, device='cuda:0'))
| > loss_gen: 2.1625382900238037 (2.2178665923157217)
| > loss_kl: 1.5715490579605103 (1.610956240818699)
| > loss_feat: 7.011415958404541 (6.819740471301048)
| > loss_mel: 15.515246391296387 (15.519953125829636)
| > loss_duration: 1.4623160362243652 (1.4132573304654183)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.723066329956055 (27.581773766068256)
| > grad_norm_1: tensor(273.3906, device='cuda:0') (tensor(245.5485, device='cuda:0'))
| > current_lr_0: 0.00019947565573076072
| > current_lr_1: 0.00019947565573076072
| > step_time: 0.7373 (0.6192686964453914)
| > loader_time: 0.0097 (0.007389628810923237)
--> TIME: 2025-05-14 13:19:16 -- STEP: 569/630 -- GLOBAL_STEP: 890800
| > loss_disc: 2.7880990505218506 (2.581029558852184)
| > loss_disc_real_0: 0.22039401531219482 (0.17004486089588675)
| > loss_disc_real_1: 0.19878561794757843 (0.21306614700855392)
| > loss_disc_real_2: 0.20163266360759735 (0.2288065819570595)
| > loss_disc_real_3: 0.21288512647151947 (0.22903648922334446)
| > loss_disc_real_4: 0.22113728523254395 (0.24004793148782425)
| > loss_disc_real_5: 0.2577158510684967 (0.23063153499878145)
| > loss_0: 2.7880990505218506 (2.581029558852184)
| > grad_norm_0: tensor(15.0286, device='cuda:0') (tensor(19.3124, device='cuda:0'))
| > loss_gen: 2.0488929748535156 (2.211720029792383)
| > loss_kl: 1.5909368991851807 (1.6083569377922635)
| > loss_feat: 6.739809513092041 (6.7707957576155025)
| > loss_mel: 15.79755687713623 (15.510798323552512)
| > loss_duration: 1.462772011756897 (1.4226950606059523)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.639968872070312 (27.524366127376197)
| > grad_norm_1: tensor(75.6075, device='cuda:0') (tensor(235.1718, device='cuda:0'))
| > current_lr_0: 0.00019947565573076072
| > current_lr_1: 0.00019947565573076072
| > step_time: 0.8502 (0.6551313957556267)
| > loader_time: 0.0107 (0.00795203897781238)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005340894063313802 (+0.00029788414637247664)
| > avg_loss_disc: 2.578609128793081 (-0.03538411855697632)
| > avg_loss_disc_real_0: 0.24630849435925484 (+0.09993822686374187)
| > avg_loss_disc_real_1: 0.2039612097044786 (-0.017873771488666534)
| > avg_loss_disc_real_2: 0.21544093017776808 (-0.05040704831480977)
| > avg_loss_disc_real_3: 0.23112130289276442 (+0.006427031010389328)
| > avg_loss_disc_real_4: 0.2424355869491895 (+0.0015313426653544293)
| > avg_loss_disc_real_5: 0.23645709827542305 (+0.006170548498630524)
| > avg_loss_0: 2.578609128793081 (-0.03538411855697632)
| > avg_loss_gen: 2.1905574997266135 (+0.13132277131080627)
| > avg_loss_kl: 1.7378626465797424 (-0.0024339059988658374)
| > avg_loss_feat: 6.640856305758159 (+0.13502987225850482)
| > avg_loss_mel: 15.556625445683798 (+0.13502224286397357)
| > avg_loss_duration: 1.5214502116044362 (-0.0106812516848247)
| > avg_loss_1: 27.64735221862793 (+0.3882597287495919)
> EPOCH: 22/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:20:31)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 13:20:53 -- STEP: 39/630 -- GLOBAL_STEP: 890900
| > loss_disc: 2.4862871170043945 (2.5442155752426534)
| > loss_disc_real_0: 0.16171938180923462 (0.16678126347370634)
| > loss_disc_real_1: 0.17382660508155823 (0.20764473386299917)
| > loss_disc_real_2: 0.1904878318309784 (0.22401892221890962)
| > loss_disc_real_3: 0.23647326231002808 (0.22330719232559204)
| > loss_disc_real_4: 0.22289222478866577 (0.24387091856736404)
| > loss_disc_real_5: 0.17892399430274963 (0.22193246927016821)
| > loss_0: 2.4862871170043945 (2.5442155752426534)
| > grad_norm_0: tensor(23.3675, device='cuda:0') (tensor(21.3466, device='cuda:0'))
| > loss_gen: 2.342576503753662 (2.284468369606213)
| > loss_kl: 1.977612853050232 (1.5225593952032237)
| > loss_feat: 7.522021293640137 (7.080509051298484)
| > loss_mel: 16.195520401000977 (15.682995894016363)
| > loss_duration: 1.432945966720581 (1.4284984087332704)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.47067642211914 (27.999031115800907)
| > grad_norm_1: tensor(539.9031, device='cuda:0') (tensor(271.0610, device='cuda:0'))
| > current_lr_0: 0.00019945072127379438
| > current_lr_1: 0.00019945072127379438
| > step_time: 0.5394 (0.5257566831050773)
| > loader_time: 0.0055 (0.004984213755680964)
--> TIME: 2025-05-14 13:21:48 -- STEP: 139/630 -- GLOBAL_STEP: 891000
| > loss_disc: 2.467832565307617 (2.575657576965772)
| > loss_disc_real_0: 0.19448700547218323 (0.17217704198128886)
| > loss_disc_real_1: 0.1781279742717743 (0.21134078106005416)
| > loss_disc_real_2: 0.2002749741077423 (0.22741555899596042)
| > loss_disc_real_3: 0.1981908529996872 (0.22798056696816313)
| > loss_disc_real_4: 0.24452482163906097 (0.24062685539825357)
| > loss_disc_real_5: 0.23619678616523743 (0.2283968773248384)
| > loss_0: 2.467832565307617 (2.575657576965772)
| > grad_norm_0: tensor(20.3191, device='cuda:0') (tensor(21.8278, device='cuda:0'))
| > loss_gen: 2.3146634101867676 (2.245582060848208)
| > loss_kl: 1.502134919166565 (1.5974943672152733)
| > loss_feat: 6.66635274887085 (6.99470390347268)
| > loss_mel: 15.383187294006348 (15.528581358545976)
| > loss_duration: 1.4595664739608765 (1.4183408785209382)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.325902938842773 (27.784702520576314)
| > grad_norm_1: tensor(214.1115, device='cuda:0') (tensor(273.5426, device='cuda:0'))
| > current_lr_0: 0.00019945072127379438
| > current_lr_1: 0.00019945072127379438
| > step_time: 0.568 (0.5397497475576055)
| > loader_time: 0.007 (0.00560855693954358)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_891000.pth
--> TIME: 2025-05-14 13:22:53 -- STEP: 239/630 -- GLOBAL_STEP: 891100
| > loss_disc: 2.6191329956054688 (2.5757144205739806)
| > loss_disc_real_0: 0.15967923402786255 (0.17048825847304522)
| > loss_disc_real_1: 0.2796841561794281 (0.21115110197326628)
| > loss_disc_real_2: 0.3248772919178009 (0.22838655924697301)
| > loss_disc_real_3: 0.28730103373527527 (0.2272232148687211)
| > loss_disc_real_4: 0.26753365993499756 (0.24036176259547598)
| > loss_disc_real_5: 0.2568940222263336 (0.23081161125434493)
| > loss_0: 2.6191329956054688 (2.5757144205739806)
| > grad_norm_0: tensor(7.9852, device='cuda:0') (tensor(20.1573, device='cuda:0'))
| > loss_gen: 2.4112160205841064 (2.229011643880579)
| > loss_kl: 1.5851234197616577 (1.6243307046810451)
| > loss_feat: 6.609187126159668 (6.926211450888022)
| > loss_mel: 15.783415794372559 (15.465702819026165)
| > loss_duration: 1.4742943048477173 (1.3849049646984084)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.863237380981445 (27.630161532797075)
| > grad_norm_1: tensor(106.5759, device='cuda:0') (tensor(254.1200, device='cuda:0'))
| > current_lr_0: 0.00019945072127379438
| > current_lr_1: 0.00019945072127379438
| > step_time: 0.6011 (0.5667659438304818)
| > loader_time: 0.007 (0.006167164407514626)
--> TIME: 2025-05-14 13:24:00 -- STEP: 339/630 -- GLOBAL_STEP: 891200
| > loss_disc: 2.651001214981079 (2.5755001190489377)
| > loss_disc_real_0: 0.15858310461044312 (0.1702411769062369)
| > loss_disc_real_1: 0.21519364416599274 (0.21063764933991222)
| > loss_disc_real_2: 0.29751110076904297 (0.22837608991119362)
| > loss_disc_real_3: 0.21780391037464142 (0.2286901379493134)
| > loss_disc_real_4: 0.27049314975738525 (0.24057540697509913)
| > loss_disc_real_5: 0.25189730525016785 (0.22915096629334059)
| > loss_0: 2.651001214981079 (2.5755001190489377)
| > grad_norm_0: tensor(31.7216, device='cuda:0') (tensor(21.6649, device='cuda:0'))
| > loss_gen: 2.161207437515259 (2.2334440672292084)
| > loss_kl: 1.7371916770935059 (1.618396511823378)
| > loss_feat: 6.317499160766602 (6.914376862281192)
| > loss_mel: 15.419225692749023 (15.449232318056719)
| > loss_duration: 1.4229356050491333 (1.405448529572613)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.058059692382812 (27.62089830021591)
| > grad_norm_1: tensor(361.7995, device='cuda:0') (tensor(270.9490, device='cuda:0'))
| > current_lr_0: 0.00019945072127379438
| > current_lr_1: 0.00019945072127379438
| > step_time: 0.699 (0.5935708674709351)
| > loader_time: 0.009 (0.006723299139017199)
--> TIME: 2025-05-14 13:25:13 -- STEP: 439/630 -- GLOBAL_STEP: 891300
| > loss_disc: 2.530735969543457 (2.5804842180977636)
| > loss_disc_real_0: 0.1332130879163742 (0.17088404341955135)
| > loss_disc_real_1: 0.18438254296779633 (0.21160039797866534)
| > loss_disc_real_2: 0.23824411630630493 (0.22901611498520966)
| > loss_disc_real_3: 0.26029273867607117 (0.22861847936563992)
| > loss_disc_real_4: 0.2681395411491394 (0.24059045043241462)
| > loss_disc_real_5: 0.26121267676353455 (0.22946967137022822)
| > loss_0: 2.530735969543457 (2.5804842180977636)
| > grad_norm_0: tensor(36.4242, device='cuda:0') (tensor(21.8376, device='cuda:0'))
| > loss_gen: 2.1692895889282227 (2.2262020434225307)
| > loss_kl: 1.7057948112487793 (1.6160539032929577)
| > loss_feat: 5.619987487792969 (6.875993704741528)
| > loss_mel: 14.519865036010742 (15.461664656028661)
| > loss_duration: 1.483278512954712 (1.4065148898300655)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.49821662902832 (27.586429200574315)
| > grad_norm_1: tensor(351.5213, device='cuda:0') (tensor(270.1876, device='cuda:0'))
| > current_lr_0: 0.00019945072127379438
| > current_lr_1: 0.00019945072127379438
| > step_time: 0.7375 (0.6228535153599692)
| > loader_time: 0.0093 (0.007270436080550277)
--> TIME: 2025-05-14 13:26:36 -- STEP: 539/630 -- GLOBAL_STEP: 891400
| > loss_disc: 2.6219401359558105 (2.580116985459052)
| > loss_disc_real_0: 0.15695784986019135 (0.17159318870040627)
| > loss_disc_real_1: 0.18657176196575165 (0.21160398899181876)
| > loss_disc_real_2: 0.20335178077220917 (0.22857944001072197)
| > loss_disc_real_3: 0.2102961540222168 (0.22885899345264363)
| > loss_disc_real_4: 0.21603041887283325 (0.24028236467342873)
| > loss_disc_real_5: 0.23602360486984253 (0.22890306699585602)
| > loss_0: 2.6219401359558105 (2.580116985459052)
| > grad_norm_0: tensor(28.9615, device='cuda:0') (tensor(22.1884, device='cuda:0'))
| > loss_gen: 2.031845808029175 (2.225745136087588)
| > loss_kl: 1.5627387762069702 (1.6158750917562081)
| > loss_feat: 6.519467830657959 (6.842279374931208)
| > loss_mel: 14.992443084716797 (15.461781105437836)
| > loss_duration: 1.4734389781951904 (1.4174927614615445)
| > amp_scaler: 256.0 (259.3246753246754)
| > loss_1: 26.579933166503906 (27.563173460385354)
| > grad_norm_1: tensor(257.2169, device='cuda:0') (tensor(271.9716, device='cuda:0'))
| > current_lr_0: 0.00019945072127379438
| > current_lr_1: 0.00019945072127379438
| > step_time: 0.9001 (0.6577556062496656)
| > loader_time: 0.0121 (0.007814493161627889)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005332748095194499 (-8.145968119302807e-06)
| > avg_loss_disc: 2.6937608321507773 (+0.11515170335769653)
| > avg_loss_disc_real_0: 0.23777721698085466 (-0.008531277378400176)
| > avg_loss_disc_real_1: 0.2687414512038231 (+0.0647802414993445)
| > avg_loss_disc_real_2: 0.23312701905767122 (+0.01768608887990314)
| > avg_loss_disc_real_3: 0.25097675745685893 (+0.019855454564094516)
| > avg_loss_disc_real_4: 0.22540594016512236 (-0.017029646784067154)
| > avg_loss_disc_real_5: 0.22697569305698076 (-0.00948140521844229)
| > avg_loss_0: 2.6937608321507773 (+0.11515170335769653)
| > avg_loss_gen: 2.2394009232521057 (+0.0488434235254922)
| > avg_loss_kl: 1.764559268951416 (+0.026696622371673584)
| > avg_loss_feat: 6.607199629147847 (-0.033656676610311465)
| > avg_loss_mel: 15.474721749623617 (-0.08190369606018066)
| > avg_loss_duration: 1.5320588052272797 (+0.010608593622843498)
| > avg_loss_1: 27.617940266927082 (-0.02941195170084754)
> EPOCH: 23/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:28:20)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 13:28:25 -- STEP: 9/630 -- GLOBAL_STEP: 891500
| > loss_disc: 2.5689265727996826 (2.5919610129462347)
| > loss_disc_real_0: 0.17978167533874512 (0.17066588832272422)
| > loss_disc_real_1: 0.18325552344322205 (0.21302616430653465)
| > loss_disc_real_2: 0.21850590407848358 (0.22134993804825676)
| > loss_disc_real_3: 0.20475980639457703 (0.2237211416165034)
| > loss_disc_real_4: 0.21983112394809723 (0.2596525020069546)
| > loss_disc_real_5: 0.20252567529678345 (0.24208380778630575)
| > loss_0: 2.5689265727996826 (2.5919610129462347)
| > grad_norm_0: tensor(14.0030, device='cuda:0') (tensor(13.5660, device='cuda:0'))
| > loss_gen: 2.2741007804870605 (2.3125761879814997)
| > loss_kl: 1.4184082746505737 (1.5447381734848022)
| > loss_feat: 8.165867805480957 (7.639859676361084)
| > loss_mel: 15.84589958190918 (15.62499385409885)
| > loss_duration: 1.3994815349578857 (1.4241113795174494)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.103757858276367 (28.54627842373318)
| > grad_norm_1: tensor(137.1086, device='cuda:0') (tensor(116.9546, device='cuda:0'))
| > current_lr_0: 0.00019942578993363514
| > current_lr_1: 0.00019942578993363514
| > step_time: 0.549 (0.5141121016608344)
| > loader_time: 0.0045 (0.004394107394748264)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_891500.pth
--> TIME: 2025-05-14 13:29:24 -- STEP: 109/630 -- GLOBAL_STEP: 891600
| > loss_disc: 2.5886924266815186 (2.5814893420683123)
| > loss_disc_real_0: 0.20531460642814636 (0.16804821344964002)
| > loss_disc_real_1: 0.19147153198719025 (0.21510062503431915)
| > loss_disc_real_2: 0.2289365977048874 (0.23182541815512772)
| > loss_disc_real_3: 0.2078743726015091 (0.22507203814633395)
| > loss_disc_real_4: 0.21619728207588196 (0.24197430266152828)
| > loss_disc_real_5: 0.16749246418476105 (0.23055763583664501)
| > loss_0: 2.5886924266815186 (2.5814893420683123)
| > grad_norm_0: tensor(14.6978, device='cuda:0') (tensor(14.6822, device='cuda:0'))
| > loss_gen: 2.0990474224090576 (2.231327756829219)
| > loss_kl: 1.6624685525894165 (1.596866870145186)
| > loss_feat: 7.037642955780029 (6.952344054475836)
| > loss_mel: 14.712151527404785 (15.463085559529995)
| > loss_duration: 1.465456247329712 (1.3892308375157343)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.976764678955078 (27.632855039124095)
| > grad_norm_1: tensor(291.7482, device='cuda:0') (tensor(170.0835, device='cuda:0'))
| > current_lr_0: 0.00019942578993363514
| > current_lr_1: 0.00019942578993363514
| > step_time: 0.5431 (0.5454286019736473)
| > loader_time: 0.0069 (0.005419768324685755)
--> TIME: 2025-05-14 13:30:24 -- STEP: 209/630 -- GLOBAL_STEP: 891700
| > loss_disc: 2.5634336471557617 (2.573903987282201)
| > loss_disc_real_0: 0.24457067251205444 (0.17003351296676975)
| > loss_disc_real_1: 0.20944413542747498 (0.2147131591108427)
| > loss_disc_real_2: 0.19956517219543457 (0.23043949146304973)
| > loss_disc_real_3: 0.25024062395095825 (0.22843704597231304)
| > loss_disc_real_4: 0.2167312502861023 (0.24072909426460995)
| > loss_disc_real_5: 0.24948589503765106 (0.22235335473808945)
| > loss_0: 2.5634336471557617 (2.573903987282201)
| > grad_norm_0: tensor(22.1037, device='cuda:0') (tensor(21.4279, device='cuda:0'))
| > loss_gen: 2.2316858768463135 (2.2665162474344807)
| > loss_kl: 1.751657485961914 (1.618117614225908)
| > loss_feat: 6.470715522766113 (7.004102658997312)
| > loss_mel: 15.747870445251465 (15.497275785966353)
| > loss_duration: 1.4620251655578613 (1.3901018896741724)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.66395378112793 (27.776114103326385)
| > grad_norm_1: tensor(116.8840, device='cuda:0') (tensor(267.9967, device='cuda:0'))
| > current_lr_0: 0.00019942578993363514
| > current_lr_1: 0.00019942578993363514
| > step_time: 0.6291 (0.5643940211483165)
| > loader_time: 0.007 (0.005940561659598465)
--> TIME: 2025-05-14 13:31:28 -- STEP: 309/630 -- GLOBAL_STEP: 891800
| > loss_disc: 2.6625027656555176 (2.581497336668489)
| > loss_disc_real_0: 0.17479553818702698 (0.17125427742220434)
| > loss_disc_real_1: 0.23651325702667236 (0.21439736857286934)
| > loss_disc_real_2: 0.20791219174861908 (0.23016273546180294)
| > loss_disc_real_3: 0.23678532242774963 (0.22787972479383536)
| > loss_disc_real_4: 0.24007932841777802 (0.2392869632703201)
| > loss_disc_real_5: 0.2525744140148163 (0.22764699947101016)
| > loss_0: 2.6625027656555176 (2.581497336668489)
| > grad_norm_0: tensor(26.4045, device='cuda:0') (tensor(19.1814, device='cuda:0'))
| > loss_gen: 2.0717248916625977 (2.2394346075922167)
| > loss_kl: 1.777432918548584 (1.6177632723811373)
| > loss_feat: 7.193081378936768 (6.8821740767716575)
| > loss_mel: 15.496232032775879 (15.499811653951996)
| > loss_duration: 1.4587136507034302 (1.4124866029591236)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.99718475341797 (27.651670141127504)
| > grad_norm_1: tensor(272.0473, device='cuda:0') (tensor(226.0540, device='cuda:0'))
| > current_lr_0: 0.00019942578993363514
| > current_lr_1: 0.00019942578993363514
| > step_time: 0.6769 (0.5841680005144535)
| > loader_time: 0.0093 (0.006496181765806327)
--> TIME: 2025-05-14 13:32:38 -- STEP: 409/630 -- GLOBAL_STEP: 891900
| > loss_disc: 2.6748569011688232 (2.5853846562812266)
| > loss_disc_real_0: 0.2233547866344452 (0.17205496105048945)
| > loss_disc_real_1: 0.19978484511375427 (0.21445629009772046)
| > loss_disc_real_2: 0.2815251350402832 (0.2302935343864203)
| > loss_disc_real_3: 0.2612247169017792 (0.228886823199489)
| > loss_disc_real_4: 0.2701517939567566 (0.23937743734613898)
| > loss_disc_real_5: 0.2605712413787842 (0.22678200711102245)
| > loss_0: 2.6748569011688232 (2.5853846562812266)
| > grad_norm_0: tensor(26.5393, device='cuda:0') (tensor(20.1052, device='cuda:0'))
| > loss_gen: 2.289989948272705 (2.2376757297655776)
| > loss_kl: 1.646167278289795 (1.6207161832846753)
| > loss_feat: 6.606828212738037 (6.864951080098419)
| > loss_mel: 15.63026237487793 (15.493133234802842)
| > loss_duration: 1.4765890836715698 (1.417925966980987)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.649837493896484 (27.63440214684074)
| > grad_norm_1: tensor(160.3665, device='cuda:0') (tensor(236.2159, device='cuda:0'))
| > current_lr_0: 0.00019942578993363514
| > current_lr_1: 0.00019942578993363514
| > step_time: 0.7393 (0.6109020546770914)
| > loader_time: 0.0103 (0.0070990904036244435)
--> TIME: 2025-05-14 13:33:57 -- STEP: 509/630 -- GLOBAL_STEP: 892000
| > loss_disc: 2.6872541904449463 (2.5836199346366238)
| > loss_disc_real_0: 0.17560569941997528 (0.1725199611780686)
| > loss_disc_real_1: 0.17958125472068787 (0.21324627375146027)
| > loss_disc_real_2: 0.2167387157678604 (0.22870843484265865)
| > loss_disc_real_3: 0.23972724378108978 (0.22934433955457684)
| > loss_disc_real_4: 0.24540747702121735 (0.23926444234571664)
| > loss_disc_real_5: 0.2788998484611511 (0.2284930286332526)
| > loss_0: 2.6872541904449463 (2.5836199346366238)
| > grad_norm_0: tensor(15.6100, device='cuda:0') (tensor(19.3758, device='cuda:0'))
| > loss_gen: 2.1119353771209717 (2.2284840387539218)
| > loss_kl: 1.5160685777664185 (1.6236470914308587)
| > loss_feat: 5.6422247886657715 (6.808107762065054)
| > loss_mel: 15.174543380737305 (15.502111695370177)
| > loss_duration: 1.4122672080993652 (1.4267470251132082)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.857038497924805 (27.589097590718147)
| > grad_norm_1: tensor(176.3160, device='cuda:0') (tensor(227.0017, device='cuda:0'))
| > current_lr_0: 0.00019942578993363514
| > current_lr_1: 0.00019942578993363514
| > step_time: 0.8654 (0.6423497185960033)
| > loader_time: 0.0099 (0.007670002508257133)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_892000.pth
--> TIME: 2025-05-14 13:35:33 -- STEP: 609/630 -- GLOBAL_STEP: 892100
| > loss_disc: 2.614476203918457 (2.5837684531125724)
| > loss_disc_real_0: 0.21674810349941254 (0.172272972701414)
| > loss_disc_real_1: 0.18852540850639343 (0.21305428412307073)
| > loss_disc_real_2: 0.26506489515304565 (0.22835815880196822)
| > loss_disc_real_3: 0.2070174515247345 (0.2293985060038434)
| > loss_disc_real_4: 0.22738218307495117 (0.23935967544323117)
| > loss_disc_real_5: 0.27336961030960083 (0.2287121003337682)
| > loss_0: 2.614476203918457 (2.5837684531125724)
| > grad_norm_0: tensor(23.2242, device='cuda:0') (tensor(19.3261, device='cuda:0'))
| > loss_gen: 2.237143039703369 (2.224512664555329)
| > loss_kl: 1.6999918222427368 (1.6234541900443722)
| > loss_feat: 5.941520690917969 (6.774398225085877)
| > loss_mel: 15.512892723083496 (15.497400014467036)
| > loss_duration: 1.4870257377624512 (1.4334721173754656)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.87857437133789 (27.553237175902318)
| > grad_norm_1: tensor(210.6920, device='cuda:0') (tensor(223.5282, device='cuda:0'))
| > current_lr_0: 0.00019942578993363514
| > current_lr_1: 0.00019942578993363514
| > step_time: 1.0045 (0.6876274321858324)
| > loader_time: 0.0127 (0.008315508784527454)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004717727502187093 (-0.0006150205930074062)
| > avg_loss_disc: 2.498935321966807 (-0.19482551018397043)
| > avg_loss_disc_real_0: 0.15154729783535004 (-0.08622991914550462)
| > avg_loss_disc_real_1: 0.1898052953183651 (-0.07893615588545799)
| > avg_loss_disc_real_2: 0.2770354362825553 (+0.04390841722488406)
| > avg_loss_disc_real_3: 0.22912824029723802 (-0.02184851715962091)
| > avg_loss_disc_real_4: 0.26078782106439274 (+0.035381880899270385)
| > avg_loss_disc_real_5: 0.2220700408021609 (-0.00490565225481987)
| > avg_loss_0: 2.498935321966807 (-0.19482551018397043)
| > avg_loss_gen: 2.216202994187673 (-0.023197929064432632)
| > avg_loss_kl: 1.7678057551383972 (+0.003246486186981201)
| > avg_loss_feat: 6.6186629931132 (+0.011463363965352968)
| > avg_loss_mel: 15.71893310546875 (+0.24421135584513287)
| > avg_loss_duration: 1.532705008983612 (+0.0006462037563323975)
| > avg_loss_1: 27.85430971781413 (+0.23636945088704664)
> EPOCH: 24/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:36:08)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 13:36:51 -- STEP: 79/630 -- GLOBAL_STEP: 892200
| > loss_disc: 2.4496335983276367 (2.560191335557382)
| > loss_disc_real_0: 0.1254006028175354 (0.16532723350992687)
| > loss_disc_real_1: 0.25151437520980835 (0.21667173240758195)
| > loss_disc_real_2: 0.16487927734851837 (0.2251586035082612)
| > loss_disc_real_3: 0.2551586925983429 (0.23402504396589496)
| > loss_disc_real_4: 0.26479706168174744 (0.240153246853925)
| > loss_disc_real_5: 0.24906928837299347 (0.22110917579524125)
| > loss_0: 2.4496335983276367 (2.560191335557382)
| > grad_norm_0: tensor(19.7371, device='cuda:0') (tensor(27.6022, device='cuda:0'))
| > loss_gen: 2.377375602722168 (2.2863251106648503)
| > loss_kl: 1.540795922279358 (1.539606273928775)
| > loss_feat: 6.9101691246032715 (7.142035828361029)
| > loss_mel: 15.592442512512207 (15.609358509884604)
| > loss_duration: 1.4678561687469482 (1.4346433063096642)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.888639450073242 (28.011969023113004)
| > grad_norm_1: tensor(131.0186, device='cuda:0') (tensor(354.7166, device='cuda:0'))
| > current_lr_0: 0.00019940086170989343
| > current_lr_1: 0.00019940086170989343
| > step_time: 0.5364 (0.5235586920871013)
| > loader_time: 0.0058 (0.00523210779021058)
--> TIME: 2025-05-14 13:37:50 -- STEP: 179/630 -- GLOBAL_STEP: 892300
| > loss_disc: 2.568108320236206 (2.5711176075748896)
| > loss_disc_real_0: 0.10500884056091309 (0.1671106490675963)
| > loss_disc_real_1: 0.1828179508447647 (0.21332836334265806)
| > loss_disc_real_2: 0.22070814669132233 (0.2257454627552512)
| > loss_disc_real_3: 0.19880756735801697 (0.2301037815196554)
| > loss_disc_real_4: 0.2154455929994583 (0.23852085026615824)
| > loss_disc_real_5: 0.22344838082790375 (0.22731317246759403)
| > loss_0: 2.568108320236206 (2.5711176075748896)
| > grad_norm_0: tensor(9.4836, device='cuda:0') (tensor(21.7735, device='cuda:0'))
| > loss_gen: 2.1180574893951416 (2.23638651757267)
| > loss_kl: 1.7388206720352173 (1.5768534224792565)
| > loss_feat: 6.820229530334473 (6.969730251994213)
| > loss_mel: 16.03732681274414 (15.489555273642088)
| > loss_duration: 1.4395644664764404 (1.3999013827499727)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.15399932861328 (27.67242674587825)
| > grad_norm_1: tensor(44.0881, device='cuda:0') (tensor(271.8749, device='cuda:0'))
| > current_lr_0: 0.00019940086170989343
| > current_lr_1: 0.00019940086170989343
| > step_time: 0.5905 (0.5569041734301178)
| > loader_time: 0.007 (0.005922221604672223)
--> TIME: 2025-05-14 13:38:55 -- STEP: 279/630 -- GLOBAL_STEP: 892400
| > loss_disc: 2.42195200920105 (2.577917036617101)
| > loss_disc_real_0: 0.1635759174823761 (0.167289646536005)
| > loss_disc_real_1: 0.21111717820167542 (0.21234440632618456)
| > loss_disc_real_2: 0.2309059202671051 (0.2279528025337445)
| > loss_disc_real_3: 0.23176603019237518 (0.23126731770226605)
| > loss_disc_real_4: 0.22945751249790192 (0.24036014646184914)
| > loss_disc_real_5: 0.1893680840730667 (0.22752231797437086)
| > loss_0: 2.42195200920105 (2.577917036617101)
| > grad_norm_0: tensor(47.2095, device='cuda:0') (tensor(21.8084, device='cuda:0'))
| > loss_gen: 2.385234832763672 (2.227526716006698)
| > loss_kl: 1.6130712032318115 (1.5973326207061822)
| > loss_feat: 7.552953243255615 (6.88879153890849)
| > loss_mel: 17.059486389160156 (15.47037402532434)
| > loss_duration: 1.4855835437774658 (1.403017902459722)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 30.096328735351562 (27.587042661550655)
| > grad_norm_1: tensor(410.9521, device='cuda:0') (tensor(266.7566, device='cuda:0'))
| > current_lr_0: 0.00019940086170989343
| > current_lr_1: 0.00019940086170989343
| > step_time: 0.6543 (0.5847421410263227)
| > loader_time: 0.0076 (0.006533682559980713)
--> TIME: 2025-05-14 13:40:05 -- STEP: 379/630 -- GLOBAL_STEP: 892500
| > loss_disc: 2.5036118030548096 (2.5764483166244223)
| > loss_disc_real_0: 0.1717599332332611 (0.16764298673119576)
| > loss_disc_real_1: 0.22274130582809448 (0.2126898014608348)
| > loss_disc_real_2: 0.2756887376308441 (0.22802749374453815)
| > loss_disc_real_3: 0.27115580439567566 (0.2308823748597369)
| > loss_disc_real_4: 0.24008089303970337 (0.23952535376699743)
| > loss_disc_real_5: 0.2344999462366104 (0.22672945357328356)
| > loss_0: 2.5036118030548096 (2.5764483166244223)
| > grad_norm_0: tensor(16.8725, device='cuda:0') (tensor(22.6872, device='cuda:0'))
| > loss_gen: 2.397099494934082 (2.2285622024913563)
| > loss_kl: 1.556849718093872 (1.611115695304166)
| > loss_feat: 6.378726482391357 (6.875169442008225)
| > loss_mel: 14.836872100830078 (15.453780974435933)
| > loss_duration: 1.4777708053588867 (1.4185376481833747)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.647319793701172 (27.587165842584696)
| > grad_norm_1: tensor(243.6609, device='cuda:0') (tensor(276.2766, device='cuda:0'))
| > current_lr_0: 0.00019940086170989343
| > current_lr_1: 0.00019940086170989343
| > step_time: 0.713 (0.6113307513788065)
| > loader_time: 0.0092 (0.007141598925426956)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_892500.pth
--> TIME: 2025-05-14 13:41:27 -- STEP: 479/630 -- GLOBAL_STEP: 892600
| > loss_disc: 2.559563159942627 (2.575916322636457)
| > loss_disc_real_0: 0.20617829263210297 (0.167248225271204)
| > loss_disc_real_1: 0.2650220990180969 (0.21287730202421018)
| > loss_disc_real_2: 0.2385183423757553 (0.22788398238462795)
| > loss_disc_real_3: 0.2752355635166168 (0.23089635449934107)
| > loss_disc_real_4: 0.2675914764404297 (0.2400068472098707)
| > loss_disc_real_5: 0.2203385829925537 (0.2272795187873233)
| > loss_0: 2.559563159942627 (2.575916322636457)
| > grad_norm_0: tensor(18.3153, device='cuda:0') (tensor(22.6190, device='cuda:0'))
| > loss_gen: 2.2004191875457764 (2.2279985824557063)
| > loss_kl: 1.495432734489441 (1.6143682291711796)
| > loss_feat: 6.6541290283203125 (6.851533863887904)
| > loss_mel: 15.686687469482422 (15.466478357733168)
| > loss_duration: 1.4596128463745117 (1.4208535038105878)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.496280670166016 (27.581232445225087)
| > grad_norm_1: tensor(403.4604, device='cuda:0') (tensor(276.1136, device='cuda:0'))
| > current_lr_0: 0.00019940086170989343
| > current_lr_1: 0.00019940086170989343
| > step_time: 0.8004 (0.644642941887045)
| > loader_time: 0.0091 (0.0077203718754842035)
--> TIME: 2025-05-14 13:42:57 -- STEP: 579/630 -- GLOBAL_STEP: 892700
| > loss_disc: 2.5087175369262695 (2.576530113944943)
| > loss_disc_real_0: 0.13554731011390686 (0.16767250370742529)
| > loss_disc_real_1: 0.18904609978199005 (0.21247038062475299)
| > loss_disc_real_2: 0.23593422770500183 (0.22825706923872702)
| > loss_disc_real_3: 0.2216615378856659 (0.23106944030842427)
| > loss_disc_real_4: 0.2205604463815689 (0.23995606557487)
| > loss_disc_real_5: 0.2233188897371292 (0.2264027106149415)
| > loss_0: 2.5087175369262695 (2.576530113944943)
| > grad_norm_0: tensor(19.0486, device='cuda:0') (tensor(22.7432, device='cuda:0'))
| > loss_gen: 2.184246301651001 (2.2270264353776814)
| > loss_kl: 1.5699611902236938 (1.6134498018469017)
| > loss_feat: 6.983954429626465 (6.81806026798044)
| > loss_mel: 15.908055305480957 (15.468477446798216)
| > loss_duration: 1.5008370876312256 (1.4287356321469897)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.14705467224121 (27.555749504471493)
| > grad_norm_1: tensor(241.4291, device='cuda:0') (tensor(279.7232, device='cuda:0'))
| > current_lr_0: 0.00019940086170989343
| > current_lr_1: 0.00019940086170989343
| > step_time: 0.964 (0.6861027370050985)
| > loader_time: 0.0145 (0.008303890574163723)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.0051739613215128575 (+0.0004562338193257647)
| > avg_loss_disc: 2.535228510697683 (+0.03629318873087595)
| > avg_loss_disc_real_0: 0.22166882827877998 (+0.07012153044342995)
| > avg_loss_disc_real_1: 0.20456891879439354 (+0.014763623476028442)
| > avg_loss_disc_real_2: 0.19886084025104842 (-0.07817459603150687)
| > avg_loss_disc_real_3: 0.25782539571324986 (+0.028697155416011838)
| > avg_loss_disc_real_4: 0.23588514948884645 (-0.024902671575546292)
| > avg_loss_disc_real_5: 0.23992516348759332 (+0.017855122685432434)
| > avg_loss_0: 2.535228510697683 (+0.03629318873087595)
| > avg_loss_gen: 2.243287732203801 (+0.027084738016128096)
| > avg_loss_kl: 1.8143297235171 (+0.046523968378702873)
| > avg_loss_feat: 6.461727658907573 (-0.15693533420562744)
| > avg_loss_mel: 15.49359162648519 (-0.2253414789835606)
| > avg_loss_duration: 1.5293051699797313 (-0.0033998390038807447)
| > avg_loss_1: 27.54224157333374 (-0.31206814448038855)
> EPOCH: 25/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:44:01)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 13:44:29 -- STEP: 49/630 -- GLOBAL_STEP: 892800
| > loss_disc: 2.5394883155822754 (2.5734404544441074)
| > loss_disc_real_0: 0.252113401889801 (0.1665809698098776)
| > loss_disc_real_1: 0.2001657336950302 (0.21203466215912176)
| > loss_disc_real_2: 0.25866612792015076 (0.22711754939994033)
| > loss_disc_real_3: 0.21893486380577087 (0.2342909267362283)
| > loss_disc_real_4: 0.24336272478103638 (0.24004414647209402)
| > loss_disc_real_5: 0.1857919692993164 (0.23133124867264104)
| > loss_0: 2.5394883155822754 (2.5734404544441074)
| > grad_norm_0: tensor(19.0034, device='cuda:0') (tensor(19.0386, device='cuda:0'))
| > loss_gen: 2.367680549621582 (2.267561099967178)
| > loss_kl: 1.514462947845459 (1.5533329491712609)
| > loss_feat: 7.365781784057617 (7.290323393685477)
| > loss_mel: 15.954742431640625 (15.570270032298808)
| > loss_duration: 1.4509087800979614 (1.435791018057843)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.653575897216797 (28.117278391001175)
| > grad_norm_1: tensor(601.8508, device='cuda:0') (tensor(249.3826, device='cuda:0'))
| > current_lr_0: 0.0001993759366021797
| > current_lr_1: 0.0001993759366021797
| > step_time: 0.5426 (0.5258935714254573)
| > loader_time: 0.0056 (0.005193092385116887)
--> TIME: 2025-05-14 13:45:26 -- STEP: 149/630 -- GLOBAL_STEP: 892900
| > loss_disc: 2.598405122756958 (2.5658583001002375)
| > loss_disc_real_0: 0.1887606978416443 (0.166742469265357)
| > loss_disc_real_1: 0.22057390213012695 (0.2124848138766001)
| > loss_disc_real_2: 0.20667403936386108 (0.22841921188687317)
| > loss_disc_real_3: 0.2380741387605667 (0.23023109448036091)
| > loss_disc_real_4: 0.2683013677597046 (0.24003044460843873)
| > loss_disc_real_5: 0.2351967841386795 (0.2256902210264398)
| > loss_0: 2.598405122756958 (2.5658583001002375)
| > grad_norm_0: tensor(7.1542, device='cuda:0') (tensor(21.4625, device='cuda:0'))
| > loss_gen: 2.0848379135131836 (2.261859371358117)
| > loss_kl: 1.6121609210968018 (1.5727014741641565)
| > loss_feat: 6.013556957244873 (7.045145847653383)
| > loss_mel: 16.756378173828125 (15.489524150054727)
| > loss_duration: 1.4154300689697266 (1.387534867197075)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.88236427307129 (27.756765660023518)
| > grad_norm_1: tensor(152.1048, device='cuda:0') (tensor(291.4995, device='cuda:0'))
| > current_lr_0: 0.0001993759366021797
| > current_lr_1: 0.0001993759366021797
| > step_time: 0.6063 (0.5468586195235282)
| > loader_time: 0.0074 (0.005704746950392758)
--> TIME: 2025-05-14 13:46:28 -- STEP: 249/630 -- GLOBAL_STEP: 893000
| > loss_disc: 2.6487929821014404 (2.566969094027479)
| > loss_disc_real_0: 0.2827165424823761 (0.16609308801322098)
| > loss_disc_real_1: 0.16978922486305237 (0.2114362266647768)
| > loss_disc_real_2: 0.23358368873596191 (0.2291397153134327)
| > loss_disc_real_3: 0.2631237506866455 (0.22960602734462324)
| > loss_disc_real_4: 0.203736811876297 (0.2395137349764506)
| > loss_disc_real_5: 0.20581944286823273 (0.22748592178744964)
| > loss_0: 2.6487929821014404 (2.566969094027479)
| > grad_norm_0: tensor(13.2329, device='cuda:0') (tensor(20.0036, device='cuda:0'))
| > loss_gen: 2.0750746726989746 (2.242674197537831)
| > loss_kl: 1.5943864583969116 (1.604235943062717)
| > loss_feat: 7.353593349456787 (6.969152804838127)
| > loss_mel: 15.78513240814209 (15.50129174228653)
| > loss_duration: 1.4290827512741089 (1.3951952189326766)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.23727035522461 (27.712549891337805)
| > grad_norm_1: tensor(135.6784, device='cuda:0') (tensor(254.0196, device='cuda:0'))
| > current_lr_0: 0.0001993759366021797
| > current_lr_1: 0.0001993759366021797
| > step_time: 0.6155 (0.5723299702487318)
| > loader_time: 0.0076 (0.00624189893883395)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_893000.pth
--> TIME: 2025-05-14 13:47:38 -- STEP: 349/630 -- GLOBAL_STEP: 893100
| > loss_disc: 2.415276527404785 (2.5723410984848165)
| > loss_disc_real_0: 0.20009660720825195 (0.16847071442272746)
| > loss_disc_real_1: 0.17552639544010162 (0.21201250610344732)
| > loss_disc_real_2: 0.17198039591312408 (0.22874909737561017)
| > loss_disc_real_3: 0.18976205587387085 (0.2289949558611244)
| > loss_disc_real_4: 0.24148768186569214 (0.2405962943176827)
| > loss_disc_real_5: 0.17704151570796967 (0.22674108794049752)
| > loss_0: 2.415276527404785 (2.5723410984848165)
| > grad_norm_0: tensor(35.8703, device='cuda:0') (tensor(19.6447, device='cuda:0'))
| > loss_gen: 2.669581174850464 (2.241000146442293)
| > loss_kl: 1.7263394594192505 (1.616507730716279)
| > loss_feat: 8.776947021484375 (6.917519416371867)
| > loss_mel: 16.150772094726562 (15.487957427016644)
| > loss_duration: 1.433473825454712 (1.4139015623354982)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 30.757112503051758 (27.67688626614545)
| > grad_norm_1: tensor(599.1036, device='cuda:0') (tensor(247.0874, device='cuda:0'))
| > current_lr_0: 0.0001993759366021797
| > current_lr_1: 0.0001993759366021797
| > step_time: 0.7153 (0.596814872200646)
| > loader_time: 0.0104 (0.0068022118598478915)
--> TIME: 2025-05-14 13:48:52 -- STEP: 449/630 -- GLOBAL_STEP: 893200
| > loss_disc: 2.6924571990966797 (2.5781474262144095)
| > loss_disc_real_0: 0.2174464762210846 (0.16903300073935357)
| > loss_disc_real_1: 0.20376244187355042 (0.21232303346451248)
| > loss_disc_real_2: 0.21075107157230377 (0.2286846012474434)
| > loss_disc_real_3: 0.18819455802440643 (0.22988272997610817)
| > loss_disc_real_4: 0.24462942779064178 (0.24071285659592506)
| > loss_disc_real_5: 0.22571979463100433 (0.22754974626751415)
| > loss_0: 2.6924571990966797 (2.5781474262144095)
| > grad_norm_0: tensor(30.6482, device='cuda:0') (tensor(21.2976, device='cuda:0'))
| > loss_gen: 2.0929102897644043 (2.2342119341703723)
| > loss_kl: 1.759830117225647 (1.6200484143599105)
| > loss_feat: 6.99064826965332 (6.8771930282524805)
| > loss_mel: 15.734223365783691 (15.47597147043139)
| > loss_duration: 1.4444859027862549 (1.417501851285752)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.0221004486084 (27.62492669239341)
| > grad_norm_1: tensor(448.7083, device='cuda:0') (tensor(263.1789, device='cuda:0'))
| > current_lr_0: 0.0001993759366021797
| > current_lr_1: 0.0001993759366021797
| > step_time: 0.7533 (0.6258973900087694)
| > loader_time: 0.0092 (0.00734468079887679)
--> TIME: 2025-05-14 13:50:16 -- STEP: 549/630 -- GLOBAL_STEP: 893300
| > loss_disc: 2.6218693256378174 (2.581584754971642)
| > loss_disc_real_0: 0.3054982125759125 (0.16989013421025215)
| > loss_disc_real_1: 0.20867034792900085 (0.21226087739124544)
| > loss_disc_real_2: 0.22148185968399048 (0.22855070233345032)
| > loss_disc_real_3: 0.2011033296585083 (0.22950896246185715)
| > loss_disc_real_4: 0.22966477274894714 (0.24037991116715693)
| > loss_disc_real_5: 0.25731655955314636 (0.22825171278691248)
| > loss_0: 2.6218693256378174 (2.581584754971642)
| > grad_norm_0: tensor(33.5861, device='cuda:0') (tensor(20.7943, device='cuda:0'))
| > loss_gen: 2.2132554054260254 (2.2223421254878915)
| > loss_kl: 1.5549870729446411 (1.6201849874034389)
| > loss_feat: 6.549464702606201 (6.812816145641556)
| > loss_mel: 15.330020904541016 (15.45380118462123)
| > loss_duration: 1.4764535427093506 (1.4259479710313145)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.124181747436523 (27.53509241114548)
| > grad_norm_1: tensor(250.9529, device='cuda:0') (tensor(256.9871, device='cuda:0'))
| > current_lr_0: 0.0001993759366021797
| > current_lr_1: 0.0001993759366021797
| > step_time: 0.9444 (0.6615392823036904)
| > loader_time: 0.0115 (0.007944542202141767)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005395412445068359 (+0.00022145112355550188)
| > avg_loss_disc: 2.6073222955067954 (+0.07209378480911255)
| > avg_loss_disc_real_0: 0.1588436538974444 (-0.06282517438133559)
| > avg_loss_disc_real_1: 0.17851862063010535 (-0.026050298164288194)
| > avg_loss_disc_real_2: 0.19548504054546356 (-0.003375799705584853)
| > avg_loss_disc_real_3: 0.2097185862561067 (-0.04810680945714316)
| > avg_loss_disc_real_4: 0.23695510625839233 (+0.0010699567695458823)
| > avg_loss_disc_real_5: 0.22283328200380007 (-0.01709188148379326)
| > avg_loss_0: 2.6073222955067954 (+0.07209378480911255)
| > avg_loss_gen: 1.8990122477213542 (-0.34427548448244694)
| > avg_loss_kl: 1.7195779780546825 (-0.0947517454624176)
| > avg_loss_feat: 6.205055832862854 (-0.2566718260447187)
| > avg_loss_mel: 15.43578815460205 (-0.05780347188313861)
| > avg_loss_duration: 1.5292454262574513 (-5.9743722280014566e-05)
| > avg_loss_1: 26.788679440816242 (-0.7535621325174979)
> BEST MODEL : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/best_model_893381.pth
> EPOCH: 26/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:51:54)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 13:52:05 -- STEP: 19/630 -- GLOBAL_STEP: 893400
| > loss_disc: 2.549625873565674 (2.554559431577984)
| > loss_disc_real_0: 0.1405792236328125 (0.1693875621023931)
| > loss_disc_real_1: 0.16271531581878662 (0.21215201757456126)
| > loss_disc_real_2: 0.22423651814460754 (0.2246891809137244)
| > loss_disc_real_3: 0.253535658121109 (0.22936825062099256)
| > loss_disc_real_4: 0.24418634176254272 (0.2385831992877157)
| > loss_disc_real_5: 0.23142971098423004 (0.2312984890059421)
| > loss_0: 2.549625873565674 (2.554559431577984)
| > grad_norm_0: tensor(49.9013, device='cuda:0') (tensor(24.6366, device='cuda:0'))
| > loss_gen: 2.275780439376831 (2.2565296198192395)
| > loss_kl: 1.4163769483566284 (1.4224435404727334)
| > loss_feat: 6.609110355377197 (6.875587764539216)
| > loss_mel: 15.441646575927734 (15.332055443211607)
| > loss_duration: 1.426713228225708 (1.4301150786249262)
| > amp_scaler: 256.0 (269.4736842105263)
| > loss_1: 27.169626235961914 (27.31673150313528)
| > grad_norm_1: tensor(541.4528, device='cuda:0') (tensor(332.2595, device='cuda:0'))
| > current_lr_0: 0.00019935101461010442
| > current_lr_1: 0.00019935101461010442
| > step_time: 0.5497 (0.5528375851480586)
| > loader_time: 0.0048 (0.005198804955733449)
--> TIME: 2025-05-14 13:53:02 -- STEP: 119/630 -- GLOBAL_STEP: 893500
| > loss_disc: 2.5719356536865234 (2.5809373074219013)
| > loss_disc_real_0: 0.23393823206424713 (0.16566687866168864)
| > loss_disc_real_1: 0.19228433072566986 (0.21512021800550093)
| > loss_disc_real_2: 0.24850700795650482 (0.23081098046122478)
| > loss_disc_real_3: 0.2333553582429886 (0.23022271442313155)
| > loss_disc_real_4: 0.19330118596553802 (0.2407452963730868)
| > loss_disc_real_5: 0.26490944623947144 (0.22462549154497996)
| > loss_0: 2.5719356536865234 (2.5809373074219013)
| > grad_norm_0: tensor(12.0578, device='cuda:0') (tensor(25.5013, device='cuda:0'))
| > loss_gen: 2.1734061241149902 (2.243967018207581)
| > loss_kl: 1.4873147010803223 (1.5947487815087584)
| > loss_feat: 6.398857593536377 (6.962650519459188)
| > loss_mel: 15.517060279846191 (15.323966731544303)
| > loss_duration: 1.4685230255126953 (1.4061811350974716)
| > amp_scaler: 256.0 (258.1512605042015)
| > loss_1: 27.045162200927734 (27.531514127715294)
| > grad_norm_1: tensor(45.3194, device='cuda:0') (tensor(326.3759, device='cuda:0'))
| > current_lr_0: 0.00019935101461010442
| > current_lr_1: 0.00019935101461010442
| > step_time: 0.5641 (0.5507614452297949)
| > loader_time: 0.0065 (0.005653108869280132)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_893500.pth
--> TIME: 2025-05-14 13:54:07 -- STEP: 219/630 -- GLOBAL_STEP: 893600
| > loss_disc: 2.6167197227478027 (2.580518429682136)
| > loss_disc_real_0: 0.21750010550022125 (0.16792932969250082)
| > loss_disc_real_1: 0.18010571599006653 (0.21484069750733573)
| > loss_disc_real_2: 0.3172585368156433 (0.22991217455090998)
| > loss_disc_real_3: 0.21923162043094635 (0.23025833580591906)
| > loss_disc_real_4: 0.19954395294189453 (0.24165601606510545)
| > loss_disc_real_5: 0.22048547863960266 (0.22327318631078555)
| > loss_0: 2.6167197227478027 (2.580518429682136)
| > grad_norm_0: tensor(21.1612, device='cuda:0') (tensor(24.3172, device='cuda:0'))
| > loss_gen: 2.4187281131744385 (2.2413769895083284)
| > loss_kl: 1.4059609174728394 (1.6103642776132174)
| > loss_feat: 7.665640354156494 (6.891126391005843)
| > loss_mel: 16.159029006958008 (15.38695524381176)
| > loss_duration: 1.485241174697876 (1.3821566768977198)
| > amp_scaler: 256.0 (257.1689497716895)
| > loss_1: 29.134597778320312 (27.511979630004326)
| > grad_norm_1: tensor(428.9087, device='cuda:0') (tensor(312.6104, device='cuda:0'))
| > current_lr_0: 0.00019935101461010442
| > current_lr_1: 0.00019935101461010442
| > step_time: 0.6094 (0.5786488916231618)
| > loader_time: 0.0073 (0.006201442518190708)
--> TIME: 2025-05-14 13:55:13 -- STEP: 319/630 -- GLOBAL_STEP: 893700
| > loss_disc: 2.5058603286743164 (2.573592185974123)
| > loss_disc_real_0: 0.28920555114746094 (0.16698069812081826)
| > loss_disc_real_1: 0.16154949367046356 (0.213706329278064)
| > loss_disc_real_2: 0.20499072968959808 (0.2284238693949571)
| > loss_disc_real_3: 0.195858895778656 (0.2297093611339043)
| > loss_disc_real_4: 0.1850840449333191 (0.24060242069552312)
| > loss_disc_real_5: 0.17580704391002655 (0.22347508501670205)
| > loss_0: 2.5058603286743164 (2.573592185974123)
| > grad_norm_0: tensor(19.2095, device='cuda:0') (tensor(24.4102, device='cuda:0'))
| > loss_gen: 2.2707507610321045 (2.2437733217466587)
| > loss_kl: 1.6005734205245972 (1.6151374582212925)
| > loss_feat: 6.694543361663818 (6.862995436199033)
| > loss_mel: 15.51902961730957 (15.42045081446537)
| > loss_duration: 1.486216425895691 (1.4074781340865135)
| > amp_scaler: 128.0 (218.2821316614421)
| > loss_1: 27.57111167907715 (27.54983524693217)
| > grad_norm_1: tensor(275.4962, device='cuda:0') (tensor(310.3579, device='cuda:0'))
| > current_lr_0: 0.00019935101461010442
| > current_lr_1: 0.00019935101461010442
| > step_time: 0.6683 (0.598225761730469)
| > loader_time: 0.0087 (0.006762057636225112)
--> TIME: 2025-05-14 13:56:25 -- STEP: 419/630 -- GLOBAL_STEP: 893800
| > loss_disc: 2.606405258178711 (2.5726096254544517)
| > loss_disc_real_0: 0.139694482088089 (0.1668712828743999)
| > loss_disc_real_1: 0.2473660707473755 (0.21342960874903458)
| > loss_disc_real_2: 0.21431973576545715 (0.2276200928807543)
| > loss_disc_real_3: 0.25996914505958557 (0.2294875907229353)
| > loss_disc_real_4: 0.21859581768512726 (0.24000684113235063)
| > loss_disc_real_5: 0.21903377771377563 (0.22612570396897902)
| > loss_0: 2.606405258178711 (2.5726096254544517)
| > grad_norm_0: tensor(36.3870, device='cuda:0') (tensor(22.0319, device='cuda:0'))
| > loss_gen: 2.2330005168914795 (2.230734130363191)
| > loss_kl: 1.529077410697937 (1.6204429466570764)
| > loss_feat: 6.889566421508789 (6.814829545260045)
| > loss_mel: 15.183241844177246 (15.409383332245675)
| > loss_duration: 1.4515154361724854 (1.4115022139219227)
| > amp_scaler: 128.0 (196.73508353221965)
| > loss_1: 27.286401748657227 (27.486892258637276)
| > grad_norm_1: tensor(318.4008, device='cuda:0') (tensor(273.3612, device='cuda:0'))
| > current_lr_0: 0.00019935101461010442
| > current_lr_1: 0.00019935101461010442
| > step_time: 0.7379 (0.6251133796992333)
| > loader_time: 0.0098 (0.007320434210693068)
--> TIME: 2025-05-14 13:57:45 -- STEP: 519/630 -- GLOBAL_STEP: 893900
| > loss_disc: 2.5590505599975586 (2.573438126227761)
| > loss_disc_real_0: 0.21822497248649597 (0.16692428807647247)
| > loss_disc_real_1: 0.184295192360878 (0.21371228233525288)
| > loss_disc_real_2: 0.24500514566898346 (0.2278613063698789)
| > loss_disc_real_3: 0.22521163523197174 (0.22972877530348784)
| > loss_disc_real_4: 0.27040886878967285 (0.24008334036162823)
| > loss_disc_real_5: 0.2568376660346985 (0.22669974121629388)
| > loss_0: 2.5590505599975586 (2.573438126227761)
| > grad_norm_0: tensor(12.9392, device='cuda:0') (tensor(20.6384, device='cuda:0'))
| > loss_gen: 2.25132417678833 (2.227827523944466)
| > loss_kl: 1.5879237651824951 (1.6164855878936535)
| > loss_feat: 6.050282955169678 (6.7963450418961076)
| > loss_mel: 15.46203899383545 (15.419004502783391)
| > loss_duration: 1.4436250925064087 (1.4216159244493256)
| > amp_scaler: 128.0 (183.49132947976884)
| > loss_1: 26.795194625854492 (27.481278641834884)
| > grad_norm_1: tensor(116.4640, device='cuda:0') (tensor(254.0692, device='cuda:0'))
| > current_lr_0: 0.00019935101461010442
| > current_lr_1: 0.00019935101461010442
| > step_time: 0.8534 (0.6562635848058209)
| > loader_time: 0.0104 (0.007832928659369262)
--> TIME: 2025-05-14 13:59:24 -- STEP: 619/630 -- GLOBAL_STEP: 894000
| > loss_disc: 2.5044631958007812 (2.5703288064442087)
| > loss_disc_real_0: 0.17165090143680573 (0.1664656647669095)
| > loss_disc_real_1: 0.2347671389579773 (0.21336964298767871)
| > loss_disc_real_2: 0.25497475266456604 (0.2280830311948533)
| > loss_disc_real_3: 0.22518043220043182 (0.22954459286179035)
| > loss_disc_real_4: 0.2464902400970459 (0.23990965132663247)
| > loss_disc_real_5: 0.22824804484844208 (0.22593712958361298)
| > loss_0: 2.5044631958007812 (2.5703288064442087)
| > grad_norm_0: tensor(35.8421, device='cuda:0') (tensor(21.0574, device='cuda:0'))
| > loss_gen: 2.450899600982666 (2.2336528253093095)
| > loss_kl: 1.5653245449066162 (1.6146950506047024)
| > loss_feat: 7.283891201019287 (6.80102929314042)
| > loss_mel: 15.814393043518066 (15.438343448669729)
| > loss_duration: 1.5300953388214111 (1.4301712942431546)
| > amp_scaler: 128.0 (174.52665589660754)
| > loss_1: 28.644603729248047 (27.517891959342883)
| > grad_norm_1: tensor(837.7761, device='cuda:0') (tensor(258.0875, device='cuda:0'))
| > current_lr_0: 0.00019935101461010442
| > current_lr_1: 0.00019935101461010442
| > step_time: 1.2109 (0.707457216953037)
| > loader_time: 0.0154 (0.008510416659476876)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_894000.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005273779233296712 (-0.00012163321177164742)
| > avg_loss_disc: 2.522285004456838 (-0.08503729104995728)
| > avg_loss_disc_real_0: 0.1442653133223454 (-0.014578340575098991)
| > avg_loss_disc_real_1: 0.17139596616228422 (-0.007122654467821121)
| > avg_loss_disc_real_2: 0.18940273796518645 (-0.006082302580277116)
| > avg_loss_disc_real_3: 0.22096187248826027 (+0.011243286232153565)
| > avg_loss_disc_real_4: 0.23676555479566255 (-0.00018955146272978118)
| > avg_loss_disc_real_5: 0.24566969027121863 (+0.022836408267418562)
| > avg_loss_0: 2.522285004456838 (-0.08503729104995728)
| > avg_loss_gen: 2.0537258187929788 (+0.15471357107162453)
| > avg_loss_kl: 1.7379916906356812 (+0.018413712580998665)
| > avg_loss_feat: 6.223216533660889 (+0.018160700798034668)
| > avg_loss_mel: 15.216332991917929 (-0.21945516268412213)
| > avg_loss_duration: 1.5298860867818196 (+0.0006406605243682861)
| > avg_loss_1: 26.76115306218465 (-0.027526378631591797)
> BEST MODEL : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/best_model_894011.pth
> EPOCH: 27/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 13:59:55)
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
যদি লিভের আবেদন
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:00:45 -- STEP: 89/630 -- GLOBAL_STEP: 894100
| > loss_disc: 2.5677289962768555 (2.5832440424501235)
| > loss_disc_real_0: 0.0941711887717247 (0.16559753859980725)
| > loss_disc_real_1: 0.1725863367319107 (0.21239188681827503)
| > loss_disc_real_2: 0.17287816107273102 (0.22718310448225965)
| > loss_disc_real_3: 0.21631093323230743 (0.23037607833910523)
| > loss_disc_real_4: 0.2243182361125946 (0.23832319208075492)
| > loss_disc_real_5: 0.22078734636306763 (0.23467730906572234)
| > loss_0: 2.5677289962768555 (2.5832440424501235)
| > grad_norm_0: tensor(6.8641, device='cuda:0') (tensor(13.3966, device='cuda:0'))
| > loss_gen: 2.1587777137756348 (2.217611387874304)
| > loss_kl: 1.4864838123321533 (1.5342122919104073)
| > loss_feat: 7.067257404327393 (7.01992910899473)
| > loss_mel: 15.05163288116455 (15.481766807899046)
| > loss_duration: 1.433026671409607 (1.4362209941563988)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.19717788696289 (27.6897408131803)
| > grad_norm_1: tensor(54.7561, device='cuda:0') (tensor(151.9429, device='cuda:0'))
| > current_lr_0: 0.00019932609573327815
| > current_lr_1: 0.00019932609573327815
| > step_time: 0.5314 (0.5391824406184508)
| > loader_time: 0.0054 (0.005355146493804591)
--> TIME: 2025-05-14 14:01:44 -- STEP: 189/630 -- GLOBAL_STEP: 894200
| > loss_disc: 2.6545281410217285 (2.5680161052280015)
| > loss_disc_real_0: 0.23078209161758423 (0.16510166760001857)
| > loss_disc_real_1: 0.24672414362430573 (0.2119437344175167)
| > loss_disc_real_2: 0.21327397227287292 (0.2266873519020106)
| > loss_disc_real_3: 0.23152673244476318 (0.22910589090100042)
| > loss_disc_real_4: 0.170954167842865 (0.23725086119439867)
| > loss_disc_real_5: 0.2265065759420395 (0.2311006528202188)
| > loss_0: 2.6545281410217285 (2.5680161052280015)
| > grad_norm_0: tensor(35.2875, device='cuda:0') (tensor(18.8377, device='cuda:0'))
| > loss_gen: 2.1433310508728027 (2.234196203726311)
| > loss_kl: 1.7170859575271606 (1.5678539225664094)
| > loss_feat: 7.4810309410095215 (6.995018328308428)
| > loss_mel: 15.407057762145996 (15.521943622165256)
| > loss_duration: 1.4368923902511597 (1.3955074220738088)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.18539810180664 (27.714519551191387)
| > grad_norm_1: tensor(200.4768, device='cuda:0') (tensor(226.0314, device='cuda:0'))
| > current_lr_0: 0.00019932609573327815
| > current_lr_1: 0.00019932609573327815
| > step_time: 0.58 (0.5586714113830895)
| > loader_time: 0.0063 (0.005839041301182338)
--> TIME: 2025-05-14 14:02:47 -- STEP: 289/630 -- GLOBAL_STEP: 894300
| > loss_disc: 2.527235269546509 (2.568113812938281)
| > loss_disc_real_0: 0.1371433436870575 (0.16629308954551553)
| > loss_disc_real_1: 0.21884502470493317 (0.21132409758221324)
| > loss_disc_real_2: 0.2048213928937912 (0.22600948405822668)
| > loss_disc_real_3: 0.22641345858573914 (0.2300300886886755)
| > loss_disc_real_4: 0.2505433261394501 (0.23859900298003095)
| > loss_disc_real_5: 0.23990540206432343 (0.2298096231729514)
| > loss_0: 2.527235269546509 (2.568113812938281)
| > grad_norm_0: tensor(22.7295, device='cuda:0') (tensor(20.4249, device='cuda:0'))
| > loss_gen: 2.111034393310547 (2.2402697710842427)
| > loss_kl: 1.7663902044296265 (1.5930882510841928)
| > loss_feat: 6.726494312286377 (6.946313516491425)
| > loss_mel: 15.062750816345215 (15.526856706216673)
| > loss_duration: 1.4506149291992188 (1.399229332237508)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.117284774780273 (27.705757669099057)
| > grad_norm_1: tensor(306.6739, device='cuda:0') (tensor(247.7672, device='cuda:0'))
| > current_lr_0: 0.00019932609573327815
| > current_lr_1: 0.00019932609573327815
| > step_time: 0.6411 (0.5812818616319287)
| > loader_time: 0.0082 (0.0064382412854362935)
--> TIME: 2025-05-14 14:03:56 -- STEP: 389/630 -- GLOBAL_STEP: 894400
| > loss_disc: 2.6409833431243896 (2.574537438414704)
| > loss_disc_real_0: 0.13147039711475372 (0.1662301372707963)
| > loss_disc_real_1: 0.24324560165405273 (0.21168594384101486)
| > loss_disc_real_2: 0.25442102551460266 (0.22686907750551988)
| > loss_disc_real_3: 0.24939410388469696 (0.23054699607404155)
| > loss_disc_real_4: 0.24666890501976013 (0.23908762082189397)
| > loss_disc_real_5: 0.2611996531486511 (0.22981780598892956)
| > loss_0: 2.6409833431243896 (2.574537438414704)
| > grad_norm_0: tensor(22.5398, device='cuda:0') (tensor(20.5892, device='cuda:0'))
| > loss_gen: 2.3552913665771484 (2.232875443362946)
| > loss_kl: 1.582982063293457 (1.5990332291487865)
| > loss_feat: 6.587188720703125 (6.908449910906717)
| > loss_mel: 15.590124130249023 (15.510121921647178)
| > loss_duration: 1.4660383462905884 (1.4140358697479378)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.58162498474121 (27.664516434264975)
| > grad_norm_1: tensor(508.1290, device='cuda:0') (tensor(245.0278, device='cuda:0'))
| > current_lr_0: 0.00019932609573327815
| > current_lr_1: 0.00019932609573327815
| > step_time: 0.7066 (0.605114323314481)
| > loader_time: 0.0083 (0.006951595639814753)
--> TIME: 2025-05-14 14:05:13 -- STEP: 489/630 -- GLOBAL_STEP: 894500
| > loss_disc: 2.644747734069824 (2.5821796945755224)
| > loss_disc_real_0: 0.17494583129882812 (0.1669678629084599)
| > loss_disc_real_1: 0.3472725450992584 (0.21183860067331475)
| > loss_disc_real_2: 0.2675691843032837 (0.22784515284382736)
| > loss_disc_real_3: 0.27444392442703247 (0.2308724519543365)
| > loss_disc_real_4: 0.2598419189453125 (0.2397376592966189)
| > loss_disc_real_5: 0.2727237045764923 (0.23212084384417972)
| > loss_0: 2.644747734069824 (2.5821796945755224)
| > grad_norm_0: tensor(17.1799, device='cuda:0') (tensor(19.4249, device='cuda:0'))
| > loss_gen: 2.4464378356933594 (2.2257841472001667)
| > loss_kl: 1.6964823007583618 (1.6030497156037877)
| > loss_feat: 6.837000846862793 (6.860147568833366)
| > loss_mel: 15.6535062789917 (15.511683249522328)
| > loss_duration: 1.455643653869629 (1.415985494303558)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.089069366455078 (27.616650224463335)
| > grad_norm_1: tensor(182.2418, device='cuda:0') (tensor(228.3878, device='cuda:0'))
| > current_lr_0: 0.00019932609573327815
| > current_lr_1: 0.00019932609573327815
| > step_time: 0.8047 (0.6356004400974894)
| > loader_time: 0.0101 (0.007460453758941837)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_894500.pth
--> TIME: 2025-05-14 14:06:45 -- STEP: 589/630 -- GLOBAL_STEP: 894600
| > loss_disc: 2.6180837154388428 (2.583149000015647)
| > loss_disc_real_0: 0.16217514872550964 (0.16796501388169302)
| > loss_disc_real_1: 0.2653869688510895 (0.21189771276378466)
| > loss_disc_real_2: 0.25820156931877136 (0.22834270009818425)
| > loss_disc_real_3: 0.2759656310081482 (0.2302873731924439)
| > loss_disc_real_4: 0.2635432481765747 (0.2400169764947405)
| > loss_disc_real_5: 0.18336327373981476 (0.2317163911355574)
| > loss_0: 2.6180837154388428 (2.583149000015647)
| > grad_norm_0: tensor(9.8432, device='cuda:0') (tensor(19.3664, device='cuda:0'))
| > loss_gen: 2.0957083702087402 (2.22190255463022)
| > loss_kl: 1.7349082231521606 (1.6076986648028495)
| > loss_feat: 5.5572028160095215 (6.816665256772259)
| > loss_mel: 15.48355484008789 (15.517861779153044)
| > loss_duration: 1.4698240756988525 (1.424384816797967)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.341197967529297 (27.588513100693714)
| > grad_norm_1: tensor(159.8746, device='cuda:0') (tensor(227.6174, device='cuda:0'))
| > current_lr_0: 0.00019932609573327815
| > current_lr_1: 0.00019932609573327815
| > step_time: 1.0355 (0.6769659001070293)
| > loader_time: 0.013 (0.008049839016537108)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005202571551005046 (-7.120768229166609e-05)
| > avg_loss_disc: 2.6989572842915854 (+0.17667227983474731)
| > avg_loss_disc_real_0: 0.21026518568396568 (+0.06599987236162028)
| > avg_loss_disc_real_1: 0.21350008870164552 (+0.0421041225393613)
| > avg_loss_disc_real_2: 0.19280093908309937 (+0.003398201117912919)
| > avg_loss_disc_real_3: 0.25457438329855603 (+0.03361251081029576)
| > avg_loss_disc_real_4: 0.21826023111740747 (-0.01850532367825508)
| > avg_loss_disc_real_5: 0.20293784017364183 (-0.042731850097576796)
| > avg_loss_0: 2.6989572842915854 (+0.17667227983474731)
| > avg_loss_gen: 1.9497977097829182 (-0.10392810901006055)
| > avg_loss_kl: 1.8289323846499126 (+0.09094069401423144)
| > avg_loss_feat: 6.662873148918152 (+0.4396566152572632)
| > avg_loss_mel: 15.92339563369751 (+0.7070626417795811)
| > avg_loss_duration: 1.5392732123533885 (+0.009387125571568955)
| > avg_loss_1: 27.904272238413494 (+1.1431191762288435)
> EPOCH: 28/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 14:07:41)
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:08:13 -- STEP: 59/630 -- GLOBAL_STEP: 894700
| > loss_disc: 2.5045204162597656 (2.5679217435545847)
| > loss_disc_real_0: 0.20781771838665009 (0.1742496815020755)
| > loss_disc_real_1: 0.19793309271335602 (0.213518803655091)
| > loss_disc_real_2: 0.21053257584571838 (0.2244574846857685)
| > loss_disc_real_3: 0.20812630653381348 (0.22486118441921168)
| > loss_disc_real_4: 0.21115727722644806 (0.23832320560843256)
| > loss_disc_real_5: 0.2004176527261734 (0.22050474180003343)
| > loss_0: 2.5045204162597656 (2.5679217435545847)
| > grad_norm_0: tensor(36.0208, device='cuda:0') (tensor(29.8075, device='cuda:0'))
| > loss_gen: 2.37811541557312 (2.2568139868267507)
| > loss_kl: 1.8039168119430542 (1.533085592722489)
| > loss_feat: 7.731781005859375 (7.146505468982761)
| > loss_mel: 15.383301734924316 (15.676316713882706)
| > loss_duration: 1.4453880786895752 (1.4270807605678753)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.742502212524414 (28.03980255126953)
| > grad_norm_1: tensor(477.6235, device='cuda:0') (tensor(384.1807, device='cuda:0'))
| > current_lr_0: 0.0001993011799713115
| > current_lr_1: 0.0001993011799713115
| > step_time: 0.5362 (0.5204879914299917)
| > loader_time: 0.0062 (0.00510347091545493)
--> TIME: 2025-05-14 14:09:10 -- STEP: 159/630 -- GLOBAL_STEP: 894800
| > loss_disc: 2.666640520095825 (2.5907527035887123)
| > loss_disc_real_0: 0.20960590243339539 (0.17348683883184163)
| > loss_disc_real_1: 0.23677273094654083 (0.21411696470008706)
| > loss_disc_real_2: 0.2378203123807907 (0.22714649590681185)
| > loss_disc_real_3: 0.2216479480266571 (0.2304960570807727)
| > loss_disc_real_4: 0.259529709815979 (0.24135806013203268)
| > loss_disc_real_5: 0.28263944387435913 (0.22973087308166912)
| > loss_0: 2.666640520095825 (2.5907527035887123)
| > grad_norm_0: tensor(12.6162, device='cuda:0') (tensor(26.2019, device='cuda:0'))
| > loss_gen: 2.2116270065307617 (2.236054106328473)
| > loss_kl: 1.0934131145477295 (1.552537454749054)
| > loss_feat: 5.932989597320557 (6.982803296742949)
| > loss_mel: 15.2632417678833 (15.588893218610272)
| > loss_duration: 1.4509385824203491 (1.384305790535309)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 25.95220947265625 (27.744593746257273)
| > grad_norm_1: tensor(90.8011, device='cuda:0') (tensor(326.3665, device='cuda:0'))
| > current_lr_0: 0.0001993011799713115
| > current_lr_1: 0.0001993011799713115
| > step_time: 0.5636 (0.5470815064772122)
| > loader_time: 0.0064 (0.005662534221913079)
--> TIME: 2025-05-14 14:10:11 -- STEP: 259/630 -- GLOBAL_STEP: 894900
| > loss_disc: 2.5473580360412598 (2.593602023069463)
| > loss_disc_real_0: 0.10044188052415848 (0.17349501960986374)
| > loss_disc_real_1: 0.19221210479736328 (0.2136402589819146)
| > loss_disc_real_2: 0.2237100452184677 (0.2275184126549246)
| > loss_disc_real_3: 0.2318628877401352 (0.2292835208439919)
| > loss_disc_real_4: 0.22971005737781525 (0.24005549018447464)
| > loss_disc_real_5: 0.26549509167671204 (0.2315923104990403)
| > loss_0: 2.5473580360412598 (2.593602023069463)
| > grad_norm_0: tensor(11.2641, device='cuda:0') (tensor(21.6852, device='cuda:0'))
| > loss_gen: 2.276172399520874 (2.210513123674281)
| > loss_kl: 1.7830767631530762 (1.573916338585519)
| > loss_feat: 7.360772609710693 (6.869665696353986)
| > loss_mel: 15.708767890930176 (15.57840278802231)
| > loss_duration: 1.468316912651062 (1.3939614664173494)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.59710693359375 (27.62645930581111)
| > grad_norm_1: tensor(277.5322, device='cuda:0') (tensor(259.5237, device='cuda:0'))
| > current_lr_0: 0.0001993011799713115
| > current_lr_1: 0.0001993011799713115
| > step_time: 0.6029 (0.5649048425976377)
| > loader_time: 0.007 (0.006213181727641335)
--> TIME: 2025-05-14 14:11:15 -- STEP: 359/630 -- GLOBAL_STEP: 895000
| > loss_disc: 2.585083484649658 (2.587473695324658)
| > loss_disc_real_0: 0.21131455898284912 (0.17249504153027828)
| > loss_disc_real_1: 0.174115389585495 (0.2132790407845569)
| > loss_disc_real_2: 0.219455748796463 (0.22757428104166866)
| > loss_disc_real_3: 0.21732445061206818 (0.22942441527557905)
| > loss_disc_real_4: 0.22894158959388733 (0.2399854657958809)
| > loss_disc_real_5: 0.2711358964443207 (0.22984134710930848)
| > loss_0: 2.585083484649658 (2.587473695324658)
| > grad_norm_0: tensor(15.5966, device='cuda:0') (tensor(22.4192, device='cuda:0'))
| > loss_gen: 2.098353385925293 (2.2205178146574824)
| > loss_kl: 1.7614009380340576 (1.5812828288436929)
| > loss_feat: 7.088401794433594 (6.8450320397910955)
| > loss_mel: 15.776224136352539 (15.537450243171543)
| > loss_duration: 1.4752357006072998 (1.4121298076050524)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.199615478515625 (27.59641264806551)
| > grad_norm_1: tensor(123.0370, device='cuda:0') (tensor(270.5168, device='cuda:0'))
| > current_lr_0: 0.0001993011799713115
| > current_lr_1: 0.0001993011799713115
| > step_time: 0.6483 (0.5825143637431369)
| > loader_time: 0.0079 (0.006732390783623398)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_895000.pth
--> TIME: 2025-05-14 14:12:30 -- STEP: 459/630 -- GLOBAL_STEP: 895100
| > loss_disc: 2.528414487838745 (2.584880705752406)
| > loss_disc_real_0: 0.18887893855571747 (0.1719691316741224)
| > loss_disc_real_1: 0.20222234725952148 (0.2124339821941193)
| > loss_disc_real_2: 0.2438184767961502 (0.22728932978410865)
| > loss_disc_real_3: 0.21780647337436676 (0.2288986541217189)
| > loss_disc_real_4: 0.24388763308525085 (0.2397290144870484)
| > loss_disc_real_5: 0.2381303608417511 (0.23084824059913361)
| > loss_0: 2.528414487838745 (2.584880705752406)
| > grad_norm_0: tensor(10.9716, device='cuda:0') (tensor(21.4652, device='cuda:0'))
| > loss_gen: 2.2065207958221436 (2.218483671643379)
| > loss_kl: 1.7004987001419067 (1.584812807101829)
| > loss_feat: 6.618616580963135 (6.826438760445787)
| > loss_mel: 15.840658187866211 (15.544654374548553)
| > loss_duration: 1.4139573574066162 (1.4141286406381972)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.78025245666504 (27.588518196720962)
| > grad_norm_1: tensor(130.5781, device='cuda:0') (tensor(249.6866, device='cuda:0'))
| > current_lr_0: 0.0001993011799713115
| > current_lr_1: 0.0001993011799713115
| > step_time: 0.7969 (0.6103191183543161)
| > loader_time: 0.0093 (0.007255422783313491)
--> TIME: 2025-05-14 14:13:53 -- STEP: 559/630 -- GLOBAL_STEP: 895200
| > loss_disc: 2.6158013343811035 (2.5844753138281162)
| > loss_disc_real_0: 0.1978832185268402 (0.17201228391825618)
| > loss_disc_real_1: 0.20682136714458466 (0.21168630027707025)
| > loss_disc_real_2: 0.251901775598526 (0.2275729628816274)
| > loss_disc_real_3: 0.2470848709344864 (0.2290628748631008)
| > loss_disc_real_4: 0.34149542450904846 (0.23957701472562198)
| > loss_disc_real_5: 0.20431113243103027 (0.23180004557151487)
| > loss_0: 2.6158013343811035 (2.5844753138281162)
| > grad_norm_0: tensor(9.0554, device='cuda:0') (tensor(19.9265, device='cuda:0'))
| > loss_gen: 2.3224921226501465 (2.2151409242575437)
| > loss_kl: 1.521057367324829 (1.5861147072745991)
| > loss_feat: 7.284184455871582 (6.8106312308200545)
| > loss_mel: 15.664324760437012 (15.533660093658938)
| > loss_duration: 1.4864933490753174 (1.4230793036373866)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.278553009033203 (27.56862621955667)
| > grad_norm_1: tensor(119.3670, device='cuda:0') (tensor(227.1752, device='cuda:0'))
| > current_lr_0: 0.0001993011799713115
| > current_lr_1: 0.0001993011799713115
| > step_time: 0.8635 (0.6457573749085025)
| > loader_time: 0.0122 (0.007837753176475892)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005352218945821126 (+0.00014964739481608015)
| > avg_loss_disc: 2.590180218219757 (-0.10877706607182835)
| > avg_loss_disc_real_0: 0.1609876248985529 (-0.04927756078541279)
| > avg_loss_disc_real_1: 0.2238335261742274 (+0.010333437472581863)
| > avg_loss_disc_real_2: 0.2520638604958852 (+0.05926292141278583)
| > avg_loss_disc_real_3: 0.21293373281757036 (-0.04164065048098567)
| > avg_loss_disc_real_4: 0.23162572210033736 (+0.013365490982929884)
| > avg_loss_disc_real_5: 0.24721476684014002 (+0.044276926666498184)
| > avg_loss_0: 2.590180218219757 (-0.10877706607182835)
| > avg_loss_gen: 2.12803324063619 (+0.1782355308532717)
| > avg_loss_kl: 1.717425376176834 (-0.11150700847307848)
| > avg_loss_feat: 6.499409278233846 (-0.16346387068430612)
| > avg_loss_mel: 15.328961849212646 (-0.5944337844848633)
| > avg_loss_duration: 1.5242623488108318 (-0.015010863542556763)
| > avg_loss_1: 27.198091824849445 (-0.7061804135640486)
> EPOCH: 29/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 14:15:14)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:15:31 -- STEP: 29/630 -- GLOBAL_STEP: 895300
| > loss_disc: 2.770977735519409 (2.587538324553391)
| > loss_disc_real_0: 0.21877139806747437 (0.17394947851526324)
| > loss_disc_real_1: 0.220976784825325 (0.2154935218136886)
| > loss_disc_real_2: 0.22721631824970245 (0.23018128450574546)
| > loss_disc_real_3: 0.3393315076828003 (0.23096890130947376)
| > loss_disc_real_4: 0.26138269901275635 (0.23685493089001755)
| > loss_disc_real_5: 0.23350368440151215 (0.23151773419873467)
| > loss_0: 2.770977735519409 (2.587538324553391)
| > grad_norm_0: tensor(24.3267, device='cuda:0') (tensor(24.2653, device='cuda:0'))
| > loss_gen: 2.1547749042510986 (2.215526095752059)
| > loss_kl: 1.7683271169662476 (1.5754655846234025)
| > loss_feat: 7.136878490447998 (6.883174452288397)
| > loss_mel: 15.52764892578125 (15.627282043983197)
| > loss_duration: 1.3928256034851074 (1.4216468868584469)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.98045539855957 (27.72309507172683)
| > grad_norm_1: tensor(198.8776, device='cuda:0') (tensor(322.0692, device='cuda:0'))
| > current_lr_0: 0.00019927626732381507
| > current_lr_1: 0.00019927626732381507
| > step_time: 0.5438 (0.5289263807494065)
| > loader_time: 0.0055 (0.004910904785682415)
--> TIME: 2025-05-14 14:16:26 -- STEP: 129/630 -- GLOBAL_STEP: 895400
| > loss_disc: 2.6044716835021973 (2.5782894847929017)
| > loss_disc_real_0: 0.11463948339223862 (0.1681481528189755)
| > loss_disc_real_1: 0.21433113515377045 (0.21301883025917895)
| > loss_disc_real_2: 0.21250048279762268 (0.2282314778760422)
| > loss_disc_real_3: 0.17495469748973846 (0.2281581337830817)
| > loss_disc_real_4: 0.24711468815803528 (0.24092493489269137)
| > loss_disc_real_5: 0.22713473439216614 (0.23500759922718817)
| > loss_0: 2.6044716835021973 (2.5782894847929017)
| > grad_norm_0: tensor(6.9347, device='cuda:0') (tensor(17.0103, device='cuda:0'))
| > loss_gen: 2.287511110305786 (2.2066994156948363)
| > loss_kl: 1.8115170001983643 (1.5803090832954234)
| > loss_feat: 7.192992687225342 (6.846309488133866)
| > loss_mel: 15.238046646118164 (15.478057262509369)
| > loss_duration: 1.489389419555664 (1.4045683736949004)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.019458770751953 (27.515943571578624)
| > grad_norm_1: tensor(69.1905, device='cuda:0') (tensor(202.7068, device='cuda:0'))
| > current_lr_0: 0.00019927626732381507
| > current_lr_1: 0.00019927626732381507
| > step_time: 0.5512 (0.5429940168247662)
| > loader_time: 0.0064 (0.005544527556545051)
--> TIME: 2025-05-14 14:17:27 -- STEP: 229/630 -- GLOBAL_STEP: 895500
| > loss_disc: 2.537306785583496 (2.592810706800769)
| > loss_disc_real_0: 0.1757846474647522 (0.17121619392820836)
| > loss_disc_real_1: 0.18056756258010864 (0.2128550337717002)
| > loss_disc_real_2: 0.2731165289878845 (0.22902301598063723)
| > loss_disc_real_3: 0.27980390191078186 (0.22907493487976524)
| > loss_disc_real_4: 0.2223661243915558 (0.24138881578455845)
| > loss_disc_real_5: 0.21075275540351868 (0.23580046336463445)
| > loss_0: 2.537306785583496 (2.592810706800769)
| > grad_norm_0: tensor(15.4997, device='cuda:0') (tensor(14.8767, device='cuda:0'))
| > loss_gen: 2.322075843811035 (2.192859235809358)
| > loss_kl: 1.7202351093292236 (1.5947626475163423)
| > loss_feat: 7.857972145080566 (6.803605748055804)
| > loss_mel: 15.920849800109863 (15.506325721740723)
| > loss_duration: 1.4607415199279785 (1.3771071303879854)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 29.28187370300293 (27.47466040698722)
| > grad_norm_1: tensor(207.7351, device='cuda:0') (tensor(162.8466, device='cuda:0'))
| > current_lr_0: 0.00019927626732381507
| > current_lr_1: 0.00019927626732381507
| > step_time: 0.6198 (0.567051090007265)
| > loader_time: 0.0079 (0.006102354765979484)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_895500.pth
--> TIME: 2025-05-14 14:18:35 -- STEP: 329/630 -- GLOBAL_STEP: 895600
| > loss_disc: 2.7929582595825195 (2.5884861960599466)
| > loss_disc_real_0: 0.22252371907234192 (0.17151144227313042)
| > loss_disc_real_1: 0.26294025778770447 (0.21255682320489713)
| > loss_disc_real_2: 0.25875774025917053 (0.2282911243319149)
| > loss_disc_real_3: 0.24775323271751404 (0.22816053553736318)
| > loss_disc_real_4: 0.26078587770462036 (0.24085980141960017)
| > loss_disc_real_5: 0.2706845998764038 (0.2335290323637177)
| > loss_0: 2.7929582595825195 (2.5884861960599466)
| > grad_norm_0: tensor(13.9930, device='cuda:0') (tensor(17.5725, device='cuda:0'))
| > loss_gen: 2.0600099563598633 (2.2057089682407995)
| > loss_kl: 1.5783638954162598 (1.5964942047298865)
| > loss_feat: 6.54130220413208 (6.832209249397904)
| > loss_mel: 15.17801284790039 (15.503070524035978)
| > loss_duration: 1.471651315689087 (1.402072131090251)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.8293399810791 (27.539554978576476)
| > grad_norm_1: tensor(106.1275, device='cuda:0') (tensor(195.1299, device='cuda:0'))
| > current_lr_0: 0.00019927626732381507
| > current_lr_1: 0.00019927626732381507
| > step_time: 0.6607 (0.5863769525452581)
| > loader_time: 0.0077 (0.006628643053280906)
--> TIME: 2025-05-14 14:19:47 -- STEP: 429/630 -- GLOBAL_STEP: 895700
| > loss_disc: 2.6206934452056885 (2.585637344902766)
| > loss_disc_real_0: 0.13844215869903564 (0.17067655617922609)
| > loss_disc_real_1: 0.19757547974586487 (0.21295699322626588)
| > loss_disc_real_2: 0.26974356174468994 (0.22837961758628036)
| > loss_disc_real_3: 0.2629674971103668 (0.2281450346146986)
| > loss_disc_real_4: 0.27174487709999084 (0.24010952397104188)
| > loss_disc_real_5: 0.25376859307289124 (0.2323821110603137)
| > loss_0: 2.6206934452056885 (2.585637344902766)
| > grad_norm_0: tensor(30.3318, device='cuda:0') (tensor(18.8724, device='cuda:0'))
| > loss_gen: 2.151759147644043 (2.20744526052808)
| > loss_kl: 1.6448142528533936 (1.5982486798768836)
| > loss_feat: 5.738891124725342 (6.814631376511011)
| > loss_mel: 15.324670791625977 (15.513132021977352)
| > loss_duration: 1.4720180034637451 (1.4072338665004105)
| > amp_scaler: 256.0 (156.64335664335673)
| > loss_1: 26.332151412963867 (27.540691108970375)
| > grad_norm_1: tensor(146.7918, device='cuda:0') (tensor(216.9925, device='cuda:0'))
| > current_lr_0: 0.00019927626732381507
| > current_lr_1: 0.00019927626732381507
| > step_time: 0.7303 (0.615360816875537)
| > loader_time: 0.009 (0.007176454806383393)
--> TIME: 2025-05-14 14:21:16 -- STEP: 529/630 -- GLOBAL_STEP: 895800
| > loss_disc: 2.696789026260376 (2.585464686211655)
| > loss_disc_real_0: 0.1815582662820816 (0.17001913209746822)
| > loss_disc_real_1: 0.20490306615829468 (0.2126376452399788)
| > loss_disc_real_2: 0.3046059012413025 (0.2286388727859198)
| > loss_disc_real_3: 0.2713591158390045 (0.22883796827103556)
| > loss_disc_real_4: 0.259976327419281 (0.24005793040664075)
| > loss_disc_real_5: 0.2297755777835846 (0.2318340145854283)
| > loss_0: 2.696789026260376 (2.585464686211655)
| > grad_norm_0: tensor(18.6559, device='cuda:0') (tensor(19.9419, device='cuda:0'))
| > loss_gen: 2.2573490142822266 (2.2107302754948375)
| > loss_kl: 1.646681547164917 (1.598977122730479)
| > loss_feat: 6.046257495880127 (6.79247479808353)
| > loss_mel: 15.138802528381348 (15.496741085737549)
| > loss_duration: 1.443295955657959 (1.4179127813512304)
| > amp_scaler: 256.0 (175.4253308128545)
| > loss_1: 26.532386779785156 (27.51683598970871)
| > grad_norm_1: tensor(216.4701, device='cuda:0') (tensor(234.4342, device='cuda:0'))
| > current_lr_0: 0.00019927626732381507
| > current_lr_1: 0.00019927626732381507
| > step_time: 0.827 (0.6505983074130537)
| > loader_time: 0.0101 (0.021350263422513505)
--> TIME: 2025-05-14 14:23:01 -- STEP: 629/630 -- GLOBAL_STEP: 895900
| > loss_disc: 2.584672451019287 (2.5843344235079098)
| > loss_disc_real_0: 0.176754891872406 (0.17040160072697924)
| > loss_disc_real_1: 0.20560337603092194 (0.21256611645458626)
| > loss_disc_real_2: 0.22913093864917755 (0.22809655125740033)
| > loss_disc_real_3: 0.2649998366832733 (0.22928338056054137)
| > loss_disc_real_4: 0.24881871044635773 (0.23980053804447618)
| > loss_disc_real_5: 0.2563698887825012 (0.2315194435026763)
| > loss_0: 2.584672451019287 (2.5843344235079098)
| > grad_norm_0: tensor(14.0682, device='cuda:0') (tensor(20.3715, device='cuda:0'))
| > loss_gen: 2.3372490406036377 (2.2107497080331355)
| > loss_kl: 1.5596281290054321 (1.6028613380862722)
| > loss_feat: 5.898149490356445 (6.782044642680397)
| > loss_mel: 14.744524955749512 (15.484405411445849)
| > loss_duration: 1.4959086179733276 (1.4268631656522408)
| > amp_scaler: 256.0 (188.2352941176471)
| > loss_1: 26.03546142578125 (27.506924206198487)
| > grad_norm_1: tensor(162.1804, device='cuda:0') (tensor(238.0099, device='cuda:0'))
| > current_lr_0: 0.00019927626732381507
| > current_lr_1: 0.00019927626732381507
| > step_time: 1.6643 (0.7115702124961037)
| > loader_time: 0.0148 (0.019924641413605285)
> EVALUATION
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005300045013427734 (-5.217393239339164e-05)
| > avg_loss_disc: 2.681883672873179 (+0.09170345465342189)
| > avg_loss_disc_real_0: 0.2228593217829863 (+0.06187169688443342)
| > avg_loss_disc_real_1: 0.2368244801958402 (+0.012990954021612822)
| > avg_loss_disc_real_2: 0.2637351726492246 (+0.011671312153339386)
| > avg_loss_disc_real_3: 0.2915797407428424 (+0.07864600792527202)
| > avg_loss_disc_real_4: 0.2665112813313802 (+0.034885559231042834)
| > avg_loss_disc_real_5: 0.23880826185146967 (-0.008406504988670349)
| > avg_loss_0: 2.681883672873179 (+0.09170345465342189)
| > avg_loss_gen: 2.315833111604055 (+0.187799870967865)
| > avg_loss_kl: 1.7601235806941986 (+0.0426982045173645)
| > avg_loss_feat: 6.542269190152486 (+0.04285991191864014)
| > avg_loss_mel: 15.299624045689901 (-0.029337803522745176)
| > avg_loss_duration: 1.5329414109388988 (+0.008679062128067017)
| > avg_loss_1: 27.450791358947754 (+0.2526995340983085)
> EPOCH: 30/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 14:23:07)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:24:02 -- STEP: 99/630 -- GLOBAL_STEP: 896000
| > loss_disc: 2.492387533187866 (2.5834601310768517)
| > loss_disc_real_0: 0.13149598240852356 (0.16933441944796637)
| > loss_disc_real_1: 0.15738296508789062 (0.21101752149336267)
| > loss_disc_real_2: 0.24401673674583435 (0.22843928785637171)
| > loss_disc_real_3: 0.22596432268619537 (0.23074740020915716)
| > loss_disc_real_4: 0.211592435836792 (0.2392481682878552)
| > loss_disc_real_5: 0.24949344992637634 (0.23834014194782335)
| > loss_0: 2.492387533187866 (2.5834601310768517)
| > grad_norm_0: tensor(13.9562, device='cuda:0') (tensor(12.0531, device='cuda:0'))
| > loss_gen: 2.1057167053222656 (2.21596272666045)
| > loss_kl: 1.68856680393219 (1.5674012465910478)
| > loss_feat: 7.142721176147461 (6.993429140611128)
| > loss_mel: 14.802922248840332 (15.513881009034437)
| > loss_duration: 1.4580836296081543 (1.4326888852649264)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.19801139831543 (27.723363144229147)
| > grad_norm_1: tensor(46.0604, device='cuda:0') (tensor(116.0587, device='cuda:0'))
| > current_lr_0: 0.00019925135779039958
| > current_lr_1: 0.00019925135779039958
| > step_time: 0.5342 (0.5297503543622567)
| > loader_time: 0.0061 (0.005311361466995391)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_896000.pth
--> TIME: 2025-05-14 14:25:03 -- STEP: 199/630 -- GLOBAL_STEP: 896100
| > loss_disc: 2.5390002727508545 (2.5743883087407418)
| > loss_disc_real_0: 0.10975390672683716 (0.16886619515904233)
| > loss_disc_real_1: 0.28786778450012207 (0.21159934061556007)
| > loss_disc_real_2: 0.2361527681350708 (0.22809777285285932)
| > loss_disc_real_3: 0.21950344741344452 (0.22892449399334702)
| > loss_disc_real_4: 0.22832094132900238 (0.2396200710355337)
| > loss_disc_real_5: 0.1675490438938141 (0.2302596320833393)
| > loss_0: 2.5390002727508545 (2.5743883087407418)
| > grad_norm_0: tensor(30.6342, device='cuda:0') (tensor(18.8454, device='cuda:0'))
| > loss_gen: 2.4134750366210938 (2.2362227853219094)
| > loss_kl: 1.68876314163208 (1.5898040736739958)
| > loss_feat: 6.339339733123779 (6.932058645852247)
| > loss_mel: 15.628644943237305 (15.496036380978685)
| > loss_duration: 1.4281883239746094 (1.3940671520616548)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.498411178588867 (27.64818911336774)
| > grad_norm_1: tensor(632.8674, device='cuda:0') (tensor(203.8495, device='cuda:0'))
| > current_lr_0: 0.00019925135779039958
| > current_lr_1: 0.00019925135779039958
| > step_time: 0.589 (0.5537432641839265)
| > loader_time: 0.0068 (0.00588385903056542)
--> TIME: 2025-05-14 14:26:07 -- STEP: 299/630 -- GLOBAL_STEP: 896200
| > loss_disc: 2.5538830757141113 (2.575090897920539)
| > loss_disc_real_0: 0.19318422675132751 (0.1687911978134742)
| > loss_disc_real_1: 0.22637128829956055 (0.2123304897776017)
| > loss_disc_real_2: 0.21187546849250793 (0.2279180496632056)
| > loss_disc_real_3: 0.26009899377822876 (0.22914513073437986)
| > loss_disc_real_4: 0.2770030200481415 (0.24001316267710465)
| > loss_disc_real_5: 0.2312958687543869 (0.2311305784212307)
| > loss_0: 2.5538830757141113 (2.575090897920539)
| > grad_norm_0: tensor(6.7703, device='cuda:0') (tensor(17.8964, device='cuda:0'))
| > loss_gen: 2.1683690547943115 (2.230940928028576)
| > loss_kl: 1.6948785781860352 (1.6014224187187527)
| > loss_feat: 6.061750888824463 (6.919680675136604)
| > loss_mel: 15.612981796264648 (15.484478593271312)
| > loss_duration: 1.4394227266311646 (1.397460969794156)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.97740364074707 (27.63398365033509)
| > grad_norm_1: tensor(95.7695, device='cuda:0') (tensor(194.4717, device='cuda:0'))
| > current_lr_0: 0.00019925135779039958
| > current_lr_1: 0.00019925135779039958
| > step_time: 0.6768 (0.5776427007439144)
| > loader_time: 0.0089 (0.006424391150075852)
--> TIME: 2025-05-14 14:27:18 -- STEP: 399/630 -- GLOBAL_STEP: 896300
| > loss_disc: 2.31477952003479 (2.5751300891837996)
| > loss_disc_real_0: 0.15281584858894348 (0.1678010854207185)
| > loss_disc_real_1: 0.18052540719509125 (0.21282578252237244)
| > loss_disc_real_2: 0.16895723342895508 (0.22858039855508877)
| > loss_disc_real_3: 0.2053835242986679 (0.229470488384254)
| > loss_disc_real_4: 0.20209068059921265 (0.23931639930956944)
| > loss_disc_real_5: 0.19580577313899994 (0.23048424020521624)
| > loss_0: 2.31477952003479 (2.5751300891837996)
| > grad_norm_0: tensor(15.2438, device='cuda:0') (tensor(17.5159, device='cuda:0'))
| > loss_gen: 2.4101979732513428 (2.2256748272960287)
| > loss_kl: 1.8338301181793213 (1.6026373181426732)
| > loss_feat: 7.665280342102051 (6.883077781600761)
| > loss_mel: 15.986160278320312 (15.483407479479798)
| > loss_duration: 1.435424566268921 (1.4029123033198492)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.330894470214844 (27.597709751368157)
| > grad_norm_1: tensor(459.7279, device='cuda:0') (tensor(196.4757, device='cuda:0'))
| > current_lr_0: 0.00019925135779039958
| > current_lr_1: 0.00019925135779039958
| > step_time: 0.7504 (0.6064663070783877)
| > loader_time: 0.0089 (0.006978728119890788)
--> TIME: 2025-05-14 14:28:36 -- STEP: 499/630 -- GLOBAL_STEP: 896400
| > loss_disc: 2.5791189670562744 (2.576936222508342)
| > loss_disc_real_0: 0.1848527491092682 (0.16935989895242012)
| > loss_disc_real_1: 0.25408828258514404 (0.21219528741193916)
| > loss_disc_real_2: 0.24411654472351074 (0.22886331785537437)
| > loss_disc_real_3: 0.23404455184936523 (0.2299148245063239)
| > loss_disc_real_4: 0.21628963947296143 (0.23950703391331232)
| > loss_disc_real_5: 0.2906271815299988 (0.22797806940241186)
| > loss_0: 2.5791189670562744 (2.576936222508342)
| > grad_norm_0: tensor(13.4028, device='cuda:0') (tensor(19.4571, device='cuda:0'))
| > loss_gen: 2.2903759479522705 (2.230959098898091)
| > loss_kl: 1.5474177598953247 (1.6063970131482292)
| > loss_feat: 6.103886604309082 (6.847482232149235)
| > loss_mel: 15.206357955932617 (15.470659508256015)
| > loss_duration: 1.5013067722320557 (1.4155760248581724)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.64934539794922 (27.571073891404627)
| > grad_norm_1: tensor(42.6444, device='cuda:0') (tensor(222.1009, device='cuda:0'))
| > current_lr_0: 0.00019925135779039958
| > current_lr_1: 0.00019925135779039958
| > step_time: 0.833 (0.6380952192929558)
| > loader_time: 0.0109 (0.0074785539286886735)
--> TIME: 2025-05-14 14:30:08 -- STEP: 599/630 -- GLOBAL_STEP: 896500
| > loss_disc: 2.621278762817383 (2.5818490595968826)
| > loss_disc_real_0: 0.1773521900177002 (0.17005333397692948)
| > loss_disc_real_1: 0.1703961342573166 (0.2124017421933566)
| > loss_disc_real_2: 0.20795036852359772 (0.22908200599713396)
| > loss_disc_real_3: 0.2462727427482605 (0.2299883524095873)
| > loss_disc_real_4: 0.27755430340766907 (0.23939154940176885)
| > loss_disc_real_5: 0.28349748253822327 (0.2294494826626499)
| > loss_0: 2.621278762817383 (2.5818490595968826)
| > grad_norm_0: tensor(16.0479, device='cuda:0') (tensor(18.8505, device='cuda:0'))
| > loss_gen: 2.1414122581481934 (2.219238616389299)
| > loss_kl: 1.5891332626342773 (1.6089556867968857)
| > loss_feat: 6.351428985595703 (6.807189638905216)
| > loss_mel: 15.113811492919922 (15.46432338294282)
| > loss_duration: 1.4905493259429932 (1.4243868141620106)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.686336517333984 (27.524094166063108)
| > grad_norm_1: tensor(70.7579, device='cuda:0') (tensor(213.0405, device='cuda:0'))
| > current_lr_0: 0.00019925135779039958
| > current_lr_1: 0.00019925135779039958
| > step_time: 1.0847 (0.6835776967476922)
| > loader_time: 0.0137 (0.008078684591888784)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_896500.pth
> EVALUATION
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004902939001719157 (-0.0003971060117085772)
| > avg_loss_disc: 2.6949883898099265 (+0.013104716936747529)
| > avg_loss_disc_real_0: 0.18098333850502968 (-0.041875983277956635)
| > avg_loss_disc_real_1: 0.19756234685579935 (-0.03926213334004086)
| > avg_loss_disc_real_2: 0.24271289507548013 (-0.021022277573744447)
| > avg_loss_disc_real_3: 0.23135857780774435 (-0.06022116293509802)
| > avg_loss_disc_real_4: 0.25843309611082077 (-0.00807818522055942)
| > avg_loss_disc_real_5: 0.23537550369898477 (-0.003432758152484894)
| > avg_loss_0: 2.6949883898099265 (+0.013104716936747529)
| > avg_loss_gen: 2.042183746894201 (-0.2736493647098541)
| > avg_loss_kl: 1.7670665582021077 (+0.006942977507909065)
| > avg_loss_feat: 6.31814964612325 (-0.22411954402923584)
| > avg_loss_mel: 15.857055823008219 (+0.5574317773183175)
| > avg_loss_duration: 1.528798093398412 (-0.004143317540486802)
| > avg_loss_1: 27.51325337092082 (+0.062462011973064335)
> EPOCH: 31/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 14:30:58)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:31:37 -- STEP: 69/630 -- GLOBAL_STEP: 896600
| > loss_disc: 2.543262481689453 (2.582861706830453)
| > loss_disc_real_0: 0.16345863044261932 (0.17012407911428507)
| > loss_disc_real_1: 0.17437463998794556 (0.21148644344530243)
| > loss_disc_real_2: 0.27635765075683594 (0.22504053081291311)
| > loss_disc_real_3: 0.22673244774341583 (0.22624694804350534)
| > loss_disc_real_4: 0.24972233176231384 (0.24042235746763754)
| > loss_disc_real_5: 0.24779853224754333 (0.23951649709024292)
| > loss_0: 2.543262481689453 (2.582861706830453)
| > grad_norm_0: tensor(9.6934, device='cuda:0') (tensor(13.3437, device='cuda:0'))
| > loss_gen: 2.228480577468872 (2.2285197299459716)
| > loss_kl: 1.6802010536193848 (1.5678002022314763)
| > loss_feat: 6.4193010330200195 (7.004382168037304)
| > loss_mel: 15.598711967468262 (15.54788357278575)
| > loss_duration: 1.4558385610580444 (1.4302387185718701)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.382535934448242 (27.778824460679207)
| > grad_norm_1: tensor(75.4880, device='cuda:0') (tensor(138.2408, device='cuda:0'))
| > current_lr_0: 0.00019922645137067577
| > current_lr_1: 0.00019922645137067577
| > step_time: 0.5379 (0.5297333710435508)
| > loader_time: 0.0052 (0.005324653957201087)
--> TIME: 2025-05-14 14:32:35 -- STEP: 169/630 -- GLOBAL_STEP: 896700
| > loss_disc: 2.5778615474700928 (2.5954165105988993)
| > loss_disc_real_0: 0.1659017652273178 (0.17121870220589214)
| > loss_disc_real_1: 0.16727761924266815 (0.2126058846183077)
| > loss_disc_real_2: 0.18294890224933624 (0.22880962790822137)
| > loss_disc_real_3: 0.2529226541519165 (0.22834809089200736)
| > loss_disc_real_4: 0.2533794939517975 (0.23919173695984677)
| > loss_disc_real_5: 0.18908673524856567 (0.2347492729947412)
| > loss_0: 2.5778615474700928 (2.5954165105988993)
| > grad_norm_0: tensor(28.3249, device='cuda:0') (tensor(18.2502, device='cuda:0'))
| > loss_gen: 2.2166085243225098 (2.212540326739204)
| > loss_kl: 1.6904319524765015 (1.5967881771234365)
| > loss_feat: 7.676005840301514 (6.870028055631197)
| > loss_mel: 16.104522705078125 (15.454087076807868)
| > loss_duration: 1.4676107168197632 (1.3811008401170994)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.155179977416992 (27.514544582931247)
| > grad_norm_1: tensor(266.1927, device='cuda:0') (tensor(202.5907, device='cuda:0'))
| > current_lr_0: 0.00019922645137067577
| > current_lr_1: 0.00019922645137067577
| > step_time: 0.5992 (0.5576318326081043)
| > loader_time: 0.0067 (0.0059497821965866565)
--> TIME: 2025-05-14 14:33:38 -- STEP: 269/630 -- GLOBAL_STEP: 896800
| > loss_disc: 2.5610480308532715 (2.5926377569432577)
| > loss_disc_real_0: 0.11161787807941437 (0.17070053492890852)
| > loss_disc_real_1: 0.22083227336406708 (0.21229092100960614)
| > loss_disc_real_2: 0.23998156189918518 (0.22910085813485115)
| > loss_disc_real_3: 0.22441613674163818 (0.22930814303651617)
| > loss_disc_real_4: 0.23235231637954712 (0.23940648991600733)
| > loss_disc_real_5: 0.2734689712524414 (0.2337589478293316)
| > loss_0: 2.5610480308532715 (2.5926377569432577)
| > grad_norm_0: tensor(11.7095, device='cuda:0') (tensor(17.7281, device='cuda:0'))
| > loss_gen: 2.092686653137207 (2.2060695851159355)
| > loss_kl: 1.6080951690673828 (1.6038162659535178)
| > loss_feat: 6.220919132232666 (6.878744400123681)
| > loss_mel: 14.598409652709961 (15.523957748838518)
| > loss_duration: 1.4922876358032227 (1.3896652078983065)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.01239776611328 (27.602253300549812)
| > grad_norm_1: tensor(46.8093, device='cuda:0') (tensor(200.0579, device='cuda:0'))
| > current_lr_0: 0.00019922645137067577
| > current_lr_1: 0.00019922645137067577
| > step_time: 0.6258 (0.5793449275998821)
| > loader_time: 0.007 (0.00648731547217387)
--> TIME: 2025-05-14 14:34:47 -- STEP: 369/630 -- GLOBAL_STEP: 896900
| > loss_disc: 2.412473678588867 (2.587144142243919)
| > loss_disc_real_0: 0.125201016664505 (0.16934594144504558)
| > loss_disc_real_1: 0.21053141355514526 (0.21167181371673335)
| > loss_disc_real_2: 0.24109941720962524 (0.22856508445772053)
| > loss_disc_real_3: 0.173531636595726 (0.22852840599651905)
| > loss_disc_real_4: 0.2149638682603836 (0.23952558297451917)
| > loss_disc_real_5: 0.17177711427211761 (0.23413625278770117)
| > loss_0: 2.412473678588867 (2.587144142243919)
| > grad_norm_0: tensor(6.3222, device='cuda:0') (tensor(15.9553, device='cuda:0'))
| > loss_gen: 2.2612802982330322 (2.2013611858130155)
| > loss_kl: 1.7230178117752075 (1.6056843676218178)
| > loss_feat: 6.39061975479126 (6.817879946897345)
| > loss_mel: 14.478240966796875 (15.495913963007734)
| > loss_duration: 1.4252872467041016 (1.408217083793991)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.278446197509766 (27.529056590423988)
| > grad_norm_1: tensor(77.7768, device='cuda:0') (tensor(170.2482, device='cuda:0'))
| > current_lr_0: 0.00019922645137067577
| > current_lr_1: 0.00019922645137067577
| > step_time: 0.6978 (0.6042185456449097)
| > loader_time: 0.0087 (0.00699595901055065)
--> TIME: 2025-05-14 14:36:03 -- STEP: 469/630 -- GLOBAL_STEP: 897000
| > loss_disc: 2.6883645057678223 (2.5880507401057637)
| > loss_disc_real_0: 0.2936555743217468 (0.16928831715065268)
| > loss_disc_real_1: 0.2280992865562439 (0.21259064209867895)
| > loss_disc_real_2: 0.2667272090911865 (0.22873785840804134)
| > loss_disc_real_3: 0.21735790371894836 (0.22913686127296642)
| > loss_disc_real_4: 0.24190576374530792 (0.23951148542005624)
| > loss_disc_real_5: 0.26686590909957886 (0.23303084431299523)
| > loss_0: 2.6883645057678223 (2.5880507401057637)
| > grad_norm_0: tensor(39.4002, device='cuda:0') (tensor(17.1400, device='cuda:0'))
| > loss_gen: 2.3769965171813965 (2.2065512818822475)
| > loss_kl: 1.6776245832443237 (1.6025542226681582)
| > loss_feat: 6.450469970703125 (6.815479362951412)
| > loss_mel: 15.137331008911133 (15.5145094165924)
| > loss_duration: 1.4837684631347656 (1.410773215009205)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.126192092895508 (27.54986756086857)
| > grad_norm_1: tensor(470.6466, device='cuda:0') (tensor(183.8926, device='cuda:0'))
| > current_lr_0: 0.00019922645137067577
| > current_lr_1: 0.00019922645137067577
| > step_time: 0.7775 (0.6355114298334505)
| > loader_time: 0.0096 (0.007510432810671551)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_897000.pth
--> TIME: 2025-05-14 14:37:31 -- STEP: 569/630 -- GLOBAL_STEP: 897100
| > loss_disc: 2.553347110748291 (2.5880266291814435)
| > loss_disc_real_0: 0.15217477083206177 (0.16973131478670805)
| > loss_disc_real_1: 0.22508502006530762 (0.21232085356812905)
| > loss_disc_real_2: 0.20192453265190125 (0.22901693824514982)
| > loss_disc_real_3: 0.2143993079662323 (0.22888978477731112)
| > loss_disc_real_4: 0.20327697694301605 (0.23949051453275294)
| > loss_disc_real_5: 0.21651451289653778 (0.23373967390802078)
| > loss_0: 2.553347110748291 (2.5880266291814435)
| > grad_norm_0: tensor(6.0555, device='cuda:0') (tensor(16.8268, device='cuda:0'))
| > loss_gen: 2.0237059593200684 (2.205464867799689)
| > loss_kl: 1.582961916923523 (1.6083282921561464)
| > loss_feat: 7.09470796585083 (6.773000899014868)
| > loss_mel: 15.472702026367188 (15.510009554442286)
| > loss_duration: 1.4642661809921265 (1.4203866024637466)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.638343811035156 (27.51719027286255)
| > grad_norm_1: tensor(46.7183, device='cuda:0') (tensor(178.0626, device='cuda:0'))
| > current_lr_0: 0.00019922645137067577
| > current_lr_1: 0.00019922645137067577
| > step_time: 0.8517 (0.6693734024865765)
| > loader_time: 0.0116 (0.008086065835399668)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004980146884918213 (+7.72078831990557e-05)
| > avg_loss_disc: 2.6775503357251487 (-0.017438054084777832)
| > avg_loss_disc_real_0: 0.21755751222372055 (+0.03657417371869087)
| > avg_loss_disc_real_1: 0.22268001238505045 (+0.0251176655292511)
| > avg_loss_disc_real_2: 0.25135298321644467 (+0.008640088140964536)
| > avg_loss_disc_real_3: 0.24957474321126938 (+0.018216165403525025)
| > avg_loss_disc_real_4: 0.2925233542919159 (+0.03409025818109512)
| > avg_loss_disc_real_5: 0.2706283355752627 (+0.03525283187627795)
| > avg_loss_0: 2.6775503357251487 (-0.017438054084777832)
| > avg_loss_gen: 2.203978717327118 (+0.16179497043291713)
| > avg_loss_kl: 1.7266619006792705 (-0.04040465752283717)
| > avg_loss_feat: 6.358975807825725 (+0.04082616170247455)
| > avg_loss_mel: 15.591796239217123 (-0.2652595837910958)
| > avg_loss_duration: 1.5293487409750621 (+0.0005506475766501318)
| > avg_loss_1: 27.41076151529948 (-0.10249185562133789)
> EPOCH: 32/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 14:38:45)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:39:07 -- STEP: 39/630 -- GLOBAL_STEP: 897200
| > loss_disc: 2.5396604537963867 (2.531262452785785)
| > loss_disc_real_0: 0.22440609335899353 (0.15969666953270256)
| > loss_disc_real_1: 0.19507573544979095 (0.20781127497171745)
| > loss_disc_real_2: 0.2030462771654129 (0.23171778443532112)
| > loss_disc_real_3: 0.20559386909008026 (0.23431659165101174)
| > loss_disc_real_4: 0.22726653516292572 (0.24901708922325036)
| > loss_disc_real_5: 0.24232953786849976 (0.206691841284434)
| > loss_0: 2.5396604537963867 (2.531262452785785)
| > grad_norm_0: tensor(14.5156, device='cuda:0') (tensor(20.6579, device='cuda:0'))
| > loss_gen: 2.1945033073425293 (2.3384870137923803)
| > loss_kl: 1.3741456270217896 (1.5289339744127715)
| > loss_feat: 6.7812113761901855 (7.3029698469699955)
| > loss_mel: 15.31379222869873 (15.532305668561886)
| > loss_duration: 1.423271656036377 (1.4243869200730934)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.086925506591797 (28.127083411583534)
| > grad_norm_1: tensor(114.4440, device='cuda:0') (tensor(277.8428, device='cuda:0'))
| > current_lr_0: 0.00019920154806425444
| > current_lr_1: 0.00019920154806425444
| > step_time: 0.531 (0.5267206705533539)
| > loader_time: 0.0053 (0.005131917122082833)
--> TIME: 2025-05-14 14:40:03 -- STEP: 139/630 -- GLOBAL_STEP: 897300
| > loss_disc: 2.418463945388794 (2.562026866048359)
| > loss_disc_real_0: 0.09888115525245667 (0.16849753223091585)
| > loss_disc_real_1: 0.1987760215997696 (0.21063714318995852)
| > loss_disc_real_2: 0.2761313319206238 (0.22864353806852436)
| > loss_disc_real_3: 0.28086215257644653 (0.23029591153851517)
| > loss_disc_real_4: 0.23138707876205444 (0.2432475341952962)
| > loss_disc_real_5: 0.1999412477016449 (0.22147611383911517)
| > loss_0: 2.418463945388794 (2.562026866048359)
| > grad_norm_0: tensor(33.0532, device='cuda:0') (tensor(21.5132, device='cuda:0'))
| > loss_gen: 2.366720676422119 (2.2648354314214028)
| > loss_kl: 1.545178771018982 (1.5690393465028392)
| > loss_feat: 7.365007400512695 (7.040403877230856)
| > loss_mel: 16.301834106445312 (15.506792397807828)
| > loss_duration: 1.4316943883895874 (1.4032871740327464)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.010435104370117 (27.784358251009053)
| > grad_norm_1: tensor(294.8273, device='cuda:0') (tensor(287.9978, device='cuda:0'))
| > current_lr_0: 0.00019920154806425444
| > current_lr_1: 0.00019920154806425444
| > step_time: 0.5509 (0.5428668509284369)
| > loader_time: 0.0058 (0.005612047456151292)
--> TIME: 2025-05-14 14:41:04 -- STEP: 239/630 -- GLOBAL_STEP: 897400
| > loss_disc: 2.7034664154052734 (2.5665329091219733)
| > loss_disc_real_0: 0.18353284895420074 (0.1695099898836104)
| > loss_disc_real_1: 0.21572938561439514 (0.21062685748772642)
| > loss_disc_real_2: 0.2509567439556122 (0.2288241320324742)
| > loss_disc_real_3: 0.3128962814807892 (0.22832518466845717)
| > loss_disc_real_4: 0.2124558687210083 (0.24124459224016598)
| > loss_disc_real_5: 0.23281539976596832 (0.22435905313641458)
| > loss_0: 2.7034664154052734 (2.5665329091219733)
| > grad_norm_0: tensor(17.5061, device='cuda:0') (tensor(22.7126, device='cuda:0'))
| > loss_gen: 1.9745062589645386 (2.2592054864851487)
| > loss_kl: 1.5910465717315674 (1.5963340598669014)
| > loss_feat: 6.432912826538086 (6.987115889912369)
| > loss_mel: 15.42198657989502 (15.516172648473763)
| > loss_duration: 1.4696247577667236 (1.3790149943100363)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.890077590942383 (27.73784307854943)
| > grad_norm_1: tensor(42.0538, device='cuda:0') (tensor(292.4666, device='cuda:0'))
| > current_lr_0: 0.00019920154806425444
| > current_lr_1: 0.00019920154806425444
| > step_time: 0.6102 (0.5664548634485224)
| > loader_time: 0.0084 (0.006118545971156165)
--> TIME: 2025-05-14 14:42:09 -- STEP: 339/630 -- GLOBAL_STEP: 897500
| > loss_disc: 2.5629377365112305 (2.574390862895324)
| > loss_disc_real_0: 0.1967736780643463 (0.17098767884009708)
| > loss_disc_real_1: 0.1850001960992813 (0.21035804379742398)
| > loss_disc_real_2: 0.24765269458293915 (0.22813134906390423)
| > loss_disc_real_3: 0.22246384620666504 (0.22826228455632133)
| > loss_disc_real_4: 0.2617068290710449 (0.24056564438483707)
| > loss_disc_real_5: 0.23162700235843658 (0.22758580656354055)
| > loss_0: 2.5629377365112305 (2.574390862895324)
| > grad_norm_0: tensor(12.9803, device='cuda:0') (tensor(20.7803, device='cuda:0'))
| > loss_gen: 2.135162115097046 (2.2371824019778086)
| > loss_kl: 1.5423997640609741 (1.6033238728137853)
| > loss_feat: 7.070607662200928 (6.898900399165871)
| > loss_mel: 15.47858715057373 (15.488133770877985)
| > loss_duration: 1.4272699356079102 (1.4017117301271376)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.65402603149414 (27.6292521327646)
| > grad_norm_1: tensor(312.6975, device='cuda:0') (tensor(265.5212, device='cuda:0'))
| > current_lr_0: 0.00019920154806425444
| > current_lr_1: 0.00019920154806425444
| > step_time: 0.6752 (0.5876029452039779)
| > loader_time: 0.0081 (0.006662479895757714)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_897500.pth
--> TIME: 2025-05-14 14:43:23 -- STEP: 439/630 -- GLOBAL_STEP: 897600
| > loss_disc: 2.466315269470215 (2.575318318564691)
| > loss_disc_real_0: 0.2702219784259796 (0.17074945436659048)
| > loss_disc_real_1: 0.2057638019323349 (0.21089904188498815)
| > loss_disc_real_2: 0.22779056429862976 (0.2289657917951397)
| > loss_disc_real_3: 0.23462510108947754 (0.2279221643958928)
| > loss_disc_real_4: 0.2092885971069336 (0.24016663618810086)
| > loss_disc_real_5: 0.22804172337055206 (0.22653326840226906)
| > loss_0: 2.466315269470215 (2.575318318564691)
| > grad_norm_0: tensor(53.6063, device='cuda:0') (tensor(21.5606, device='cuda:0'))
| > loss_gen: 2.680696487426758 (2.2383453930157433)
| > loss_kl: 1.5598026514053345 (1.6001164234309104)
| > loss_feat: 7.7765936851501465 (6.861509470841879)
| > loss_mel: 15.835127830505371 (15.479427735191814)
| > loss_duration: 1.4712376594543457 (1.405135282622926)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.323457717895508 (27.58453428229329)
| > grad_norm_1: tensor(730.7031, device='cuda:0') (tensor(272.0424, device='cuda:0'))
| > current_lr_0: 0.00019920154806425444
| > current_lr_1: 0.00019920154806425444
| > step_time: 0.6907 (0.6109164586642886)
| > loader_time: 0.0094 (0.007214917137302408)
--> TIME: 2025-05-14 14:44:38 -- STEP: 539/630 -- GLOBAL_STEP: 897700
| > loss_disc: 2.6754708290100098 (2.5802386271489133)
| > loss_disc_real_0: 0.261410653591156 (0.1716304258728513)
| > loss_disc_real_1: 0.19996553659439087 (0.21166384683192765)
| > loss_disc_real_2: 0.24471858143806458 (0.2288907017966591)
| > loss_disc_real_3: 0.21796157956123352 (0.22817478009632652)
| > loss_disc_real_4: 0.24078205227851868 (0.24008600455268195)
| > loss_disc_real_5: 0.27065661549568176 (0.22763617483273507)
| > loss_0: 2.6754708290100098 (2.5802386271489133)
| > grad_norm_0: tensor(15.4972, device='cuda:0') (tensor(21.8525, device='cuda:0'))
| > loss_gen: 1.9906830787658691 (2.2285983268316656)
| > loss_kl: 1.612855315208435 (1.6045897141900713)
| > loss_feat: 6.318711757659912 (6.8159169416480685)
| > loss_mel: 15.780976295471191 (15.477341361744728)
| > loss_duration: 1.4483387470245361 (1.4156555368639323)
| > amp_scaler: 256.0 (256.4749536178105)
| > loss_1: 27.151565551757812 (27.54210186889308)
| > grad_norm_1: tensor(168.8304, device='cuda:0') (tensor(273.5316, device='cuda:0'))
| > current_lr_0: 0.00019920154806425444
| > current_lr_1: 0.00019920154806425444
| > step_time: 0.8701 (0.6348489286284724)
| > loader_time: 0.0119 (0.007781687826747576)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005263050397237142 (+0.00028290351231892875)
| > avg_loss_disc: 2.6459139982859297 (-0.03163633743921901)
| > avg_loss_disc_real_0: 0.23093177874883017 (+0.013374266525109618)
| > avg_loss_disc_real_1: 0.2308391568561395 (+0.008159144471089064)
| > avg_loss_disc_real_2: 0.2213765780131022 (-0.029976405203342465)
| > avg_loss_disc_real_3: 0.21207704146703085 (-0.037497701744238526)
| > avg_loss_disc_real_4: 0.24023116752505302 (-0.05229218676686287)
| > avg_loss_disc_real_5: 0.22541260595122972 (-0.045215729624033)
| > avg_loss_0: 2.6459139982859297 (-0.03163633743921901)
| > avg_loss_gen: 2.075097024440765 (-0.12888169288635298)
| > avg_loss_kl: 1.7180614372094472 (-0.00860046346982335)
| > avg_loss_feat: 6.509936610857646 (+0.1509608030319214)
| > avg_loss_mel: 15.484007438023886 (-0.1077888011932373)
| > avg_loss_duration: 1.5348797937234242 (+0.005531052748362075)
| > avg_loss_1: 27.321982224782307 (-0.08877929051717359)
> EPOCH: 33/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 14:46:13)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:46:18 -- STEP: 9/630 -- GLOBAL_STEP: 897800
| > loss_disc: 2.5562422275543213 (2.523728953467475)
| > loss_disc_real_0: 0.21328608691692352 (0.1592095543940862)
| > loss_disc_real_1: 0.2392948418855667 (0.2168935371769799)
| > loss_disc_real_2: 0.26868727803230286 (0.2236895759900411)
| > loss_disc_real_3: 0.1987999826669693 (0.22275303138626945)
| > loss_disc_real_4: 0.22323398292064667 (0.23312292165226406)
| > loss_disc_real_5: 0.22474516928195953 (0.22813576294316185)
| > loss_0: 2.5562422275543213 (2.523728953467475)
| > grad_norm_0: tensor(12.3023, device='cuda:0') (tensor(11.9925, device='cuda:0'))
| > loss_gen: 2.366055727005005 (2.2406460444132485)
| > loss_kl: 1.4777699708938599 (1.5556683275434706)
| > loss_feat: 8.243067741394043 (7.017897288004558)
| > loss_mel: 15.739367485046387 (15.759702576531303)
| > loss_duration: 1.4245541095733643 (1.4062458409203424)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.250816345214844 (27.980159971449112)
| > grad_norm_1: tensor(244.4388, device='cuda:0') (tensor(133.1332, device='cuda:0'))
| > current_lr_0: 0.0001991766478707464
| > current_lr_1: 0.0001991766478707464
| > step_time: 0.5226 (0.5098064210679796)
| > loader_time: 0.0045 (0.004319217469957139)
--> TIME: 2025-05-14 14:47:14 -- STEP: 109/630 -- GLOBAL_STEP: 897900
| > loss_disc: 2.6384623050689697 (2.5568003807592827)
| > loss_disc_real_0: 0.0991840586066246 (0.16203846782445905)
| > loss_disc_real_1: 0.19506707787513733 (0.2124052017653754)
| > loss_disc_real_2: 0.2002745270729065 (0.22625687376621667)
| > loss_disc_real_3: 0.2682802081108093 (0.22826414069998155)
| > loss_disc_real_4: 0.2563401758670807 (0.24229780673433882)
| > loss_disc_real_5: 0.25052767992019653 (0.22637520443408862)
| > loss_0: 2.6384623050689697 (2.5568003807592827)
| > grad_norm_0: tensor(24.7364, device='cuda:0') (tensor(21.5286, device='cuda:0'))
| > loss_gen: 1.9955470561981201 (2.271295162515905)
| > loss_kl: 1.6217588186264038 (1.5391625439355132)
| > loss_feat: 5.641001224517822 (7.033432015585243)
| > loss_mel: 15.280253410339355 (15.592628032789317)
| > loss_duration: 1.4680070877075195 (1.3900649831929341)
| > amp_scaler: 128.0 (193.76146788990826)
| > loss_1: 26.006568908691406 (27.826582882382453)
| > grad_norm_1: tensor(249.3422, device='cuda:0') (tensor(255.7138, device='cuda:0'))
| > current_lr_0: 0.0001991766478707464
| > current_lr_1: 0.0001991766478707464
| > step_time: 0.5433 (0.5397575317172829)
| > loader_time: 0.0056 (0.005343487503331736)
--> TIME: 2025-05-14 14:48:13 -- STEP: 209/630 -- GLOBAL_STEP: 898000
| > loss_disc: 2.398164749145508 (2.5682438617688046)
| > loss_disc_real_0: 0.1402733027935028 (0.16468926084241214)
| > loss_disc_real_1: 0.19250182807445526 (0.21260199157530044)
| > loss_disc_real_2: 0.2005774974822998 (0.2274458009803124)
| > loss_disc_real_3: 0.21657301485538483 (0.22989088418095877)
| > loss_disc_real_4: 0.21542243659496307 (0.24163081008566623)
| > loss_disc_real_5: 0.2365240603685379 (0.22662862515050258)
| > loss_0: 2.398164749145508 (2.5682438617688046)
| > grad_norm_0: tensor(13.3027, device='cuda:0') (tensor(23.6568, device='cuda:0'))
| > loss_gen: 2.2748935222625732 (2.256350129985355)
| > loss_kl: 1.5219768285751343 (1.5693874695654697)
| > loss_feat: 6.909457683563232 (6.971205271031868)
| > loss_mel: 16.061216354370117 (15.516189114328776)
| > loss_duration: 1.4496898651123047 (1.3697361278762088)
| > amp_scaler: 128.0 (162.2966507177034)
| > loss_1: 28.217233657836914 (27.68286810879502)
| > grad_norm_1: tensor(241.1748, device='cuda:0') (tensor(293.6336, device='cuda:0'))
| > current_lr_0: 0.0001991766478707464
| > current_lr_1: 0.0001991766478707464
| > step_time: 0.6081 (0.5620721949344613)
| > loader_time: 0.007 (0.00594857092679402)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_898000.pth
--> TIME: 2025-05-14 14:49:21 -- STEP: 309/630 -- GLOBAL_STEP: 898100
| > loss_disc: 2.339240550994873 (2.5741999758871623)
| > loss_disc_real_0: 0.11917226016521454 (0.16721572013252367)
| > loss_disc_real_1: 0.20482169091701508 (0.21211170272533947)
| > loss_disc_real_2: 0.19769224524497986 (0.22807244903447177)
| > loss_disc_real_3: 0.17833714187145233 (0.23020439645619067)
| > loss_disc_real_4: 0.20485353469848633 (0.2400942103858905)
| > loss_disc_real_5: 0.157339945435524 (0.22797226804552725)
| > loss_0: 2.339240550994873 (2.5741999758871623)
| > grad_norm_0: tensor(16.2378, device='cuda:0') (tensor(21.1257, device='cuda:0'))
| > loss_gen: 2.3154208660125732 (2.23496614960791)
| > loss_kl: 1.638696551322937 (1.5785866979642216)
| > loss_feat: 7.133881092071533 (6.873276792297854)
| > loss_mel: 15.811195373535156 (15.509021481263984)
| > loss_duration: 1.4273741245269775 (1.399247720403579)
| > amp_scaler: 128.0 (151.19741100323625)
| > loss_1: 28.326566696166992 (27.595098822633812)
| > grad_norm_1: tensor(112.3615, device='cuda:0') (tensor(258.8123, device='cuda:0'))
| > current_lr_0: 0.0001991766478707464
| > current_lr_1: 0.0001991766478707464
| > step_time: 0.6648 (0.584716817707691)
| > loader_time: 0.0075 (0.006481307995743732)
--> TIME: 2025-05-14 14:50:33 -- STEP: 409/630 -- GLOBAL_STEP: 898200
| > loss_disc: 2.627354621887207 (2.5748423696438665)
| > loss_disc_real_0: 0.18856804072856903 (0.16757296987588352)
| > loss_disc_real_1: 0.20679223537445068 (0.21207836962562318)
| > loss_disc_real_2: 0.24250084161758423 (0.2285404147757878)
| > loss_disc_real_3: 0.229591965675354 (0.23005162554731579)
| > loss_disc_real_4: 0.25138333439826965 (0.23998815681065794)
| > loss_disc_real_5: 0.279891699552536 (0.2281363042832004)
| > loss_0: 2.627354621887207 (2.5748423696438665)
| > grad_norm_0: tensor(9.9897, device='cuda:0') (tensor(21.8347, device='cuda:0'))
| > loss_gen: 2.0807058811187744 (2.231078923477231)
| > loss_kl: 1.7381190061569214 (1.5839465474732646)
| > loss_feat: 5.942470073699951 (6.853460092707774)
| > loss_mel: 15.120033264160156 (15.479821676147013)
| > loss_duration: 1.4754860401153564 (1.4028851682807533)
| > amp_scaler: 128.0 (145.52567237163828)
| > loss_1: 26.356815338134766 (27.55119239788475)
| > grad_norm_1: tensor(63.5322, device='cuda:0') (tensor(266.2996, device='cuda:0'))
| > current_lr_0: 0.0001991766478707464
| > current_lr_1: 0.0001991766478707464
| > step_time: 0.725 (0.6143002515900102)
| > loader_time: 0.0102 (0.007040120570175802)
--> TIME: 2025-05-14 14:51:52 -- STEP: 509/630 -- GLOBAL_STEP: 898300
| > loss_disc: 2.518625259399414 (2.577955303117194)
| > loss_disc_real_0: 0.2561902403831482 (0.16781162996071952)
| > loss_disc_real_1: 0.26820093393325806 (0.21207119913841277)
| > loss_disc_real_2: 0.2550453543663025 (0.22836922469214047)
| > loss_disc_real_3: 0.20421884953975677 (0.23010019574511964)
| > loss_disc_real_4: 0.27301499247550964 (0.23991675680770388)
| > loss_disc_real_5: 0.20127059519290924 (0.23007498230704623)
| > loss_0: 2.518625259399414 (2.577955303117194)
| > grad_norm_0: tensor(11.5068, device='cuda:0') (tensor(20.9427, device='cuda:0'))
| > loss_gen: 2.2372727394104004 (2.2217200572926346)
| > loss_kl: 1.847757339477539 (1.5911401400163276)
| > loss_feat: 6.884058475494385 (6.805303382498809)
| > loss_mel: 15.887514114379883 (15.48364722471106)
| > loss_duration: 1.4175479412078857 (1.414477230289362)
| > amp_scaler: 128.0 (142.08251473477418)
| > loss_1: 28.27414894104004 (27.516288019116594)
| > grad_norm_1: tensor(59.3258, device='cuda:0') (tensor(248.7932, device='cuda:0'))
| > current_lr_0: 0.0001991766478707464
| > current_lr_1: 0.0001991766478707464
| > step_time: 0.8649 (0.6456364292526993)
| > loader_time: 0.0102 (0.007566378486648287)
--> TIME: 2025-05-14 14:53:24 -- STEP: 609/630 -- GLOBAL_STEP: 898400
| > loss_disc: 2.5308890342712402 (2.5838625203995464)
| > loss_disc_real_0: 0.16803377866744995 (0.16852095761077926)
| > loss_disc_real_1: 0.22324925661087036 (0.2118951313943895)
| > loss_disc_real_2: 0.23681451380252838 (0.22860956187122952)
| > loss_disc_real_3: 0.23458760976791382 (0.23041888525822676)
| > loss_disc_real_4: 0.2279311567544937 (0.23965797941575104)
| > loss_disc_real_5: 0.24567294120788574 (0.23145864118496184)
| > loss_0: 2.5308890342712402 (2.5838625203995464)
| > grad_norm_0: tensor(10.9204, device='cuda:0') (tensor(19.5419, device='cuda:0'))
| > loss_gen: 2.1531784534454346 (2.208908011173382)
| > loss_kl: 1.574000358581543 (1.5994170549859368)
| > loss_feat: 6.0521240234375 (6.7467871941564885)
| > loss_mel: 15.38608455657959 (15.488119997610209)
| > loss_duration: 1.4926962852478027 (1.4238011645174564)
| > amp_scaler: 128.0 (139.77011494252892)
| > loss_1: 26.658084869384766 (27.467033430077553)
| > grad_norm_1: tensor(145.8639, device='cuda:0') (tensor(227.4299, device='cuda:0'))
| > current_lr_0: 0.0001991766478707464
| > current_lr_1: 0.0001991766478707464
| > step_time: 1.0082 (0.6878550765158113)
| > loader_time: 0.0121 (0.008180039661075481)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.0049944718678792315 (-0.00026857852935791016)
| > avg_loss_disc: 2.5700851082801814 (-0.07582889000574822)
| > avg_loss_disc_real_0: 0.13117654745777446 (-0.09975523129105571)
| > avg_loss_disc_real_1: 0.24330608795086542 (+0.012466931094725908)
| > avg_loss_disc_real_2: 0.22379212329785028 (+0.0024155452847480774)
| > avg_loss_disc_real_3: 0.22776468843221664 (+0.015687646965185792)
| > avg_loss_disc_real_4: 0.265523595114549 (+0.025292427589495958)
| > avg_loss_disc_real_5: 0.23448720201849937 (+0.009074596067269652)
| > avg_loss_0: 2.5700851082801814 (-0.07582889000574822)
| > avg_loss_gen: 2.1220362385114035 (+0.04693921407063861)
| > avg_loss_kl: 1.6565354565779369 (-0.06152598063151027)
| > avg_loss_feat: 6.55951742331187 (+0.04958081245422363)
| > avg_loss_mel: 15.205196698506674 (-0.2788107395172119)
| > avg_loss_duration: 1.5444487531979878 (+0.009568959474563599)
| > avg_loss_1: 27.08773438135783 (-0.2342478434244768)
> EPOCH: 34/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 14:53:57)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 14:54:41 -- STEP: 79/630 -- GLOBAL_STEP: 898500
| > loss_disc: 2.5751755237579346 (2.57942318614525)
| > loss_disc_real_0: 0.19519412517547607 (0.1664852003885221)
| > loss_disc_real_1: 0.1793692409992218 (0.20924707266348827)
| > loss_disc_real_2: 0.27496373653411865 (0.2285476411822476)
| > loss_disc_real_3: 0.2280089557170868 (0.22917517755604996)
| > loss_disc_real_4: 0.24790190160274506 (0.24090282751035086)
| > loss_disc_real_5: 0.2551231384277344 (0.2378796022149581)
| > loss_0: 2.5751755237579346 (2.57942318614525)
| > grad_norm_0: tensor(10.2981, device='cuda:0') (tensor(11.8516, device='cuda:0'))
| > loss_gen: 2.232154607772827 (2.2155929154987577)
| > loss_kl: 1.7593824863433838 (1.578790260266654)
| > loss_feat: 6.659547805786133 (6.850612972356096)
| > loss_mel: 15.980627059936523 (15.413605122626583)
| > loss_duration: 1.4387905597686768 (1.432987954043135)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.07050323486328 (27.491589268551596)
| > grad_norm_1: tensor(63.2488, device='cuda:0') (tensor(110.5854, device='cuda:0'))
| > current_lr_0: 0.00019915175078976256
| > current_lr_1: 0.00019915175078976256
| > step_time: 0.5323 (0.5263152062138424)
| > loader_time: 0.0058 (0.005187973191466512)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_898500.pth
--> TIME: 2025-05-14 14:55:43 -- STEP: 179/630 -- GLOBAL_STEP: 898600
| > loss_disc: 2.616441249847412 (2.5734262919292767)
| > loss_disc_real_0: 0.11455436050891876 (0.1657541357188918)
| > loss_disc_real_1: 0.1824163794517517 (0.21057116935373016)
| > loss_disc_real_2: 0.2650325894355774 (0.22728455099979591)
| > loss_disc_real_3: 0.25396689772605896 (0.227660564736947)
| > loss_disc_real_4: 0.2734259068965912 (0.2398826713002594)
| > loss_disc_real_5: 0.27326464653015137 (0.23405347040245653)
| > loss_0: 2.616441249847412 (2.5734262919292767)
| > grad_norm_0: tensor(14.2551, device='cuda:0') (tensor(15.0219, device='cuda:0'))
| > loss_gen: 2.2671775817871094 (2.228391941699236)
| > loss_kl: 1.6068873405456543 (1.607609970609569)
| > loss_feat: 7.342446327209473 (6.915473314636911)
| > loss_mel: 14.940177917480469 (15.459526323073403)
| > loss_duration: 1.4499704837799072 (1.3797316331437173)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.606658935546875 (27.590733213797627)
| > grad_norm_1: tensor(177.8401, device='cuda:0') (tensor(167.2509, device='cuda:0'))
| > current_lr_0: 0.00019915175078976256
| > current_lr_1: 0.00019915175078976256
| > step_time: 0.5681 (0.5569287305437655)
| > loader_time: 0.0061 (0.005810741605705386)
--> TIME: 2025-05-14 14:56:45 -- STEP: 279/630 -- GLOBAL_STEP: 898700
| > loss_disc: 2.514106273651123 (2.574667479402276)
| > loss_disc_real_0: 0.17739459872245789 (0.1671714676430576)
| > loss_disc_real_1: 0.21044428646564484 (0.21117966325693227)
| > loss_disc_real_2: 0.21813523769378662 (0.22781604608540895)
| > loss_disc_real_3: 0.24001382291316986 (0.22717621911811145)
| > loss_disc_real_4: 0.2345772236585617 (0.23905698100512174)
| > loss_disc_real_5: 0.28801098465919495 (0.23367515681678677)
| > loss_0: 2.514106273651123 (2.574667479402276)
| > grad_norm_0: tensor(25.6895, device='cuda:0') (tensor(15.5110, device='cuda:0'))
| > loss_gen: 2.333103656768799 (2.222872025650462)
| > loss_kl: 1.449756145477295 (1.6181598085656392)
| > loss_feat: 6.107773303985596 (6.882529880838155)
| > loss_mel: 14.46749210357666 (15.504972745013493)
| > loss_duration: 1.4727933406829834 (1.387740190311144)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 25.830917358398438 (27.616274714042632)
| > grad_norm_1: tensor(332.4164, device='cuda:0') (tensor(176.4588, device='cuda:0'))
| > current_lr_0: 0.00019915175078976256
| > current_lr_1: 0.00019915175078976256
| > step_time: 0.6446 (0.576747384122623)
| > loader_time: 0.0081 (0.006345813846929952)
--> TIME: 2025-05-14 14:57:53 -- STEP: 379/630 -- GLOBAL_STEP: 898800
| > loss_disc: 2.360568046569824 (2.577730541807993)
| > loss_disc_real_0: 0.09256041049957275 (0.16810641958719827)
| > loss_disc_real_1: 0.2387160360813141 (0.21058675277201663)
| > loss_disc_real_2: 0.24945221841335297 (0.2289858471435104)
| > loss_disc_real_3: 0.2275611311197281 (0.2272106230573478)
| > loss_disc_real_4: 0.2424025535583496 (0.2401281678189074)
| > loss_disc_real_5: 0.2571871876716614 (0.23199504733793339)
| > loss_0: 2.360568046569824 (2.577730541807993)
| > grad_norm_0: tensor(8.6528, device='cuda:0') (tensor(17.0758, device='cuda:0'))
| > loss_gen: 2.610769271850586 (2.2280321404298573)
| > loss_kl: 1.6123363971710205 (1.6208945056693853)
| > loss_feat: 7.262279033660889 (6.866584540042525)
| > loss_mel: 16.88051414489746 (15.50877500901436)
| > loss_duration: 1.4828295707702637 (1.4065693689210421)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 29.848730087280273 (27.630855650889213)
| > grad_norm_1: tensor(166.9787, device='cuda:0') (tensor(194.2847, device='cuda:0'))
| > current_lr_0: 0.00019915175078976256
| > current_lr_1: 0.00019915175078976256
| > step_time: 0.656 (0.5995579948525945)
| > loader_time: 0.0083 (0.006874539921340337)
--> TIME: 2025-05-14 14:59:05 -- STEP: 479/630 -- GLOBAL_STEP: 898900
| > loss_disc: 2.5074119567871094 (2.582017422717895)
| > loss_disc_real_0: 0.1782332807779312 (0.16884322246703828)
| > loss_disc_real_1: 0.18875743448734283 (0.21118961125301164)
| > loss_disc_real_2: 0.2203720062971115 (0.22879725377345633)
| > loss_disc_real_3: 0.2587841749191284 (0.22776528368538754)
| > loss_disc_real_4: 0.2251819372177124 (0.23996204162689241)
| > loss_disc_real_5: 0.2501223683357239 (0.2326188246585382)
| > loss_0: 2.5074119567871094 (2.582017422717895)
| > grad_norm_0: tensor(18.8510, device='cuda:0') (tensor(16.5405, device='cuda:0'))
| > loss_gen: 2.2034380435943604 (2.214116061156875)
| > loss_kl: 1.4875112771987915 (1.6182327668701684)
| > loss_feat: 6.506922245025635 (6.79622569114032)
| > loss_mel: 15.642420768737793 (15.487700786869311)
| > loss_duration: 1.4557018280029297 (1.4088842759301607)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.29599380493164 (27.52515964866431)
| > grad_norm_1: tensor(227.5011, device='cuda:0') (tensor(184.3434, device='cuda:0'))
| > current_lr_0: 0.00019915175078976256
| > current_lr_1: 0.00019915175078976256
| > step_time: 0.7704 (0.6220550168780046)
| > loader_time: 0.0093 (0.0073957129659632794)
--> TIME: 2025-05-14 15:00:26 -- STEP: 579/630 -- GLOBAL_STEP: 899000
| > loss_disc: 2.480717182159424 (2.578635921955931)
| > loss_disc_real_0: 0.16271916031837463 (0.16899847222527495)
| > loss_disc_real_1: 0.22138024866580963 (0.21079658579229268)
| > loss_disc_real_2: 0.2110372930765152 (0.22874053337310468)
| > loss_disc_real_3: 0.2324146181344986 (0.2277560299696699)
| > loss_disc_real_4: 0.261865496635437 (0.2397013608244005)
| > loss_disc_real_5: 0.21992400288581848 (0.23129158649780177)
| > loss_0: 2.480717182159424 (2.578635921955931)
| > grad_norm_0: tensor(29.8113, device='cuda:0') (tensor(17.5170, device='cuda:0'))
| > loss_gen: 2.3853230476379395 (2.217253522551738)
| > loss_kl: 1.8124042749404907 (1.6186934845435184)
| > loss_feat: 7.7594733238220215 (6.787699851759152)
| > loss_mel: 16.20210838317871 (15.484115379873748)
| > loss_duration: 1.4862221479415894 (1.4189648580880558)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 29.645530700683594 (27.526727155906137)
| > grad_norm_1: tensor(271.7693, device='cuda:0') (tensor(199.1724, device='cuda:0'))
| > current_lr_0: 0.00019915175078976256
| > current_lr_1: 0.00019915175078976256
| > step_time: 0.9655 (0.6508029096073022)
| > loader_time: 0.0133 (0.00800056572816944)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_899000.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005421082178751628 (+0.0004266103108723964)
| > avg_loss_disc: 2.7059929172197976 (+0.13590780893961618)
| > avg_loss_disc_real_0: 0.13427164591848853 (+0.0030950984607140686)
| > avg_loss_disc_real_1: 0.25899436076482135 (+0.015688272813955934)
| > avg_loss_disc_real_2: 0.21106203769644102 (-0.012730085601409258)
| > avg_loss_disc_real_3: 0.24557447681824365 (+0.01780978838602701)
| > avg_loss_disc_real_4: 0.2589929228027662 (-0.006530672311782781)
| > avg_loss_disc_real_5: 0.26592854658762616 (+0.03144134456912678)
| > avg_loss_0: 2.7059929172197976 (+0.13590780893961618)
| > avg_loss_gen: 2.0076655546824136 (-0.11437068382898996)
| > avg_loss_kl: 1.628996580839157 (-0.027538875738779778)
| > avg_loss_feat: 6.508604645729065 (-0.05091277758280466)
| > avg_loss_mel: 15.820404847462973 (+0.6152081489562988)
| > avg_loss_duration: 1.5369081695874531 (-0.007540583610534668)
| > avg_loss_1: 27.502580165863037 (+0.41484578450520715)
> EPOCH: 35/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:01:32)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:01:59 -- STEP: 49/630 -- GLOBAL_STEP: 899100
| > loss_disc: 2.4239773750305176 (2.5659909248352046)
| > loss_disc_real_0: 0.14973825216293335 (0.1641153284177488)
| > loss_disc_real_1: 0.22234749794006348 (0.22107549589507433)
| > loss_disc_real_2: 0.22665554285049438 (0.22521746797221048)
| > loss_disc_real_3: 0.22894230484962463 (0.22345253460261286)
| > loss_disc_real_4: 0.22130566835403442 (0.242072088986027)
| > loss_disc_real_5: 0.22072291374206543 (0.2231228476276203)
| > loss_0: 2.4239773750305176 (2.5659909248352046)
| > grad_norm_0: tensor(34.1354, device='cuda:0') (tensor(20.1411, device='cuda:0'))
| > loss_gen: 2.2493555545806885 (2.211717617755034)
| > loss_kl: 1.5215932130813599 (1.5095133805761531)
| > loss_feat: 6.718974590301514 (6.86573230003824)
| > loss_mel: 15.340112686157227 (15.590560952011419)
| > loss_duration: 1.4553570747375488 (1.426697952406747)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.28539276123047 (27.6042223171312)
| > grad_norm_1: tensor(479.6996, device='cuda:0') (tensor(263.4774, device='cuda:0'))
| > current_lr_0: 0.00019912685682091382
| > current_lr_1: 0.00019912685682091382
| > step_time: 0.5418 (0.5259993952147816)
| > loader_time: 0.0056 (0.005122024185803471)
--> TIME: 2025-05-14 15:02:56 -- STEP: 149/630 -- GLOBAL_STEP: 899200
| > loss_disc: 2.5638556480407715 (2.5666363735326976)
| > loss_disc_real_0: 0.208571657538414 (0.16513079694853539)
| > loss_disc_real_1: 0.15306198596954346 (0.21395828379880663)
| > loss_disc_real_2: 0.24654851853847504 (0.22619443881831713)
| > loss_disc_real_3: 0.22353030741214752 (0.22981864143938027)
| > loss_disc_real_4: 0.2150917500257492 (0.24076791987723153)
| > loss_disc_real_5: 0.19888265430927277 (0.22401698293701913)
| > loss_0: 2.5638556480407715 (2.5666363735326976)
| > grad_norm_0: tensor(24.2762, device='cuda:0') (tensor(26.0935, device='cuda:0'))
| > loss_gen: 2.0916266441345215 (2.2426867493046996)
| > loss_kl: 1.705533742904663 (1.54833902528622)
| > loss_feat: 7.495947360992432 (6.885111680766879)
| > loss_mel: 15.605327606201172 (15.541430172504194)
| > loss_duration: 1.4233824014663696 (1.3716330608265512)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 28.32181739807129 (27.58920062788382)
| > grad_norm_1: tensor(342.3159, device='cuda:0') (tensor(344.4819, device='cuda:0'))
| > current_lr_0: 0.00019912685682091382
| > current_lr_1: 0.00019912685682091382
| > step_time: 0.568 (0.5493572254308919)
| > loader_time: 0.006 (0.005684057338125752)
--> TIME: 2025-05-14 15:03:58 -- STEP: 249/630 -- GLOBAL_STEP: 899300
| > loss_disc: 2.654385566711426 (2.5772836055142805)
| > loss_disc_real_0: 0.2239164113998413 (0.16650425594853588)
| > loss_disc_real_1: 0.1997099220752716 (0.21308463051855325)
| > loss_disc_real_2: 0.2603133022785187 (0.22564542760331946)
| > loss_disc_real_3: 0.2167835831642151 (0.2286212031381676)
| > loss_disc_real_4: 0.23251387476921082 (0.24135160601761446)
| > loss_disc_real_5: 0.2363336980342865 (0.23030827753993882)
| > loss_0: 2.654385566711426 (2.5772836055142805)
| > grad_norm_0: tensor(8.6865, device='cuda:0') (tensor(21.1807, device='cuda:0'))
| > loss_gen: 2.0416574478149414 (2.216007636254089)
| > loss_kl: 1.902483582496643 (1.5706155625691853)
| > loss_feat: 6.051441669464111 (6.794444428869039)
| > loss_mel: 15.746969223022461 (15.481597992311041)
| > loss_duration: 1.4290142059326172 (1.38230753758825)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.17156410217285 (27.444973068543714)
| > grad_norm_1: tensor(79.8894, device='cuda:0') (tensor(263.2690, device='cuda:0'))
| > current_lr_0: 0.00019912685682091382
| > current_lr_1: 0.00019912685682091382
| > step_time: 0.6218 (0.5722913770790559)
| > loader_time: 0.0074 (0.006260616233549921)
--> TIME: 2025-05-14 15:05:06 -- STEP: 349/630 -- GLOBAL_STEP: 899400
| > loss_disc: 2.562516927719116 (2.573511588197726)
| > loss_disc_real_0: 0.1511302888393402 (0.1667913094931482)
| > loss_disc_real_1: 0.2044755071401596 (0.21225141151074353)
| > loss_disc_real_2: 0.21291202306747437 (0.2260732884307987)
| > loss_disc_real_3: 0.23122258484363556 (0.22978072987074155)
| > loss_disc_real_4: 0.23428310453891754 (0.24016831196140082)
| > loss_disc_real_5: 0.18493328988552094 (0.2289823465753763)
| > loss_0: 2.562516927719116 (2.573511588197726)
| > grad_norm_0: tensor(10.5751, device='cuda:0') (tensor(19.8025, device='cuda:0'))
| > loss_gen: 2.2070443630218506 (2.219276367080926)
| > loss_kl: 1.6522713899612427 (1.5753004492866276)
| > loss_feat: 7.477463722229004 (6.799275078541226)
| > loss_mel: 15.232359886169434 (15.48468019764198)
| > loss_duration: 1.4287440776824951 (1.4037556176882435)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.997882843017578 (27.48228766105237)
| > grad_norm_1: tensor(58.7481, device='cuda:0') (tensor(243.2588, device='cuda:0'))
| > current_lr_0: 0.00019912685682091382
| > current_lr_1: 0.00019912685682091382
| > step_time: 0.6905 (0.5998187208585546)
| > loader_time: 0.0093 (0.00676018802347702)
--> TIME: 2025-05-14 15:06:23 -- STEP: 449/630 -- GLOBAL_STEP: 899500
| > loss_disc: 2.685792922973633 (2.5750452086229907)
| > loss_disc_real_0: 0.20468907058238983 (0.16689070227881583)
| > loss_disc_real_1: 0.1749895066022873 (0.21244548032172272)
| > loss_disc_real_2: 0.2170199602842331 (0.22665118444337612)
| > loss_disc_real_3: 0.2478378266096115 (0.22937793515307336)
| > loss_disc_real_4: 0.29915785789489746 (0.2397081990018985)
| > loss_disc_real_5: 0.2987678349018097 (0.22990786236086508)
| > loss_0: 2.685792922973633 (2.5750452086229907)
| > grad_norm_0: tensor(7.6681, device='cuda:0') (tensor(20.6467, device='cuda:0'))
| > loss_gen: 2.2239737510681152 (2.224221526381696)
| > loss_kl: 1.5884007215499878 (1.579711956542425)
| > loss_feat: 5.7930755615234375 (6.807169661490049)
| > loss_mel: 15.50680160522461 (15.520425307989651)
| > loss_duration: 1.4403491020202637 (1.4064030472048155)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 26.552602767944336 (27.537931425268777)
| > grad_norm_1: tensor(105.4764, device='cuda:0') (tensor(241.8343, device='cuda:0'))
| > current_lr_0: 0.00019912685682091382
| > current_lr_1: 0.00019912685682091382
| > step_time: 0.7743 (0.6323911209148928)
| > loader_time: 0.0102 (0.007355015102632855)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_899500.pth
--> TIME: 2025-05-14 15:07:50 -- STEP: 549/630 -- GLOBAL_STEP: 899600
| > loss_disc: 2.5563273429870605 (2.5746900462061983)
| > loss_disc_real_0: 0.16526931524276733 (0.16740536877040654)
| > loss_disc_real_1: 0.18564102053642273 (0.21218660012403254)
| > loss_disc_real_2: 0.1910644918680191 (0.22633498250243875)
| > loss_disc_real_3: 0.2493700534105301 (0.22935790477663226)
| > loss_disc_real_4: 0.22177988290786743 (0.23933480785844105)
| > loss_disc_real_5: 0.2053566426038742 (0.23070440013877677)
| > loss_0: 2.5563273429870605 (2.5746900462061983)
| > grad_norm_0: tensor(13.3089, device='cuda:0') (tensor(19.0730, device='cuda:0'))
| > loss_gen: 2.202301263809204 (2.220295897598473)
| > loss_kl: 1.413133978843689 (1.580734455303199)
| > loss_feat: 6.551865100860596 (6.783484887989924)
| > loss_mel: 15.663331985473633 (15.508894809173974)
| > loss_duration: 1.4830223321914673 (1.416951588594198)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.31365394592285 (27.510361544638602)
| > grad_norm_1: tensor(177.8032, device='cuda:0') (tensor(217.8615, device='cuda:0'))
| > current_lr_0: 0.00019912685682091382
| > current_lr_1: 0.00019912685682091382
| > step_time: 0.8742 (0.6675642266299558)
| > loader_time: 0.0124 (0.007919443978203667)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005267500877380371 (-0.0001535813013712568)
| > avg_loss_disc: 2.634272654851278 (-0.0717202623685198)
| > avg_loss_disc_real_0: 0.16900225604573885 (+0.034730610127250316)
| > avg_loss_disc_real_1: 0.20402215421199799 (-0.054972206552823366)
| > avg_loss_disc_real_2: 0.17274603620171547 (-0.038316001494725554)
| > avg_loss_disc_real_3: 0.21529229978720346 (-0.03028217703104019)
| > avg_loss_disc_real_4: 0.22162757565577826 (-0.03736534714698794)
| > avg_loss_disc_real_5: 0.23041601479053497 (-0.035512531797091185)
| > avg_loss_0: 2.634272654851278 (-0.0717202623685198)
| > avg_loss_gen: 1.9533033470312755 (-0.054362207651138084)
| > avg_loss_kl: 1.7371280292669933 (+0.10813144842783617)
| > avg_loss_feat: 6.790953318277995 (+0.28234867254893015)
| > avg_loss_mel: 15.33866278330485 (-0.48174206415812293)
| > avg_loss_duration: 1.5322692692279816 (-0.004638900359471565)
| > avg_loss_1: 27.352316697438557 (-0.15026346842448035)
> EPOCH: 36/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:09:23)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:09:34 -- STEP: 19/630 -- GLOBAL_STEP: 899700
| > loss_disc: 2.604736804962158 (2.6335750379060445)
| > loss_disc_real_0: 0.30384302139282227 (0.17254657612035149)
| > loss_disc_real_1: 0.23111411929130554 (0.22418618280636637)
| > loss_disc_real_2: 0.24448087811470032 (0.23490850470568003)
| > loss_disc_real_3: 0.23169288039207458 (0.24362017214298248)
| > loss_disc_real_4: 0.24205417931079865 (0.2404584947385286)
| > loss_disc_real_5: 0.27604666352272034 (0.24345202116589798)
| > loss_0: 2.604736804962158 (2.6335750379060445)
| > grad_norm_0: tensor(11.3216, device='cuda:0') (tensor(15.3785, device='cuda:0'))
| > loss_gen: 2.184623956680298 (2.2348152775513497)
| > loss_kl: 1.752730131149292 (1.5139408425280922)
| > loss_feat: 7.00317907333374 (7.065659673590409)
| > loss_mel: 14.873517036437988 (15.165256249277215)
| > loss_duration: 1.4095301628112793 (1.4217925322683234)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.22357940673828 (27.401464863827353)
| > grad_norm_1: tensor(43.3221, device='cuda:0') (tensor(159.8932, device='cuda:0'))
| > current_lr_0: 0.0001991019659638112
| > current_lr_1: 0.0001991019659638112
| > step_time: 0.5245 (0.5212156145196212)
| > loader_time: 0.0055 (0.004809768576371043)
--> TIME: 2025-05-14 15:10:30 -- STEP: 119/630 -- GLOBAL_STEP: 899800
| > loss_disc: 2.6138527393341064 (2.586260002200344)
| > loss_disc_real_0: 0.14444002509117126 (0.1666585370397367)
| > loss_disc_real_1: 0.2545340657234192 (0.21399869976424368)
| > loss_disc_real_2: 0.23249328136444092 (0.2338636308407583)
| > loss_disc_real_3: 0.22955293953418732 (0.23256489960085444)
| > loss_disc_real_4: 0.23520922660827637 (0.23948139891404063)
| > loss_disc_real_5: 0.23552672564983368 (0.22955736830955795)
| > loss_0: 2.6138527393341064 (2.586260002200344)
| > grad_norm_0: tensor(48.8532, device='cuda:0') (tensor(19.5783, device='cuda:0'))
| > loss_gen: 2.0673723220825195 (2.2400804096911133)
| > loss_kl: 1.4993226528167725 (1.5792241407041792)
| > loss_feat: 6.916788578033447 (6.964194033326221)
| > loss_mel: 15.511136054992676 (15.430317710427676)
| > loss_duration: 1.4687144756317139 (1.3917450654406511)
| > amp_scaler: 128.0 (128.0)
| > loss_1: 27.46333122253418 (27.60556140867602)
| > grad_norm_1: tensor(295.3477, device='cuda:0') (tensor(237.3636, device='cuda:0'))
| > current_lr_0: 0.0001991019659638112
| > current_lr_1: 0.0001991019659638112
| > step_time: 0.5493 (0.5406288219099286)
| > loader_time: 0.0063 (0.005513772243211249)
--> TIME: 2025-05-14 15:11:31 -- STEP: 219/630 -- GLOBAL_STEP: 899900
| > loss_disc: 2.423008441925049 (2.5843412375341277)
| > loss_disc_real_0: 0.0981687381863594 (0.1669735361111762)
| > loss_disc_real_1: 0.15162530541419983 (0.21372426529181057)
| > loss_disc_real_2: 0.20324134826660156 (0.23159262578781337)
| > loss_disc_real_3: 0.19832831621170044 (0.23242419570276182)
| > loss_disc_real_4: 0.2127227932214737 (0.23965678782495733)
| > loss_disc_real_5: 0.2252073884010315 (0.22812059337962165)
| > loss_0: 2.423008441925049 (2.5843412375341277)
| > grad_norm_0: tensor(20.1493, device='cuda:0') (tensor(22.9055, device='cuda:0'))
| > loss_gen: 2.2251973152160645 (2.240224484983646)
| > loss_kl: 1.6351995468139648 (1.5746668163499877)
| > loss_feat: 7.056931018829346 (6.886826802606452)
| > loss_mel: 14.603894233703613 (15.457950883804392)
| > loss_duration: 1.4860332012176514 (1.3672558695213985)
| > amp_scaler: 256.0 (158.97716894977168)
| > loss_1: 27.007253646850586 (27.526924891014623)
| > grad_norm_1: tensor(298.2769, device='cuda:0') (tensor(273.6656, device='cuda:0'))
| > current_lr_0: 0.0001991019659638112
| > current_lr_1: 0.0001991019659638112
| > step_time: 0.5911 (0.5686666802184221)
| > loader_time: 0.0072 (0.0060954181026650345)
--> TIME: 2025-05-14 15:12:36 -- STEP: 319/630 -- GLOBAL_STEP: 900000
| > loss_disc: 2.5562350749969482 (2.5826840886501694)
| > loss_disc_real_0: 0.2568713426589966 (0.16746938114162513)
| > loss_disc_real_1: 0.1911785900592804 (0.21306358936438358)
| > loss_disc_real_2: 0.18227435648441315 (0.23058314046889636)
| > loss_disc_real_3: 0.21896277368068695 (0.23242367640558081)
| > loss_disc_real_4: 0.24479062855243683 (0.23931640778963095)
| > loss_disc_real_5: 0.24830856919288635 (0.2280244253178749)
| > loss_0: 2.5562350749969482 (2.5826840886501694)
| > grad_norm_0: tensor(48.3969, device='cuda:0') (tensor(22.5075, device='cuda:0'))
| > loss_gen: 2.229398727416992 (2.2336354285572027)
| > loss_kl: 1.7698734998703003 (1.5765974304892796)
| > loss_feat: 5.964440822601318 (6.8350577339483305)
| > loss_mel: 14.9555082321167 (15.431060892661163)
| > loss_duration: 1.489117980003357 (1.3954386666276997)
| > amp_scaler: 256.0 (189.39184952978053)
| > loss_1: 26.408340454101562 (27.471790182179408)
| > grad_norm_1: tensor(392.3644, device='cuda:0') (tensor(267.0042, device='cuda:0'))
| > current_lr_0: 0.0001991019659638112
| > current_lr_1: 0.0001991019659638112
| > step_time: 0.6711 (0.5901012876564435)
| > loader_time: 0.0079 (0.006613456343408662)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_900000.pth
--> TIME: 2025-05-14 15:13:53 -- STEP: 419/630 -- GLOBAL_STEP: 900100
| > loss_disc: 2.7539546489715576 (2.5802943325270356)
| > loss_disc_real_0: 0.15019591152668 (0.16778919502630443)
| > loss_disc_real_1: 0.30123910307884216 (0.21265475935611627)
| > loss_disc_real_2: 0.2535560429096222 (0.22990406505532368)
| > loss_disc_real_3: 0.23110055923461914 (0.2317059536182226)
| > loss_disc_real_4: 0.2362973988056183 (0.2395584252896343)
| > loss_disc_real_5: 0.24299350380897522 (0.22849803330790172)
| > loss_0: 2.7539546489715576 (2.5802943325270356)
| > grad_norm_0: tensor(31.7259, device='cuda:0') (tensor(21.9885, device='cuda:0'))
| > loss_gen: 2.192085027694702 (2.2315405937254007)
| > loss_kl: 1.6633126735687256 (1.5884528680746763)
| > loss_feat: 6.212068557739258 (6.808568626713357)
| > loss_mel: 15.350135803222656 (15.411433288191839)
| > loss_duration: 1.4649348258972168 (1.3986830048458674)
| > amp_scaler: 256.0 (205.28878281622906)
| > loss_1: 26.882537841796875 (27.43867842280494)
| > grad_norm_1: tensor(199.6527, device='cuda:0') (tensor(260.7267, device='cuda:0'))
| > current_lr_0: 0.0001991019659638112
| > current_lr_1: 0.0001991019659638112
| > step_time: 0.7442 (0.6216731162515065)
| > loader_time: 0.0092 (0.007190774334928016)
--> TIME: 2025-05-14 15:15:13 -- STEP: 519/630 -- GLOBAL_STEP: 900200
| > loss_disc: 2.6507768630981445 (2.580366028067236)
| > loss_disc_real_0: 0.1502837985754013 (0.16807675407571374)
| > loss_disc_real_1: 0.19515953958034515 (0.21234556995260456)
| > loss_disc_real_2: 0.2330145686864853 (0.22934406613913116)
| > loss_disc_real_3: 0.19693204760551453 (0.23139424794326627)
| > loss_disc_real_4: 0.252015620470047 (0.23922423633651696)
| > loss_disc_real_5: 0.21145687997341156 (0.22961792550794421)
| > loss_0: 2.6507768630981445 (2.580366028067236)
| > grad_norm_0: tensor(12.3919, device='cuda:0') (tensor(21.7820, device='cuda:0'))
| > loss_gen: 2.0455868244171143 (2.226812587997127)
| > loss_kl: 1.4592654705047607 (1.592149616895613)
| > loss_feat: 7.500457286834717 (6.760775991487597)
| > loss_mel: 15.191999435424805 (15.401793619571164)
| > loss_duration: 1.4152519702911377 (1.4101942837353156)
| > amp_scaler: 256.0 (215.05973025048164)
| > loss_1: 27.61256217956543 (27.391726109793186)
| > grad_norm_1: tensor(38.2301, device='cuda:0') (tensor(253.7452, device='cuda:0'))
| > current_lr_0: 0.0001991019659638112
| > current_lr_1: 0.0001991019659638112
| > step_time: 0.8394 (0.6536615804440715)
| > loader_time: 0.0107 (0.007753377245570424)
--> TIME: 2025-05-14 15:16:49 -- STEP: 619/630 -- GLOBAL_STEP: 900300
| > loss_disc: 2.6136295795440674 (2.577116682379237)
| > loss_disc_real_0: 0.19605055451393127 (0.168316406488226)
| > loss_disc_real_1: 0.22597748041152954 (0.21222246242070228)
| > loss_disc_real_2: 0.2327105700969696 (0.22869995763594578)
| > loss_disc_real_3: 0.23400607705116272 (0.23102956593806992)
| > loss_disc_real_4: 0.22964051365852356 (0.2391178221569693)
| > loss_disc_real_5: 0.19730325043201447 (0.22936170583106397)
| > loss_0: 2.6136295795440674 (2.577116682379237)
| > grad_norm_0: tensor(12.8888, device='cuda:0') (tensor(21.0958, device='cuda:0'))
| > loss_gen: 2.18489670753479 (2.226555664627926)
| > loss_kl: 1.6281003952026367 (1.598407051867546)
| > loss_feat: 6.557600498199463 (6.749233287447685)
| > loss_mel: 15.305011749267578 (15.383578278906704)
| > loss_duration: 1.5268937349319458 (1.4200515148135118)
| > amp_scaler: 256.0 (221.67366720516958)
| > loss_1: 27.202503204345703 (27.377825803248292)
| > grad_norm_1: tensor(161.5792, device='cuda:0') (tensor(246.7506, device='cuda:0'))
| > current_lr_0: 0.0001991019659638112
| > current_lr_1: 0.0001991019659638112
| > step_time: 1.1319 (0.7001367840127534)
| > loader_time: 0.0143 (0.008425718748126539)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005117654800415039 (-0.00014984607696533203)
| > avg_loss_disc: 2.6213772892951965 (-0.012895365556081284)
| > avg_loss_disc_real_0: 0.29679201791683835 (+0.1277897618710995)
| > avg_loss_disc_real_1: 0.19582734008630118 (-0.008194814125696809)
| > avg_loss_disc_real_2: 0.2724359979232152 (+0.09968996172149974)
| > avg_loss_disc_real_3: 0.22745936488111815 (+0.012167065093914686)
| > avg_loss_disc_real_4: 0.257013193021218 (+0.03538561736543974)
| > avg_loss_disc_real_5: 0.24053462594747543 (+0.01011861115694046)
| > avg_loss_0: 2.6213772892951965 (-0.012895365556081284)
| > avg_loss_gen: 2.3334860205650325 (+0.380182673533757)
| > avg_loss_kl: 1.8034574588139851 (+0.06632942954699184)
| > avg_loss_feat: 6.5121144851048784 (-0.27883883317311664)
| > avg_loss_mel: 15.419529914855957 (+0.08086713155110736)
| > avg_loss_duration: 1.524087021748225 (-0.0081822474797566)
| > avg_loss_1: 27.592674732208252 (+0.2403580347696952)
> EPOCH: 37/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:17:12)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:18:01 -- STEP: 89/630 -- GLOBAL_STEP: 900400
| > loss_disc: 2.4946541786193848 (2.560919847381249)
| > loss_disc_real_0: 0.14217323064804077 (0.1639767884370985)
| > loss_disc_real_1: 0.22339200973510742 (0.21002136689893317)
| > loss_disc_real_2: 0.20334972441196442 (0.22953846046094145)
| > loss_disc_real_3: 0.24117763340473175 (0.23136005893851933)
| > loss_disc_real_4: 0.23276643455028534 (0.23932999205053523)
| > loss_disc_real_5: 0.1934085637331009 (0.2291972374313333)
| > loss_0: 2.4946541786193848 (2.560919847381249)
| > grad_norm_0: tensor(7.3181, device='cuda:0') (tensor(16.4305, device='cuda:0'))
| > loss_gen: 2.168087959289551 (2.245085661330919)
| > loss_kl: 2.0154643058776855 (1.5813597574662623)
| > loss_feat: 7.1888322830200195 (7.0923343508431085)
| > loss_mel: 15.523865699768066 (15.384503171685036)
| > loss_duration: 1.4244070053100586 (1.429648819934116)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.320655822753906 (27.7329316085644)
| > grad_norm_1: tensor(142.5478, device='cuda:0') (tensor(181.2209, device='cuda:0'))
| > current_lr_0: 0.0001990770782180657
| > current_lr_1: 0.0001990770782180657
| > step_time: 0.5519 (0.5320678025149226)
| > loader_time: 0.0066 (0.005331585916240564)
--> TIME: 2025-05-14 15:19:00 -- STEP: 189/630 -- GLOBAL_STEP: 900500
| > loss_disc: 2.5265345573425293 (2.5643232095809205)
| > loss_disc_real_0: 0.263235479593277 (0.1645793088529475)
| > loss_disc_real_1: 0.20201019942760468 (0.20912048378318707)
| > loss_disc_real_2: 0.23948323726654053 (0.2269853945604708)
| > loss_disc_real_3: 0.238648921251297 (0.23147026965857814)
| > loss_disc_real_4: 0.22878998517990112 (0.240077959324317)
| > loss_disc_real_5: 0.2375645637512207 (0.23105875753536426)
| > loss_0: 2.5265345573425293 (2.5643232095809205)
| > grad_norm_0: tensor(35.5330, device='cuda:0') (tensor(17.8945, device='cuda:0'))
| > loss_gen: 2.3065602779388428 (2.249178213417215)
| > loss_kl: 1.7032253742218018 (1.5984622366213919)
| > loss_feat: 6.126160621643066 (6.981725296646199)
| > loss_mel: 14.998109817504883 (15.469291142054967)
| > loss_duration: 1.4719207286834717 (1.3879470106155147)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.605976104736328 (27.686603929630667)
| > grad_norm_1: tensor(233.7034, device='cuda:0') (tensor(214.8238, device='cuda:0'))
| > current_lr_0: 0.0001990770782180657
| > current_lr_1: 0.0001990770782180657
| > step_time: 0.5968 (0.5568190352626575)
| > loader_time: 0.0074 (0.005910725820632208)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_900500.pth
--> TIME: 2025-05-14 15:20:08 -- STEP: 289/630 -- GLOBAL_STEP: 900600
| > loss_disc: 2.5537567138671875 (2.563810495356787)
| > loss_disc_real_0: 0.14214389026165009 (0.16520907134333282)
| > loss_disc_real_1: 0.22557945549488068 (0.20960737354924522)
| > loss_disc_real_2: 0.1938353180885315 (0.22736817149761226)
| > loss_disc_real_3: 0.22262853384017944 (0.22989189109175262)
| > loss_disc_real_4: 0.2379276156425476 (0.239697008654733)
| > loss_disc_real_5: 0.26693132519721985 (0.23040875972967248)
| > loss_0: 2.5537567138671875 (2.563810495356787)
| > grad_norm_0: tensor(8.0758, device='cuda:0') (tensor(19.9583, device='cuda:0'))
| > loss_gen: 2.057957649230957 (2.2515753128124354)
| > loss_kl: 1.57237708568573 (1.6109421570820788)
| > loss_feat: 5.544416427612305 (6.948611266060271)
| > loss_mel: 15.321554183959961 (15.471224299764138)
| > loss_duration: 1.4576241970062256 (1.3901927512409773)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.953927993774414 (27.672545713536884)
| > grad_norm_1: tensor(48.0734, device='cuda:0') (tensor(238.8324, device='cuda:0'))
| > current_lr_0: 0.0001990770782180657
| > current_lr_1: 0.0001990770782180657
| > step_time: 0.6463 (0.5802389651433816)
| > loader_time: 0.0072 (0.00641419813294724)
--> TIME: 2025-05-14 15:21:18 -- STEP: 389/630 -- GLOBAL_STEP: 900700
| > loss_disc: 2.4389538764953613 (2.563735278529186)
| > loss_disc_real_0: 0.12935912609100342 (0.16500428008696108)
| > loss_disc_real_1: 0.15963426232337952 (0.20969231654638495)
| > loss_disc_real_2: 0.2706110179424286 (0.22697209626206397)
| > loss_disc_real_3: 0.2548009753227234 (0.23010131647776821)
| > loss_disc_real_4: 0.22664032876491547 (0.23908859261510304)
| > loss_disc_real_5: 0.24173569679260254 (0.2305611814049032)
| > loss_0: 2.4389538764953613 (2.563735278529186)
| > grad_norm_0: tensor(18.5758, device='cuda:0') (tensor(19.6987, device='cuda:0'))
| > loss_gen: 2.479889392852783 (2.2467529923872953)
| > loss_kl: 1.6370744705200195 (1.611285406397056)
| > loss_feat: 6.528133392333984 (6.9073673900417925)
| > loss_mel: 15.580540657043457 (15.466691286827421)
| > loss_duration: 1.4845266342163086 (1.4070994740586653)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.710163116455078 (27.63919648903501)
| > grad_norm_1: tensor(473.5319, device='cuda:0') (tensor(233.9213, device='cuda:0'))
| > current_lr_0: 0.0001990770782180657
| > current_lr_1: 0.0001990770782180657
| > step_time: 0.7158 (0.6094239695826043)
| > loader_time: 0.0086 (0.006933052925953215)
--> TIME: 2025-05-14 15:22:36 -- STEP: 489/630 -- GLOBAL_STEP: 900800
| > loss_disc: 2.7677628993988037 (2.5582561434412265)
| > loss_disc_real_0: 0.17988191545009613 (0.16502449212020648)
| > loss_disc_real_1: 0.24900199472904205 (0.20940141363073225)
| > loss_disc_real_2: 0.27629420161247253 (0.22687199800170516)
| > loss_disc_real_3: 0.2480325847864151 (0.2292706666243832)
| > loss_disc_real_4: 0.3067357540130615 (0.2391684602313734)
| > loss_disc_real_5: 0.2584761381149292 (0.22847323329902133)
| > loss_0: 2.7677628993988037 (2.5582561434412265)
| > grad_norm_0: tensor(13.6712, device='cuda:0') (tensor(20.2246, device='cuda:0'))
| > loss_gen: 2.30202317237854 (2.254590614197932)
| > loss_kl: 1.597883939743042 (1.6056347931820916)
| > loss_feat: 6.5503950119018555 (6.905194791548091)
| > loss_mel: 15.915780067443848 (15.466520752155951)
| > loss_duration: 1.4743854999542236 (1.4093002353952944)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.840469360351562 (27.641241108712975)
| > grad_norm_1: tensor(63.0065, device='cuda:0') (tensor(244.5108, device='cuda:0'))
| > current_lr_0: 0.0001990770782180657
| > current_lr_1: 0.0001990770782180657
| > step_time: 0.8004 (0.6406559349325291)
| > loader_time: 0.0106 (0.007493347721840949)
--> TIME: 2025-05-14 15:24:05 -- STEP: 589/630 -- GLOBAL_STEP: 900900
| > loss_disc: 2.536186933517456 (2.5667267784805143)
| > loss_disc_real_0: 0.20589879155158997 (0.16608169435164513)
| > loss_disc_real_1: 0.21708156168460846 (0.20994433959240824)
| > loss_disc_real_2: 0.22160182893276215 (0.22693781865877694)
| > loss_disc_real_3: 0.237621009349823 (0.2296813276354445)
| > loss_disc_real_4: 0.2318495810031891 (0.23963156216010983)
| > loss_disc_real_5: 0.24049730598926544 (0.2304885673806299)
| > loss_0: 2.536186933517456 (2.5667267784805143)
| > grad_norm_0: tensor(9.4817, device='cuda:0') (tensor(19.1451, device='cuda:0'))
| > loss_gen: 2.200383186340332 (2.240939173309832)
| > loss_kl: 1.817124843597412 (1.6076445014853225)
| > loss_feat: 6.466090202331543 (6.837496856274955)
| > loss_mel: 15.942034721374512 (15.471882735934038)
| > loss_duration: 1.4691238403320312 (1.418736334769956)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.894756317138672 (27.57669953377015)
| > grad_norm_1: tensor(64.1545, device='cuda:0') (tensor(224.3870, device='cuda:0'))
| > current_lr_0: 0.0001990770782180657
| > current_lr_1: 0.0001990770782180657
| > step_time: 1.0043 (0.680469474889629)
| > loader_time: 0.013 (0.008134014942447677)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005035102367401123 (-8.255243301391602e-05)
| > avg_loss_disc: 2.6300350030263266 (+0.008657713731130112)
| > avg_loss_disc_real_0: 0.14678805073102316 (-0.15000396718581518)
| > avg_loss_disc_real_1: 0.27201201890905696 (+0.07618467882275579)
| > avg_loss_disc_real_2: 0.2508363078037898 (-0.02159969011942542)
| > avg_loss_disc_real_3: 0.27515751992662746 (+0.04769815504550931)
| > avg_loss_disc_real_4: 0.2868642248213291 (+0.029851031800111116)
| > avg_loss_disc_real_5: 0.22232718765735626 (-0.01820743829011917)
| > avg_loss_0: 2.6300350030263266 (+0.008657713731130112)
| > avg_loss_gen: 2.178561727205912 (-0.1549242933591204)
| > avg_loss_kl: 1.6424353917439778 (-0.16102206707000732)
| > avg_loss_feat: 6.0774409373601275 (-0.434673547744751)
| > avg_loss_mel: 15.343431870142618 (-0.07609804471333881)
| > avg_loss_duration: 1.5358441174030304 (+0.011757095654805427)
| > avg_loss_1: 26.777714252471924 (-0.8149604797363281)
> EPOCH: 38/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:25:00)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:25:33 -- STEP: 59/630 -- GLOBAL_STEP: 901000
| > loss_disc: 2.5185282230377197 (2.556205798003633)
| > loss_disc_real_0: 0.18509531021118164 (0.1628049130914575)
| > loss_disc_real_1: 0.1885831356048584 (0.2139875992374905)
| > loss_disc_real_2: 0.23172786831855774 (0.2294067475250212)
| > loss_disc_real_3: 0.24528905749320984 (0.22800456517833775)
| > loss_disc_real_4: 0.22017477452754974 (0.2403588466725107)
| > loss_disc_real_5: 0.20634160935878754 (0.22472496608556328)
| > loss_0: 2.5185282230377197 (2.556205798003633)
| > grad_norm_0: tensor(14.2574, device='cuda:0') (tensor(18.8968, device='cuda:0'))
| > loss_gen: 2.2241194248199463 (2.264292789717852)
| > loss_kl: 1.6596559286117554 (1.5253825874651896)
| > loss_feat: 7.3409528732299805 (7.209048044883598)
| > loss_mel: 15.78722858428955 (15.675198264041189)
| > loss_duration: 1.4343864917755127 (1.4250961865408946)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.44634437561035 (28.099018064595885)
| > grad_norm_1: tensor(247.6453, device='cuda:0') (tensor(254.2647, device='cuda:0'))
| > current_lr_0: 0.00019905219358328844
| > current_lr_1: 0.00019905219358328844
| > step_time: 0.5293 (0.5288111799854344)
| > loader_time: 0.0053 (0.005220930455094677)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_901000.pth
--> TIME: 2025-05-14 15:26:34 -- STEP: 159/630 -- GLOBAL_STEP: 901100
| > loss_disc: 2.630800247192383 (2.552709276571213)
| > loss_disc_real_0: 0.2224411815404892 (0.16167302776432632)
| > loss_disc_real_1: 0.237913116812706 (0.21122909398198877)
| > loss_disc_real_2: 0.22412468492984772 (0.22822815292286422)
| > loss_disc_real_3: 0.22555457055568695 (0.22776249032350457)
| > loss_disc_real_4: 0.2284373790025711 (0.23878155264464565)
| > loss_disc_real_5: 0.2330317348241806 (0.22671713834663607)
| > loss_0: 2.630800247192383 (2.552709276571213)
| > grad_norm_0: tensor(33.3042, device='cuda:0') (tensor(21.6334, device='cuda:0'))
| > loss_gen: 2.4192843437194824 (2.280580094775313)
| > loss_kl: 1.606482744216919 (1.5684294805586714)
| > loss_feat: 7.373716831207275 (7.158773380255551)
| > loss_mel: 16.529132843017578 (15.594487346193326)
| > loss_duration: 1.4332690238952637 (1.3697059274469532)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 29.361886978149414 (27.97197634618987)
| > grad_norm_1: tensor(241.8498, device='cuda:0') (tensor(262.0580, device='cuda:0'))
| > current_lr_0: 0.00019905219358328844
| > current_lr_1: 0.00019905219358328844
| > step_time: 0.5831 (0.5543233178696544)
| > loader_time: 0.0072 (0.005871207459167864)
--> TIME: 2025-05-14 15:27:37 -- STEP: 259/630 -- GLOBAL_STEP: 901200
| > loss_disc: 2.6660959720611572 (2.562451159171617)
| > loss_disc_real_0: 0.10660277307033539 (0.16574852965398176)
| > loss_disc_real_1: 0.22888629138469696 (0.21019021956731915)
| > loss_disc_real_2: 0.2580595314502716 (0.22830411291260516)
| > loss_disc_real_3: 0.19226504862308502 (0.2281390586184719)
| > loss_disc_real_4: 0.2109064757823944 (0.23924634499209269)
| > loss_disc_real_5: 0.24312889575958252 (0.22967197432481185)
| > loss_0: 2.6660959720611572 (2.562451159171617)
| > grad_norm_0: tensor(26.9449, device='cuda:0') (tensor(20.4176, device='cuda:0'))
| > loss_gen: 2.173109769821167 (2.2628002866354677)
| > loss_kl: 1.4273626804351807 (1.591087410348723)
| > loss_feat: 7.348842620849609 (7.094260269150311)
| > loss_mel: 15.373960494995117 (15.60409335280017)
| > loss_duration: 1.4625492095947266 (1.380386243915926)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.785823822021484 (27.932627659506778)
| > grad_norm_1: tensor(183.4960, device='cuda:0') (tensor(243.6676, device='cuda:0'))
| > current_lr_0: 0.00019905219358328844
| > current_lr_1: 0.00019905219358328844
| > step_time: 0.6345 (0.578820347325682)
| > loader_time: 0.0072 (0.00639091495381359)
--> TIME: 2025-05-14 15:28:44 -- STEP: 359/630 -- GLOBAL_STEP: 901300
| > loss_disc: 2.7308297157287598 (2.5677384705928734)
| > loss_disc_real_0: 0.11880795657634735 (0.1669332120868489)
| > loss_disc_real_1: 0.24341794848442078 (0.21126828263812078)
| > loss_disc_real_2: 0.25701704621315 (0.22831243172827537)
| > loss_disc_real_3: 0.2492767721414566 (0.22861604753643025)
| > loss_disc_real_4: 0.23797404766082764 (0.23851159659102766)
| > loss_disc_real_5: 0.22093914449214935 (0.22893793565483148)
| > loss_0: 2.7308297157287598 (2.5677384705928734)
| > grad_norm_0: tensor(27.7913, device='cuda:0') (tensor(21.5404, device='cuda:0'))
| > loss_gen: 2.0527164936065674 (2.250607088415733)
| > loss_kl: 1.6926060914993286 (1.5994834441660506)
| > loss_feat: 5.908674716949463 (7.001153781221439)
| > loss_mel: 14.255027770996094 (15.557488611481649)
| > loss_duration: 1.476501703262329 (1.4024218569891034)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.385526657104492 (27.811154862300267)
| > grad_norm_1: tensor(70.3934, device='cuda:0') (tensor(249.4892, device='cuda:0'))
| > current_lr_0: 0.00019905219358328844
| > current_lr_1: 0.00019905219358328844
| > step_time: 0.6786 (0.6012179426496076)
| > loader_time: 0.0098 (0.006911229290337948)
--> TIME: 2025-05-14 15:29:56 -- STEP: 459/630 -- GLOBAL_STEP: 901400
| > loss_disc: 2.489041566848755 (2.571967736308615)
| > loss_disc_real_0: 0.17726770043373108 (0.1669735514552764)
| > loss_disc_real_1: 0.25628718733787537 (0.2110465292804641)
| > loss_disc_real_2: 0.2149880826473236 (0.22872659781529753)
| > loss_disc_real_3: 0.21658703684806824 (0.2290692858576515)
| > loss_disc_real_4: 0.22010236978530884 (0.2386698271259503)
| > loss_disc_real_5: 0.2067842185497284 (0.2305104651352419)
| > loss_0: 2.489041566848755 (2.571967736308615)
| > grad_norm_0: tensor(9.2610, device='cuda:0') (tensor(20.7129, device='cuda:0'))
| > loss_gen: 2.148062229156494 (2.2425030228359226)
| > loss_kl: 1.6264936923980713 (1.5982794340919046)
| > loss_feat: 6.504459857940674 (6.939959463730358)
| > loss_mel: 15.775476455688477 (15.532170112875813)
| > loss_duration: 1.4224169254302979 (1.4061815595834604)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.47690773010254 (27.71909363441218)
| > grad_norm_1: tensor(75.6852, device='cuda:0') (tensor(236.0115, device='cuda:0'))
| > current_lr_0: 0.00019905219358328844
| > current_lr_1: 0.00019905219358328844
| > step_time: 0.7212 (0.6233238457075128)
| > loader_time: 0.0094 (0.007450398796264382)
--> TIME: 2025-05-14 15:31:16 -- STEP: 559/630 -- GLOBAL_STEP: 901500
| > loss_disc: 2.5825376510620117 (2.571430839238314)
| > loss_disc_real_0: 0.12629365921020508 (0.16759257205163847)
| > loss_disc_real_1: 0.22038231790065765 (0.21101919968141)
| > loss_disc_real_2: 0.2443368285894394 (0.22863948646406365)
| > loss_disc_real_3: 0.20819252729415894 (0.22915122006255106)
| > loss_disc_real_4: 0.20681782066822052 (0.2382361055593371)
| > loss_disc_real_5: 0.25949719548225403 (0.23023743351691525)
| > loss_0: 2.5825376510620117 (2.571430839238314)
| > grad_norm_0: tensor(28.3229, device='cuda:0') (tensor(21.2850, device='cuda:0'))
| > loss_gen: 2.296659231185913 (2.242081706553748)
| > loss_kl: 1.7460287809371948 (1.6050159656084502)
| > loss_feat: 7.435070514678955 (6.904407430420196)
| > loss_mel: 15.702213287353516 (15.509351360136794)
| > loss_duration: 1.484721064567566 (1.4167715793005682)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.664691925048828 (27.677628061639176)
| > grad_norm_1: tensor(160.5189, device='cuda:0') (tensor(243.9824, device='cuda:0'))
| > current_lr_0: 0.00019905219358328844
| > current_lr_1: 0.00019905219358328844
| > step_time: 0.794 (0.6527088950912936)
| > loader_time: 0.0115 (0.007996841918590458)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_901500.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005169232686360677 (+0.00013413031895955375)
| > avg_loss_disc: 2.691781461238861 (+0.06174645821253444)
| > avg_loss_disc_real_0: 0.1740079695979754 (+0.027219918866952242)
| > avg_loss_disc_real_1: 0.1723965754111608 (-0.09961544349789617)
| > avg_loss_disc_real_2: 0.20904319485028586 (-0.041793112953503936)
| > avg_loss_disc_real_3: 0.2388224055369695 (-0.036335114389657946)
| > avg_loss_disc_real_4: 0.2677847209076087 (-0.01907950391372043)
| > avg_loss_disc_real_5: 0.249740240474542 (+0.02741305281718573)
| > avg_loss_0: 2.691781461238861 (+0.06174645821253444)
| > avg_loss_gen: 1.9844868779182434 (-0.19407484928766872)
| > avg_loss_kl: 1.7944643795490265 (+0.1520289878050487)
| > avg_loss_feat: 6.706584095954895 (+0.6291431585947675)
| > avg_loss_mel: 15.803575913111368 (+0.46014404296875)
| > avg_loss_duration: 1.5321936905384064 (-0.0036504268646240234)
| > avg_loss_1: 27.82130511601766 (+1.0435908635457345)
> EPOCH: 39/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:32:39)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:32:56 -- STEP: 29/630 -- GLOBAL_STEP: 901600
| > loss_disc: 2.65968656539917 (2.557833063191381)
| > loss_disc_real_0: 0.15838466584682465 (0.16295302736348125)
| > loss_disc_real_1: 0.1885339319705963 (0.21177721537392716)
| > loss_disc_real_2: 0.2600259780883789 (0.23214105182680592)
| > loss_disc_real_3: 0.27867716550827026 (0.23483930117097393)
| > loss_disc_real_4: 0.28509074449539185 (0.23973936613263755)
| > loss_disc_real_5: 0.2743983566761017 (0.21997172231304235)
| > loss_0: 2.65968656539917 (2.557833063191381)
| > grad_norm_0: tensor(11.6361, device='cuda:0') (tensor(25.1310, device='cuda:0'))
| > loss_gen: 2.059068202972412 (2.3334721203508058)
| > loss_kl: 1.5531129837036133 (1.5625938793708538)
| > loss_feat: 6.134647846221924 (7.296306626550082)
| > loss_mel: 16.679706573486328 (15.915826106893606)
| > loss_duration: 1.3970913887023926 (1.4208000158441478)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.823627471923828 (28.528998868218785)
| > grad_norm_1: tensor(127.8953, device='cuda:0') (tensor(297.8583, device='cuda:0'))
| > current_lr_0: 0.0001990273120590905
| > current_lr_1: 0.0001990273120590905
| > step_time: 0.5366 (0.5202848746858796)
| > loader_time: 0.0057 (0.0048854104403791765)
--> TIME: 2025-05-14 15:33:51 -- STEP: 129/630 -- GLOBAL_STEP: 901700
| > loss_disc: 2.6312062740325928 (2.579284666120545)
| > loss_disc_real_0: 0.249118372797966 (0.1632089653564978)
| > loss_disc_real_1: 0.18683107197284698 (0.21085087504497793)
| > loss_disc_real_2: 0.16182762384414673 (0.2287862059450889)
| > loss_disc_real_3: 0.20109771192073822 (0.2278996927793636)
| > loss_disc_real_4: 0.20804037153720856 (0.24064018028651096)
| > loss_disc_real_5: 0.2171962559223175 (0.2342073525222697)
| > loss_0: 2.6312062740325928 (2.579284666120545)
| > grad_norm_0: tensor(8.6556, device='cuda:0') (tensor(19.2823, device='cuda:0'))
| > loss_gen: 2.046862840652466 (2.227453418480333)
| > loss_kl: 1.6454100608825684 (1.5899356002955474)
| > loss_feat: 6.775015354156494 (6.924052024072455)
| > loss_mel: 15.726806640625 (15.54492557141208)
| > loss_duration: 1.497175931930542 (1.4040731625963552)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.69127082824707 (27.690439756526505)
| > grad_norm_1: tensor(39.4104, device='cuda:0') (tensor(209.0662, device='cuda:0'))
| > current_lr_0: 0.0001990273120590905
| > current_lr_1: 0.0001990273120590905
| > step_time: 0.5448 (0.541091185207515)
| > loader_time: 0.0063 (0.005592050478439923)
--> TIME: 2025-05-14 15:34:53 -- STEP: 229/630 -- GLOBAL_STEP: 901800
| > loss_disc: 2.3896007537841797 (2.5890675299032297)
| > loss_disc_real_0: 0.10780535638332367 (0.16510010722162421)
| > loss_disc_real_1: 0.19069182872772217 (0.2118321979280122)
| > loss_disc_real_2: 0.21608535945415497 (0.22998757256951394)
| > loss_disc_real_3: 0.194834366440773 (0.22841440746357347)
| > loss_disc_real_4: 0.23438626527786255 (0.24032968406333674)
| > loss_disc_real_5: 0.205485001206398 (0.23691515523663775)
| > loss_0: 2.3896007537841797 (2.5890675299032297)
| > grad_norm_0: tensor(12.5768, device='cuda:0') (tensor(15.6808, device='cuda:0'))
| > loss_gen: 2.2871341705322266 (2.2138389525975715)
| > loss_kl: 1.6684597730636597 (1.6174279472192823)
| > loss_feat: 6.800566673278809 (6.884741114737165)
| > loss_mel: 16.09637451171875 (15.56256433345345)
| > loss_duration: 1.4635398387908936 (1.3749243005394416)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.31607437133789 (27.653496529858185)
| > grad_norm_1: tensor(227.4705, device='cuda:0') (tensor(158.3713, device='cuda:0'))
| > current_lr_0: 0.0001990273120590905
| > current_lr_1: 0.0001990273120590905
| > step_time: 0.6229 (0.5673333245073341)
| > loader_time: 0.0081 (0.00615673190121047)
--> TIME: 2025-05-14 15:35:59 -- STEP: 329/630 -- GLOBAL_STEP: 901900
| > loss_disc: 2.602339744567871 (2.5801597344476765)
| > loss_disc_real_0: 0.24479296803474426 (0.1663933987630174)
| > loss_disc_real_1: 0.1633639633655548 (0.21182623351598576)
| > loss_disc_real_2: 0.2527526617050171 (0.22929998340034194)
| > loss_disc_real_3: 0.22772975265979767 (0.2286196295794745)
| > loss_disc_real_4: 0.21123595535755157 (0.23897552458529778)
| > loss_disc_real_5: 0.21010452508926392 (0.23224525633735135)
| > loss_0: 2.602339744567871 (2.5801597344476765)
| > grad_norm_0: tensor(9.7127, device='cuda:0') (tensor(18.1872, device='cuda:0'))
| > loss_gen: 2.1300854682922363 (2.2365010382556627)
| > loss_kl: 1.7449519634246826 (1.6105745777170708)
| > loss_feat: 6.223038673400879 (6.903011279990243)
| > loss_mel: 15.546710014343262 (15.56813531661106)
| > loss_duration: 1.4638948440551758 (1.3996372523641152)
| > amp_scaler: 256.0 (261.4468085106383)
| > loss_1: 27.108680725097656 (27.71785935514966)
| > grad_norm_1: tensor(171.5905, device='cuda:0') (tensor(195.2043, device='cuda:0'))
| > current_lr_0: 0.0001990273120590905
| > current_lr_1: 0.0001990273120590905
| > step_time: 0.6745 (0.5918295861739877)
| > loader_time: 0.0083 (0.006747353040700988)
--> TIME: 2025-05-14 15:37:11 -- STEP: 429/630 -- GLOBAL_STEP: 902000
| > loss_disc: 2.442568778991699 (2.5768188985633396)
| > loss_disc_real_0: 0.10277460515499115 (0.16618490985015047)
| > loss_disc_real_1: 0.21314164996147156 (0.21087901474851545)
| > loss_disc_real_2: 0.1839693933725357 (0.2282211761444043)
| > loss_disc_real_3: 0.2352340817451477 (0.22836063506997825)
| > loss_disc_real_4: 0.2512665390968323 (0.23953003229655864)
| > loss_disc_real_5: 0.2563685476779938 (0.23197939613343396)
| > loss_0: 2.442568778991699 (2.5768188985633396)
| > grad_norm_0: tensor(9.6887, device='cuda:0') (tensor(18.6896, device='cuda:0'))
| > loss_gen: 2.369499921798706 (2.235538604098323)
| > loss_kl: 1.7807064056396484 (1.6171056657404332)
| > loss_feat: 5.751713752746582 (6.861714134127386)
| > loss_mel: 16.249595642089844 (15.538407790355194)
| > loss_duration: 1.4463553428649902 (1.402738608958282)
| > amp_scaler: 256.0 (260.1771561771564)
| > loss_1: 27.597871780395508 (27.65550472464039)
| > grad_norm_1: tensor(91.4515, device='cuda:0') (tensor(205.6107, device='cuda:0'))
| > current_lr_0: 0.0001990273120590905
| > current_lr_1: 0.0001990273120590905
| > step_time: 0.7489 (0.6175726738287297)
| > loader_time: 0.0102 (0.0072881097282285175)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_902000.pth
--> TIME: 2025-05-14 15:38:33 -- STEP: 529/630 -- GLOBAL_STEP: 902100
| > loss_disc: 2.5654704570770264 (2.575031315221227)
| > loss_disc_real_0: 0.17790673673152924 (0.16631544788415575)
| > loss_disc_real_1: 0.21367619931697845 (0.21111345186914068)
| > loss_disc_real_2: 0.27226904034614563 (0.22763373960506714)
| > loss_disc_real_3: 0.22006037831306458 (0.22799203695556844)
| > loss_disc_real_4: 0.2567797899246216 (0.23945117948862016)
| > loss_disc_real_5: 0.2184712290763855 (0.23215902229112578)
| > loss_0: 2.5654704570770264 (2.575031315221227)
| > grad_norm_0: tensor(14.1710, device='cuda:0') (tensor(17.7869, device='cuda:0'))
| > loss_gen: 2.3493826389312744 (2.2289710705131585)
| > loss_kl: 1.662021279335022 (1.6145441678611452)
| > loss_feat: 6.925590515136719 (6.801367597453759)
| > loss_mel: 15.900267601013184 (15.5330360697438)
| > loss_duration: 1.4476351737976074 (1.4135681812163787)
| > amp_scaler: 256.0 (259.3875236294896)
| > loss_1: 28.28489875793457 (27.5914870372116)
| > grad_norm_1: tensor(280.7163, device='cuda:0') (tensor(193.5071, device='cuda:0'))
| > current_lr_0: 0.0001990273120590905
| > current_lr_1: 0.0001990273120590905
| > step_time: 0.8178 (0.6476738367278995)
| > loader_time: 0.0119 (0.007828155852896505)
--> TIME: 2025-05-14 15:40:11 -- STEP: 629/630 -- GLOBAL_STEP: 902200
| > loss_disc: 2.525696277618408 (2.573241720897024)
| > loss_disc_real_0: 0.17190925776958466 (0.1667480887948803)
| > loss_disc_real_1: 0.1580124944448471 (0.21085168075390945)
| > loss_disc_real_2: 0.23358018696308136 (0.22765001105011362)
| > loss_disc_real_3: 0.17649619281291962 (0.2279695821822353)
| > loss_disc_real_4: 0.23670455813407898 (0.23919462427994406)
| > loss_disc_real_5: 0.17978248000144958 (0.23111574105409066)
| > loss_0: 2.525696277618408 (2.573241720897024)
| > grad_norm_0: tensor(7.2923, device='cuda:0') (tensor(18.5342, device='cuda:0'))
| > loss_gen: 2.1674067974090576 (2.231555039249656)
| > loss_kl: 1.610292911529541 (1.61613995699132)
| > loss_feat: 7.303952217102051 (6.786861691831213)
| > loss_mel: 15.466412544250488 (15.523874144864955)
| > loss_duration: 1.4949822425842285 (1.4225856545240576)
| > amp_scaler: 256.0 (258.84896661367253)
| > loss_1: 28.043045043945312 (27.581016413168612)
| > grad_norm_1: tensor(68.6595, device='cuda:0') (tensor(202.6199, device='cuda:0'))
| > current_lr_0: 0.0001990273120590905
| > current_lr_1: 0.0001990273120590905
| > step_time: 1.4506 (0.698077900042026)
| > loader_time: 0.0161 (0.008535739537831903)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005314846833546956 (+0.0001456141471862793)
| > avg_loss_disc: 2.6674149433771768 (-0.02436651786168431)
| > avg_loss_disc_real_0: 0.22408062716325125 (+0.05007265756527585)
| > avg_loss_disc_real_1: 0.1946618097523848 (+0.022265234341224016)
| > avg_loss_disc_real_2: 0.20243489121397337 (-0.006608303636312485)
| > avg_loss_disc_real_3: 0.24231225376327833 (+0.0034898482263088226)
| > avg_loss_disc_real_4: 0.2734393775463104 (+0.005654656638701738)
| > avg_loss_disc_real_5: 0.2916317308942477 (+0.04189149041970572)
| > avg_loss_0: 2.6674149433771768 (-0.02436651786168431)
| > avg_loss_gen: 2.137625058492025 (+0.15313818057378148)
| > avg_loss_kl: 1.7241822183132172 (-0.07028216123580933)
| > avg_loss_feat: 5.997672438621521 (-0.708911657333374)
| > avg_loss_mel: 14.938910802205404 (-0.864665110905964)
| > avg_loss_duration: 1.533922831217448 (+0.0017291406790416186)
| > avg_loss_1: 26.33231274286906 (-1.488992373148598)
> BEST MODEL : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/best_model_902201.pth
> EPOCH: 40/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:40:22)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:41:18 -- STEP: 99/630 -- GLOBAL_STEP: 902300
| > loss_disc: 2.6925249099731445 (2.5671665066420437)
| > loss_disc_real_0: 0.1266770362854004 (0.16709672275817758)
| > loss_disc_real_1: 0.17505598068237305 (0.2097400642103619)
| > loss_disc_real_2: 0.30704817175865173 (0.22713017448632403)
| > loss_disc_real_3: 0.2455466240644455 (0.22788873525580974)
| > loss_disc_real_4: 0.28374752402305603 (0.2393656379044658)
| > loss_disc_real_5: 0.24058698117733002 (0.23049323968213015)
| > loss_0: 2.6925249099731445 (2.5671665066420437)
| > grad_norm_0: tensor(28.3181, device='cuda:0') (tensor(22.8826, device='cuda:0'))
| > loss_gen: 2.3403091430664062 (2.2565862169169426)
| > loss_kl: 1.7348401546478271 (1.5736577113469439)
| > loss_feat: 6.220844268798828 (7.076242832222369)
| > loss_mel: 15.59705638885498 (15.589015084083634)
| > loss_duration: 1.4798212051391602 (1.4307521581649778)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.37287139892578 (27.926253906404128)
| > grad_norm_1: tensor(477.0338, device='cuda:0') (tensor(284.5106, device='cuda:0'))
| > current_lr_0: 0.00019900243364508313
| > current_lr_1: 0.00019900243364508313
| > step_time: 0.5378 (0.5422258641984729)
| > loader_time: 0.0055 (0.005357034278638437)
--> TIME: 2025-05-14 15:42:18 -- STEP: 199/630 -- GLOBAL_STEP: 902400
| > loss_disc: 2.4839465618133545 (2.5656945549663)
| > loss_disc_real_0: 0.1440674364566803 (0.16667067135997765)
| > loss_disc_real_1: 0.20654456317424774 (0.21086499514292234)
| > loss_disc_real_2: 0.216953843832016 (0.22700319143395928)
| > loss_disc_real_3: 0.19349849224090576 (0.2273066849564787)
| > loss_disc_real_4: 0.20663736760616302 (0.23846133030838704)
| > loss_disc_real_5: 0.2502341866493225 (0.23237912993335244)
| > loss_0: 2.4839465618133545 (2.5656945549663)
| > grad_norm_0: tensor(20.8831, device='cuda:0') (tensor(22.9242, device='cuda:0'))
| > loss_gen: 2.1718127727508545 (2.241563151829209)
| > loss_kl: 1.5134583711624146 (1.5843424815029354)
| > loss_feat: 6.0543532371521 (6.941435689303144)
| > loss_mel: 15.213037490844727 (15.455782406294166)
| > loss_duration: 1.4400711059570312 (1.3855574610245278)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.392732620239258 (27.608681175576972)
| > grad_norm_1: tensor(140.9548, device='cuda:0') (tensor(270.8176, device='cuda:0'))
| > current_lr_0: 0.00019900243364508313
| > current_lr_1: 0.00019900243364508313
| > step_time: 0.5918 (0.566705253256026)
| > loader_time: 0.0071 (0.005885215260874688)
--> TIME: 2025-05-14 15:43:23 -- STEP: 299/630 -- GLOBAL_STEP: 902500
| > loss_disc: 2.581153392791748 (2.5661901319306035)
| > loss_disc_real_0: 0.19264672696590424 (0.16635787437193375)
| > loss_disc_real_1: 0.20049728453159332 (0.2101079870924902)
| > loss_disc_real_2: 0.239077627658844 (0.2266111454138389)
| > loss_disc_real_3: 0.24475567042827606 (0.22806340181907284)
| > loss_disc_real_4: 0.2584344446659088 (0.23822130497084015)
| > loss_disc_real_5: 0.2619909942150116 (0.23316980390046352)
| > loss_0: 2.581153392791748 (2.5661901319306035)
| > grad_norm_0: tensor(16.2291, device='cuda:0') (tensor(21.5668, device='cuda:0'))
| > loss_gen: 2.2741827964782715 (2.2368391728321457)
| > loss_kl: 1.799924373626709 (1.5934513356773352)
| > loss_feat: 6.604722499847412 (6.873319721540878)
| > loss_mel: 16.04664421081543 (15.438821228052861)
| > loss_duration: 1.425764799118042 (1.3892183810173466)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.15123748779297 (27.531649822375442)
| > grad_norm_1: tensor(133.7475, device='cuda:0') (tensor(255.1164, device='cuda:0'))
| > current_lr_0: 0.00019900243364508313
| > current_lr_1: 0.00019900243364508313
| > step_time: 0.6661 (0.5874982175221014)
| > loader_time: 0.0089 (0.006428324657937757)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_902500.pth
--> TIME: 2025-05-14 15:44:37 -- STEP: 399/630 -- GLOBAL_STEP: 902600
| > loss_disc: 2.519981622695923 (2.5694696807622317)
| > loss_disc_real_0: 0.16669434309005737 (0.1665311936373101)
| > loss_disc_real_1: 0.22273629903793335 (0.21109293649593994)
| > loss_disc_real_2: 0.254780650138855 (0.22680262156895228)
| > loss_disc_real_3: 0.22777016460895538 (0.22808851469728283)
| > loss_disc_real_4: 0.24084194004535675 (0.23849605315161826)
| > loss_disc_real_5: 0.21860654652118683 (0.23303048716003733)
| > loss_0: 2.519981622695923 (2.5694696807622317)
| > grad_norm_0: tensor(25.2984, device='cuda:0') (tensor(20.7182, device='cuda:0'))
| > loss_gen: 2.434544086456299 (2.2321990578993227)
| > loss_kl: 1.4517322778701782 (1.600519129506926)
| > loss_feat: 7.358145713806152 (6.8533074873730655)
| > loss_mel: 14.905921936035156 (15.444631012460045)
| > loss_duration: 1.4309886693954468 (1.3947818476454656)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.58133316040039 (27.525438504709033)
| > grad_norm_1: tensor(259.4239, device='cuda:0') (tensor(241.6796, device='cuda:0'))
| > current_lr_0: 0.00019900243364508313
| > current_lr_1: 0.00019900243364508313
| > step_time: 0.7207 (0.6151943481655645)
| > loader_time: 0.0094 (0.007012178425800832)
--> TIME: 2025-05-14 15:45:51 -- STEP: 499/630 -- GLOBAL_STEP: 902700
| > loss_disc: 2.641077995300293 (2.5700220865811523)
| > loss_disc_real_0: 0.22767364978790283 (0.16736823450288693)
| > loss_disc_real_1: 0.21531155705451965 (0.21116135636706632)
| > loss_disc_real_2: 0.1977790892124176 (0.2275213801669692)
| > loss_disc_real_3: 0.21996767818927765 (0.22876917921708437)
| > loss_disc_real_4: 0.25727322697639465 (0.23821387698272903)
| > loss_disc_real_5: 0.23201607167720795 (0.2307154424115269)
| > loss_0: 2.641077995300293 (2.5700220865811523)
| > grad_norm_0: tensor(32.7710, device='cuda:0') (tensor(22.0048, device='cuda:0'))
| > loss_gen: 2.066633701324463 (2.2375705361605176)
| > loss_kl: 1.6734235286712646 (1.6053903884065892)
| > loss_feat: 6.6646013259887695 (6.845708071110483)
| > loss_mel: 15.561558723449707 (15.431338239528372)
| > loss_duration: 1.4889345169067383 (1.4083686130558082)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.455150604248047 (27.528375812905104)
| > grad_norm_1: tensor(292.0414, device='cuda:0') (tensor(255.8800, device='cuda:0'))
| > current_lr_0: 0.00019900243364508313
| > current_lr_1: 0.00019900243364508313
| > step_time: 0.7367 (0.638222318851876)
| > loader_time: 0.0099 (0.007595330775381331)
--> TIME: 2025-05-14 15:47:13 -- STEP: 599/630 -- GLOBAL_STEP: 902800
| > loss_disc: 2.5235795974731445 (2.569399858356915)
| > loss_disc_real_0: 0.11918209493160248 (0.16669060554796944)
| > loss_disc_real_1: 0.23264454305171967 (0.21116446330521457)
| > loss_disc_real_2: 0.25229835510253906 (0.22725306894126435)
| > loss_disc_real_3: 0.2131033092737198 (0.22879140106385856)
| > loss_disc_real_4: 0.2333032637834549 (0.23842884418562377)
| > loss_disc_real_5: 0.19877669215202332 (0.23062133949517408)
| > loss_0: 2.5235795974731445 (2.569399858356915)
| > grad_norm_0: tensor(9.7717, device='cuda:0') (tensor(22.2539, device='cuda:0'))
| > loss_gen: 2.2589943408966064 (2.2351091234433236)
| > loss_kl: 1.6096079349517822 (1.611146857424052)
| > loss_feat: 6.577352523803711 (6.814170424249617)
| > loss_mel: 15.846778869628906 (15.430636057272578)
| > loss_duration: 1.4886131286621094 (1.4174363764379179)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.781347274780273 (27.50849883982255)
| > grad_norm_1: tensor(164.6762, device='cuda:0') (tensor(256.4719, device='cuda:0'))
| > current_lr_0: 0.00019900243364508313
| > current_lr_1: 0.00019900243364508313
| > step_time: 0.9524 (0.6661569562698644)
| > loader_time: 0.0117 (0.008221150638663112)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004973014195760091 (-0.00034183263778686523)
| > avg_loss_disc: 2.6032769083976746 (-0.06413803497950221)
| > avg_loss_disc_real_0: 0.12108981423079967 (-0.10299081293245158)
| > avg_loss_disc_real_1: 0.26171865810950595 (+0.06705684835712114)
| > avg_loss_disc_real_2: 0.17625130588809648 (-0.02618358532587689)
| > avg_loss_disc_real_3: 0.20003419617811838 (-0.042278057585159956)
| > avg_loss_disc_real_4: 0.22239834318558374 (-0.051041034360726684)
| > avg_loss_disc_real_5: 0.22155125314990678 (-0.07008047774434092)
| > avg_loss_0: 2.6032769083976746 (-0.06413803497950221)
| > avg_loss_gen: 1.976204921801885 (-0.16142013669014)
| > avg_loss_kl: 1.761435478925705 (+0.03725326061248779)
| > avg_loss_feat: 7.010879635810852 (+1.013207197189331)
| > avg_loss_mel: 15.787194013595581 (+0.8482832113901768)
| > avg_loss_duration: 1.5290786226590474 (-0.00484420855840062)
| > avg_loss_1: 28.06479295094808 (+1.7324802080790178)
> EPOCH: 41/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:47:57)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:48:35 -- STEP: 69/630 -- GLOBAL_STEP: 902900
| > loss_disc: 2.5200247764587402 (2.56519821761311)
| > loss_disc_real_0: 0.1855366826057434 (0.1599322389001432)
| > loss_disc_real_1: 0.27245858311653137 (0.2158979570520097)
| > loss_disc_real_2: 0.21974126994609833 (0.2313169312217961)
| > loss_disc_real_3: 0.1902202069759369 (0.22864893964235333)
| > loss_disc_real_4: 0.22888587415218353 (0.24046348013739655)
| > loss_disc_real_5: 0.2206817865371704 (0.23420234650805377)
| > loss_0: 2.5200247764587402 (2.56519821761311)
| > grad_norm_0: tensor(12.5655, device='cuda:0') (tensor(17.2281, device='cuda:0'))
| > loss_gen: 2.168630599975586 (2.257650869480077)
| > loss_kl: 1.3471205234527588 (1.5784720009651736)
| > loss_feat: 6.669039249420166 (7.074008658312369)
| > loss_mel: 16.009897232055664 (15.664360820383266)
| > loss_duration: 1.4483076333999634 (1.426961053972659)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.642995834350586 (28.00145353787187)
| > grad_norm_1: tensor(428.1897, device='cuda:0') (tensor(199.6729, device='cuda:0'))
| > current_lr_0: 0.0001989775583408775
| > current_lr_1: 0.0001989775583408775
| > step_time: 0.5524 (0.5305589627528536)
| > loader_time: 0.0056 (0.005276279173035553)
--> TIME: 2025-05-14 15:49:33 -- STEP: 169/630 -- GLOBAL_STEP: 903000
| > loss_disc: 2.557344675064087 (2.5797806463298016)
| > loss_disc_real_0: 0.2137032151222229 (0.16459719603054623)
| > loss_disc_real_1: 0.19184793531894684 (0.21364947121876937)
| > loss_disc_real_2: 0.23256394267082214 (0.22977003684410682)
| > loss_disc_real_3: 0.23505918681621552 (0.227787584066391)
| > loss_disc_real_4: 0.23932354152202606 (0.2393292445226534)
| > loss_disc_real_5: 0.22319847345352173 (0.23498768222755229)
| > loss_0: 2.557344675064087 (2.5797806463298016)
| > grad_norm_0: tensor(24.6395, device='cuda:0') (tensor(15.2714, device='cuda:0'))
| > loss_gen: 2.493558883666992 (2.224581142149028)
| > loss_kl: 1.5724493265151978 (1.6036878154122614)
| > loss_feat: 7.8270344734191895 (6.952655989742843)
| > loss_mel: 16.682628631591797 (15.613067745457034)
| > loss_duration: 1.4855912923812866 (1.3733256526247284)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 30.061262130737305 (27.767318432147686)
| > grad_norm_1: tensor(318.9959, device='cuda:0') (tensor(172.1745, device='cuda:0'))
| > current_lr_0: 0.0001989775583408775
| > current_lr_1: 0.0001989775583408775
| > step_time: 0.5848 (0.5504241638635042)
| > loader_time: 0.0065 (0.005710930513912405)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_903000.pth
--> TIME: 2025-05-14 15:50:39 -- STEP: 269/630 -- GLOBAL_STEP: 903100
| > loss_disc: 2.4726812839508057 (2.5772083745126837)
| > loss_disc_real_0: 0.15159662067890167 (0.1672869906327982)
| > loss_disc_real_1: 0.19932246208190918 (0.21256896864525893)
| > loss_disc_real_2: 0.24463237822055817 (0.22937924705695042)
| > loss_disc_real_3: 0.18835240602493286 (0.22820868523147472)
| > loss_disc_real_4: 0.2492808699607849 (0.2387535788091142)
| > loss_disc_real_5: 0.21098768711090088 (0.2329625861241472)
| > loss_0: 2.4726812839508057 (2.5772083745126837)
| > grad_norm_0: tensor(16.0480, device='cuda:0') (tensor(16.4892, device='cuda:0'))
| > loss_gen: 2.2231173515319824 (2.2262996488344258)
| > loss_kl: 1.6435692310333252 (1.6171206563821954)
| > loss_feat: 7.233229637145996 (6.919785735332389)
| > loss_mel: 15.626862525939941 (15.5764133850438)
| > loss_duration: 1.4721505641937256 (1.3814198044596109)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.198930740356445 (27.72103930051442)
| > grad_norm_1: tensor(391.8160, device='cuda:0') (tensor(191.1879, device='cuda:0'))
| > current_lr_0: 0.0001989775583408775
| > current_lr_1: 0.0001989775583408775
| > step_time: 0.6493 (0.5742539535224663)
| > loader_time: 0.0083 (0.006265307890881394)
--> TIME: 2025-05-14 15:51:47 -- STEP: 369/630 -- GLOBAL_STEP: 903200
| > loss_disc: 2.5231235027313232 (2.573667393790351)
| > loss_disc_real_0: 0.18790090084075928 (0.16652374520776728)
| > loss_disc_real_1: 0.1976436972618103 (0.21232822993745)
| > loss_disc_real_2: 0.28590574860572815 (0.22933612388323962)
| > loss_disc_real_3: 0.2329012155532837 (0.22877108824608453)
| > loss_disc_real_4: 0.2604881823062897 (0.23936251512549434)
| > loss_disc_real_5: 0.165146142244339 (0.23040310190460547)
| > loss_0: 2.5231235027313232 (2.573667393790351)
| > grad_norm_0: tensor(11.4713, device='cuda:0') (tensor(19.1918, device='cuda:0'))
| > loss_gen: 2.2085859775543213 (2.2407204523319133)
| > loss_kl: 1.4444475173950195 (1.6165199812834823)
| > loss_feat: 7.372424125671387 (6.890647354487804)
| > loss_mel: 14.871474266052246 (15.549826689205842)
| > loss_duration: 1.4344193935394287 (1.4018039751828202)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.33135223388672 (27.69951850870437)
| > grad_norm_1: tensor(245.8659, device='cuda:0') (tensor(222.4372, device='cuda:0'))
| > current_lr_0: 0.0001989775583408775
| > current_lr_1: 0.0001989775583408775
| > step_time: 0.7027 (0.6009091490975567)
| > loader_time: 0.0094 (0.0068213183705399675)
--> TIME: 2025-05-14 15:53:04 -- STEP: 469/630 -- GLOBAL_STEP: 903300
| > loss_disc: 2.6378800868988037 (2.5714984397644174)
| > loss_disc_real_0: 0.20015808939933777 (0.16635498259939374)
| > loss_disc_real_1: 0.2113986760377884 (0.21191327175351857)
| > loss_disc_real_2: 0.23903600871562958 (0.22878472418037812)
| > loss_disc_real_3: 0.23498749732971191 (0.22870685156982848)
| > loss_disc_real_4: 0.24883729219436646 (0.23916786435697632)
| > loss_disc_real_5: 0.264068067073822 (0.2296943230224825)
| > loss_0: 2.6378800868988037 (2.5714984397644174)
| > grad_norm_0: tensor(35.4780, device='cuda:0') (tensor(20.2342, device='cuda:0'))
| > loss_gen: 2.2103817462921143 (2.2382585064434553)
| > loss_kl: 1.7295888662338257 (1.6081696306464512)
| > loss_feat: 5.186499118804932 (6.857035453893991)
| > loss_mel: 15.05675220489502 (15.53592521244529)
| > loss_duration: 1.4921493530273438 (1.404802521408748)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.675371170043945 (27.644191367793944)
| > grad_norm_1: tensor(323.6645, device='cuda:0') (tensor(234.9243, device='cuda:0'))
| > current_lr_0: 0.0001989775583408775
| > current_lr_1: 0.0001989775583408775
| > step_time: 0.7825 (0.6331643854885465)
| > loader_time: 0.01 (0.007330015015754619)
--> TIME: 2025-05-14 15:54:30 -- STEP: 569/630 -- GLOBAL_STEP: 903400
| > loss_disc: 2.5151526927948 (2.573434463913285)
| > loss_disc_real_0: 0.23403996229171753 (0.16778899210722892)
| > loss_disc_real_1: 0.22521516680717468 (0.2115414866454154)
| > loss_disc_real_2: 0.2585729658603668 (0.22826368357783253)
| > loss_disc_real_3: 0.22284534573554993 (0.22872808099002542)
| > loss_disc_real_4: 0.27257663011550903 (0.23883261200309008)
| > loss_disc_real_5: 0.27294427156448364 (0.23091443163229836)
| > loss_0: 2.5151526927948 (2.573434463913285)
| > grad_norm_0: tensor(9.7746, device='cuda:0') (tensor(19.3512, device='cuda:0'))
| > loss_gen: 2.2964816093444824 (2.228387518381612)
| > loss_kl: 1.6325099468231201 (1.6091708780801564)
| > loss_feat: 6.178991794586182 (6.8067934056367525)
| > loss_mel: 15.078449249267578 (15.510200869220004)
| > loss_duration: 1.4675953388214111 (1.414921700011657)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.654027938842773 (27.56947442643042)
| > grad_norm_1: tensor(76.7391, device='cuda:0') (tensor(217.1342, device='cuda:0'))
| > current_lr_0: 0.0001989775583408775
| > current_lr_1: 0.0001989775583408775
| > step_time: 0.8966 (0.6707398049232203)
| > loader_time: 0.0109 (0.007907419506401505)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004984060923258464 (+1.1046727498372974e-05)
| > avg_loss_disc: 2.57511576016744 (-0.028161148230234634)
| > avg_loss_disc_real_0: 0.1997927539050579 (+0.07870293967425823)
| > avg_loss_disc_real_1: 0.20122268547614416 (-0.06049597263336179)
| > avg_loss_disc_real_2: 0.22824413453539213 (+0.05199282864729565)
| > avg_loss_disc_real_3: 0.23852236196398735 (+0.03848816578586897)
| > avg_loss_disc_real_4: 0.2620808780193329 (+0.039682534833749145)
| > avg_loss_disc_real_5: 0.23155219107866287 (+0.010000937928756087)
| > avg_loss_0: 2.57511576016744 (-0.028161148230234634)
| > avg_loss_gen: 2.197039624055227 (+0.2208347022533419)
| > avg_loss_kl: 1.7338032027085621 (-0.027632276217142815)
| > avg_loss_feat: 6.731028079986572 (-0.2798515558242798)
| > avg_loss_mel: 15.400558630625406 (-0.38663538297017475)
| > avg_loss_duration: 1.533058335383733 (+0.003979712724685669)
| > avg_loss_1: 27.59548807144165 (-0.46930487950642785)
> EPOCH: 42/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 15:55:42)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 15:56:04 -- STEP: 39/630 -- GLOBAL_STEP: 903500
| > loss_disc: 2.582857847213745 (2.6067650012480907)
| > loss_disc_real_0: 0.1503279060125351 (0.17129808301344895)
| > loss_disc_real_1: 0.19938522577285767 (0.21952109917616233)
| > loss_disc_real_2: 0.19778390228748322 (0.23350436374163017)
| > loss_disc_real_3: 0.20104171335697174 (0.23268273052496788)
| > loss_disc_real_4: 0.2901756465435028 (0.24496797032845327)
| > loss_disc_real_5: 0.285319983959198 (0.2352410547244243)
| > loss_0: 2.582857847213745 (2.6067650012480907)
| > grad_norm_0: tensor(20.1462, device='cuda:0') (tensor(17.5656, device='cuda:0'))
| > loss_gen: 2.098240852355957 (2.2533202660389438)
| > loss_kl: 1.6029338836669922 (1.5331727281594885)
| > loss_feat: 6.4921674728393555 (7.011642773946126)
| > loss_mel: 14.869287490844727 (15.602424474862906)
| > loss_duration: 1.4015212059020996 (1.4255998531977336)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.46415138244629 (27.826159990750828)
| > grad_norm_1: tensor(154.3740, device='cuda:0') (tensor(191.7318, device='cuda:0'))
| > current_lr_0: 0.00019895268614608487
| > current_lr_1: 0.00019895268614608487
| > step_time: 0.5319 (0.5275838313958584)
| > loader_time: 0.0051 (0.0051560524182441905)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_903500.pth
--> TIME: 2025-05-14 15:57:03 -- STEP: 139/630 -- GLOBAL_STEP: 903600
| > loss_disc: 2.5594019889831543 (2.5677693713483194)
| > loss_disc_real_0: 0.16611018776893616 (0.16700669844373525)
| > loss_disc_real_1: 0.21486802399158478 (0.2128817342060933)
| > loss_disc_real_2: 0.2319435328245163 (0.22950299952527603)
| > loss_disc_real_3: 0.2847233712673187 (0.22947685817162766)
| > loss_disc_real_4: 0.2801338732242584 (0.23882798314523354)
| > loss_disc_real_5: 0.2732917070388794 (0.22733134208180064)
| > loss_0: 2.5594019889831543 (2.5677693713483194)
| > grad_norm_0: tensor(34.2111, device='cuda:0') (tensor(22.3641, device='cuda:0'))
| > loss_gen: 2.345066547393799 (2.2524068973047275)
| > loss_kl: 1.657960057258606 (1.541626047316215)
| > loss_feat: 6.460734844207764 (6.937390354897478)
| > loss_mel: 15.278526306152344 (15.468456590775963)
| > loss_duration: 1.4560067653656006 (1.403710726353762)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.198293685913086 (27.60359068397138)
| > grad_norm_1: tensor(481.7257, device='cuda:0') (tensor(254.2543, device='cuda:0'))
| > current_lr_0: 0.00019895268614608487
| > current_lr_1: 0.00019895268614608487
| > step_time: 0.5566 (0.5441431656158222)
| > loader_time: 0.0064 (0.0056378669875988855)
--> TIME: 2025-05-14 15:58:04 -- STEP: 239/630 -- GLOBAL_STEP: 903700
| > loss_disc: 2.5803616046905518 (2.5698930538847864)
| > loss_disc_real_0: 0.1774095594882965 (0.16622289479028232)
| > loss_disc_real_1: 0.23204387724399567 (0.21229951329934543)
| > loss_disc_real_2: 0.3062106966972351 (0.2291489448008677)
| > loss_disc_real_3: 0.24665957689285278 (0.22996096662148272)
| > loss_disc_real_4: 0.28061217069625854 (0.23990725797589355)
| > loss_disc_real_5: 0.18415096402168274 (0.22862121235251925)
| > loss_0: 2.5803616046905518 (2.5698930538847864)
| > grad_norm_0: tensor(8.5476, device='cuda:0') (tensor(20.0691, device='cuda:0'))
| > loss_gen: 2.3571038246154785 (2.251589986070928)
| > loss_kl: 1.5005805492401123 (1.5737941382320355)
| > loss_feat: 7.507545471191406 (6.9309773205713245)
| > loss_mel: 15.695388793945312 (15.530560337848744)
| > loss_duration: 1.4663844108581543 (1.372526074054351)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.527002334594727 (27.659447825603404)
| > grad_norm_1: tensor(202.0921, device='cuda:0') (tensor(233.6716, device='cuda:0'))
| > current_lr_0: 0.00019895268614608487
| > current_lr_1: 0.00019895268614608487
| > step_time: 0.61 (0.5678356791141138)
| > loader_time: 0.0076 (0.006156043527515364)
--> TIME: 2025-05-14 15:59:10 -- STEP: 339/630 -- GLOBAL_STEP: 903800
| > loss_disc: 2.5070667266845703 (2.5672774525870277)
| > loss_disc_real_0: 0.17254632711410522 (0.16625228062667669)
| > loss_disc_real_1: 0.2901706397533417 (0.2127457893835408)
| > loss_disc_real_2: 0.3359139561653137 (0.22937819691358413)
| > loss_disc_real_3: 0.2785979211330414 (0.2288070773392652)
| > loss_disc_real_4: 0.2207658439874649 (0.2390617354605402)
| > loss_disc_real_5: 0.2574629485607147 (0.22748864538813762)
| > loss_0: 2.5070667266845703 (2.5672774525870277)
| > grad_norm_0: tensor(19.2488, device='cuda:0') (tensor(21.7196, device='cuda:0'))
| > loss_gen: 2.473700761795044 (2.254402531986744)
| > loss_kl: 1.5182934999465942 (1.5838563763989826)
| > loss_feat: 6.5722246170043945 (6.92073572631431)
| > loss_mel: 16.07128143310547 (15.516768368296216)
| > loss_duration: 1.4316070079803467 (1.3963128254476902)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.067108154296875 (27.672075794861385)
| > grad_norm_1: tensor(83.7846, device='cuda:0') (tensor(261.3468, device='cuda:0'))
| > current_lr_0: 0.00019895268614608487
| > current_lr_1: 0.00019895268614608487
| > step_time: 0.6702 (0.5914863857899441)
| > loader_time: 0.0079 (0.0067212187786721235)
--> TIME: 2025-05-14 16:00:25 -- STEP: 439/630 -- GLOBAL_STEP: 903900
| > loss_disc: 2.4605424404144287 (2.56656049161403)
| > loss_disc_real_0: 0.14271174371242523 (0.16593058855359813)
| > loss_disc_real_1: 0.21434113383293152 (0.21201771017427054)
| > loss_disc_real_2: 0.2388712614774704 (0.2295107816373569)
| > loss_disc_real_3: 0.20031774044036865 (0.22893116102131733)
| > loss_disc_real_4: 0.2067422717809677 (0.2392215110310661)
| > loss_disc_real_5: 0.2062377631664276 (0.22758257828635886)
| > loss_0: 2.4605424404144287 (2.56656049161403)
| > grad_norm_0: tensor(9.0687, device='cuda:0') (tensor(21.3780, device='cuda:0'))
| > loss_gen: 2.2226078510284424 (2.2532052714080644)
| > loss_kl: 1.8187624216079712 (1.5889115000911627)
| > loss_feat: 7.55617618560791 (6.882006052143211)
| > loss_mel: 15.903146743774414 (15.524152047541799)
| > loss_duration: 1.487046718597412 (1.4000080180331076)
| > amp_scaler: 256.0 (257.7494305239181)
| > loss_1: 28.987741470336914 (27.64828288745229)
| > grad_norm_1: tensor(89.1126, device='cuda:0') (tensor(251.2772, device='cuda:0'))
| > current_lr_0: 0.00019895268614608487
| > current_lr_1: 0.00019895268614608487
| > step_time: 0.75 (0.623377398097705)
| > loader_time: 0.0088 (0.0072274023416645196)
--> TIME: 2025-05-14 16:01:47 -- STEP: 539/630 -- GLOBAL_STEP: 904000
| > loss_disc: 2.6033856868743896 (2.566631629869538)
| > loss_disc_real_0: 0.17893560230731964 (0.16632600175648768)
| > loss_disc_real_1: 0.1881508231163025 (0.21191236668427046)
| > loss_disc_real_2: 0.20622244477272034 (0.22919942974933669)
| > loss_disc_real_3: 0.23218098282814026 (0.22902481625606488)
| > loss_disc_real_4: 0.2087317705154419 (0.23868874577953997)
| > loss_disc_real_5: 0.2940698564052582 (0.2280412171319376)
| > loss_0: 2.6033856868743896 (2.566631629869538)
| > grad_norm_0: tensor(22.0526, device='cuda:0') (tensor(20.3573, device='cuda:0'))
| > loss_gen: 2.186368942260742 (2.245375670617056)
| > loss_kl: 1.8016494512557983 (1.5997611307478579)
| > loss_feat: 6.450847148895264 (6.839469640728273)
| > loss_mel: 16.04085922241211 (15.519054676473472)
| > loss_duration: 1.4566248655319214 (1.4110270902265645)
| > amp_scaler: 256.0 (257.4248608534324)
| > loss_1: 27.936349868774414 (27.614688218635173)
| > grad_norm_1: tensor(231.1298, device='cuda:0') (tensor(234.3524, device='cuda:0'))
| > current_lr_0: 0.00019895268614608487
| > current_lr_1: 0.00019895268614608487
| > step_time: 0.8502 (0.6562953030687095)
| > loader_time: 0.0101 (0.007788414415490432)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_904000.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004913171132405599 (-7.088979085286516e-05)
| > avg_loss_disc: 2.569809595743815 (-0.0053061644236249705)
| > avg_loss_disc_real_0: 0.1303088236600161 (-0.06948393024504182)
| > avg_loss_disc_real_1: 0.1960697521766027 (-0.005152933299541473)
| > avg_loss_disc_real_2: 0.21457659204800925 (-0.013667542487382889)
| > avg_loss_disc_real_3: 0.2085180270175139 (-0.03000433494647345)
| > avg_loss_disc_real_4: 0.25207774961988133 (-0.010003128399451555)
| > avg_loss_disc_real_5: 0.21432634194691977 (-0.017225849131743104)
| > avg_loss_0: 2.569809595743815 (-0.0053061644236249705)
| > avg_loss_gen: 2.003121087948481 (-0.1939185361067457)
| > avg_loss_kl: 1.7886241177717845 (+0.0548209150632224)
| > avg_loss_feat: 6.941549738248189 (+0.21052165826161673)
| > avg_loss_mel: 15.715647141138712 (+0.31508851051330566)
| > avg_loss_duration: 1.5370716551939647 (+0.004013319810231675)
| > avg_loss_1: 27.986013571421307 (+0.39052549997965613)
> EPOCH: 43/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 16:03:31)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 16:03:37 -- STEP: 9/630 -- GLOBAL_STEP: 904100
| > loss_disc: 2.5348687171936035 (2.5504141913519964)
| > loss_disc_real_0: 0.23577523231506348 (0.1604436660806338)
| > loss_disc_real_1: 0.20391811430454254 (0.21411415603425768)
| > loss_disc_real_2: 0.21341709792613983 (0.23463117414050633)
| > loss_disc_real_3: 0.193723663687706 (0.23541377319229972)
| > loss_disc_real_4: 0.2268066108226776 (0.22669733067353567)
| > loss_disc_real_5: 0.17516839504241943 (0.2148546708954705)
| > loss_0: 2.5348687171936035 (2.5504141913519964)
| > grad_norm_0: tensor(15.8549, device='cuda:0') (tensor(19.9779, device='cuda:0'))
| > loss_gen: 2.384507894515991 (2.3199088043636746)
| > loss_kl: 1.4373502731323242 (1.5246722830666437)
| > loss_feat: 7.312971115112305 (6.99778774049547)
| > loss_mel: 15.044208526611328 (15.191384527418348)
| > loss_duration: 1.4190843105316162 (1.4108215437995062)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.598121643066406 (27.44457499186198)
| > grad_norm_1: tensor(207.8156, device='cuda:0') (tensor(204.2181, device='cuda:0'))
| > current_lr_0: 0.0001989278170603166
| > current_lr_1: 0.0001989278170603166
| > step_time: 0.5193 (0.5196740362379286)
| > loader_time: 0.0048 (0.004793034659491645)
--> TIME: 2025-05-14 16:04:32 -- STEP: 109/630 -- GLOBAL_STEP: 904200
| > loss_disc: 2.654417037963867 (2.546115085619304)
| > loss_disc_real_0: 0.10082683712244034 (0.16086385388850075)
| > loss_disc_real_1: 0.21886718273162842 (0.21122049013955876)
| > loss_disc_real_2: 0.2640398144721985 (0.228959526080604)
| > loss_disc_real_3: 0.1893538385629654 (0.22711739818984217)
| > loss_disc_real_4: 0.1982450634241104 (0.23545778153139515)
| > loss_disc_real_5: 0.19167757034301758 (0.2254931062049822)
| > loss_0: 2.654417037963867 (2.546115085619304)
| > grad_norm_0: tensor(13.0656, device='cuda:0') (tensor(21.3263, device='cuda:0'))
| > loss_gen: 2.012105703353882 (2.274404920569254)
| > loss_kl: 1.4818464517593384 (1.5777689962212096)
| > loss_feat: 7.466907978057861 (7.078971175972475)
| > loss_mel: 16.162473678588867 (15.351379980734729)
| > loss_duration: 1.478310465812683 (1.3908600730633518)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.60164451599121 (27.67338509515885)
| > grad_norm_1: tensor(94.4746, device='cuda:0') (tensor(249.6729, device='cuda:0'))
| > current_lr_0: 0.0001989278170603166
| > current_lr_1: 0.0001989278170603166
| > step_time: 0.5442 (0.5356102077239149)
| > loader_time: 0.0067 (0.005496051333366184)
--> TIME: 2025-05-14 16:05:31 -- STEP: 209/630 -- GLOBAL_STEP: 904300
| > loss_disc: 2.5043623447418213 (2.5496665222222714)
| > loss_disc_real_0: 0.11071236431598663 (0.1617190756759289)
| > loss_disc_real_1: 0.22119593620300293 (0.20945358447481)
| > loss_disc_real_2: 0.22067515552043915 (0.22727697888059478)
| > loss_disc_real_3: 0.2193850427865982 (0.22754175625919726)
| > loss_disc_real_4: 0.2219720035791397 (0.2381802976274034)
| > loss_disc_real_5: 0.23841968178749084 (0.2310092402488421)
| > loss_0: 2.5043623447418213 (2.5496665222222714)
| > grad_norm_0: tensor(14.1418, device='cuda:0') (tensor(17.7192, device='cuda:0'))
| > loss_gen: 2.3968639373779297 (2.2598236542569388)
| > loss_kl: 1.576817512512207 (1.5973259712520398)
| > loss_feat: 7.948611736297607 (7.02373983301044)
| > loss_mel: 15.497909545898438 (15.389380208613199)
| > loss_duration: 1.4228291511535645 (1.358361058257983)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.84303092956543 (27.628630788702715)
| > grad_norm_1: tensor(202.6582, device='cuda:0') (tensor(204.7374, device='cuda:0'))
| > current_lr_0: 0.0001989278170603166
| > current_lr_1: 0.0001989278170603166
| > step_time: 0.6067 (0.5600298717261505)
| > loader_time: 0.0073 (0.006050487454428055)
--> TIME: 2025-05-14 16:06:37 -- STEP: 309/630 -- GLOBAL_STEP: 904400
| > loss_disc: 2.4390077590942383 (2.552565065402427)
| > loss_disc_real_0: 0.13202768564224243 (0.16296752514528604)
| > loss_disc_real_1: 0.1577550768852234 (0.20993157999415232)
| > loss_disc_real_2: 0.21846292912960052 (0.22831646022673177)
| > loss_disc_real_3: 0.21730831265449524 (0.22809320230121366)
| > loss_disc_real_4: 0.2661985456943512 (0.23924168500699658)
| > loss_disc_real_5: 0.24367867410182953 (0.22893060818555672)
| > loss_0: 2.4390077590942383 (2.552565065402427)
| > grad_norm_0: tensor(6.8255, device='cuda:0') (tensor(17.6608, device='cuda:0'))
| > loss_gen: 2.0936310291290283 (2.251619560818842)
| > loss_kl: 2.004573106765747 (1.5961423965719521)
| > loss_feat: 6.537230968475342 (6.9498917601255155)
| > loss_mel: 15.554462432861328 (15.411741333871984)
| > loss_duration: 1.4182724952697754 (1.389383949508173)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.608171463012695 (27.598779079597744)
| > grad_norm_1: tensor(120.0861, device='cuda:0') (tensor(204.6481, device='cuda:0'))
| > current_lr_0: 0.0001989278170603166
| > current_lr_1: 0.0001989278170603166
| > step_time: 0.6613 (0.5857880509015423)
| > loader_time: 0.0078 (0.00660680644334713)
--> TIME: 2025-05-14 16:07:49 -- STEP: 409/630 -- GLOBAL_STEP: 904500
| > loss_disc: 2.396761655807495 (2.548306991535174)
| > loss_disc_real_0: 0.1287705898284912 (0.16244566694703552)
| > loss_disc_real_1: 0.22064347565174103 (0.21023473493335887)
| > loss_disc_real_2: 0.2184584140777588 (0.2281222842214743)
| > loss_disc_real_3: 0.22705703973770142 (0.22793844211072387)
| > loss_disc_real_4: 0.23996582627296448 (0.23879606253069013)
| > loss_disc_real_5: 0.14856979250907898 (0.2273450039308928)
| > loss_0: 2.396761655807495 (2.548306991535174)
| > grad_norm_0: tensor(20.3131, device='cuda:0') (tensor(18.3582, device='cuda:0'))
| > loss_gen: 2.1926934719085693 (2.2571624703978563)
| > loss_kl: 1.766700267791748 (1.611359052669739)
| > loss_feat: 7.576368808746338 (6.935886934508904)
| > loss_mel: 15.532519340515137 (15.4223446974253)
| > loss_duration: 1.4879682064056396 (1.3949619479167719)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.556249618530273 (27.6217151865691)
| > grad_norm_1: tensor(395.2199, device='cuda:0') (tensor(212.8351, device='cuda:0'))
| > current_lr_0: 0.0001989278170603166
| > current_lr_1: 0.0001989278170603166
| > step_time: 0.7255 (0.6155998112228508)
| > loader_time: 0.0088 (0.007107291070056721)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_904500.pth
--> TIME: 2025-05-14 16:09:11 -- STEP: 509/630 -- GLOBAL_STEP: 904600
| > loss_disc: 2.4598445892333984 (2.553028757773586)
| > loss_disc_real_0: 0.08582353591918945 (0.16333359644578113)
| > loss_disc_real_1: 0.18029718101024628 (0.21044916974303768)
| > loss_disc_real_2: 0.27917060256004333 (0.2283408103733962)
| > loss_disc_real_3: 0.2246692180633545 (0.22850100602405712)
| > loss_disc_real_4: 0.24569158256053925 (0.23895562576287388)
| > loss_disc_real_5: 0.1874908059835434 (0.22740526127030666)
| > loss_0: 2.4598445892333984 (2.553028757773586)
| > grad_norm_0: tensor(8.8722, device='cuda:0') (tensor(19.0619, device='cuda:0'))
| > loss_gen: 2.1627511978149414 (2.253230866374107)
| > loss_kl: 1.788109540939331 (1.6110779070432617)
| > loss_feat: 7.106030464172363 (6.894257104232878)
| > loss_mel: 15.133905410766602 (15.41564684907205)
| > loss_duration: 1.4989898204803467 (1.40821886460767)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.68978500366211 (27.582431669553745)
| > grad_norm_1: tensor(115.8528, device='cuda:0') (tensor(222.8762, device='cuda:0'))
| > current_lr_0: 0.0001989278170603166
| > current_lr_1: 0.0001989278170603166
| > step_time: 0.8699 (0.647900321863021)
| > loader_time: 0.0096 (0.007621113115771581)
--> TIME: 2025-05-14 16:10:44 -- STEP: 609/630 -- GLOBAL_STEP: 904700
| > loss_disc: 2.7128891944885254 (2.556847007403818)
| > loss_disc_real_0: 0.14104506373405457 (0.16361759500868614)
| > loss_disc_real_1: 0.1770966351032257 (0.2104256279607518)
| > loss_disc_real_2: 0.2058178037405014 (0.22826942033172629)
| > loss_disc_real_3: 0.23162196576595306 (0.2284773195954575)
| > loss_disc_real_4: 0.2576614022254944 (0.2394300720032017)
| > loss_disc_real_5: 0.2813703417778015 (0.22903503906991093)
| > loss_0: 2.7128891944885254 (2.556847007403818)
| > grad_norm_0: tensor(17.5384, device='cuda:0') (tensor(18.4236, device='cuda:0'))
| > loss_gen: 2.046832323074341 (2.246260320611777)
| > loss_kl: 1.6446545124053955 (1.6182913404380153)
| > loss_feat: 6.518320560455322 (6.8546227962512685)
| > loss_mel: 15.419140815734863 (15.415345121487022)
| > loss_duration: 1.4781367778778076 (1.4181419518976575)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.107084274291992 (27.552661604481965)
| > grad_norm_1: tensor(94.6994, device='cuda:0') (tensor(212.8030, device='cuda:0'))
| > current_lr_0: 0.0001989278170603166
| > current_lr_1: 0.0001989278170603166
| > step_time: 0.9969 (0.6900706851032182)
| > loader_time: 0.012 (0.008214504652226891)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005380034446716309 (+0.0004668633143107099)
| > avg_loss_disc: 2.5725507934888205 (+0.0027411977450055858)
| > avg_loss_disc_real_0: 0.1982779341439406 (+0.06796911048392451)
| > avg_loss_disc_real_1: 0.19623090450962385 (+0.00016115233302116394)
| > avg_loss_disc_real_2: 0.2146401380499204 (+6.354600191116333e-05)
| > avg_loss_disc_real_3: 0.2140937882165114 (+0.0055757611989974976)
| > avg_loss_disc_real_4: 0.21641879777113596 (-0.035658951848745374)
| > avg_loss_disc_real_5: 0.1901907299955686 (-0.024135611951351166)
| > avg_loss_0: 2.5725507934888205 (+0.0027411977450055858)
| > avg_loss_gen: 2.0137995382150016 (+0.010678450266520478)
| > avg_loss_kl: 1.796721190214157 (+0.008097072442372566)
| > avg_loss_feat: 6.665181597073873 (-0.2763681411743164)
| > avg_loss_mel: 15.699600776036581 (-0.016046365102130977)
| > avg_loss_duration: 1.5311489204565685 (-0.00592273473739624)
| > avg_loss_1: 27.706451892852783 (-0.2795616785685233)
> EPOCH: 44/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 16:11:16)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 16:11:59 -- STEP: 79/630 -- GLOBAL_STEP: 904800
| > loss_disc: 2.5331156253814697 (2.5591600212869756)
| > loss_disc_real_0: 0.1967470645904541 (0.1701591957030417)
| > loss_disc_real_1: 0.22293011844158173 (0.21075735514677024)
| > loss_disc_real_2: 0.252329021692276 (0.22764260934878)
| > loss_disc_real_3: 0.21201984584331512 (0.2261337911403632)
| > loss_disc_real_4: 0.2697852551937103 (0.24026658489734312)
| > loss_disc_real_5: 0.24263142049312592 (0.2240751383802559)
| > loss_0: 2.5331156253814697 (2.5591600212869756)
| > grad_norm_0: tensor(20.2093, device='cuda:0') (tensor(27.1800, device='cuda:0'))
| > loss_gen: 2.4130215644836426 (2.284218336962447)
| > loss_kl: 1.5815097093582153 (1.5344468324999265)
| > loss_feat: 6.750211715698242 (7.099249260335029)
| > loss_mel: 15.837685585021973 (15.550791390334503)
| > loss_duration: 1.438324213027954 (1.4293341048156158)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.020751953125 (27.898039878169197)
| > grad_norm_1: tensor(66.9638, device='cuda:0') (tensor(349.3350, device='cuda:0'))
| > current_lr_0: 0.00019890295108318404
| > current_lr_1: 0.00019890295108318404
| > step_time: 0.5387 (0.5274816404415078)
| > loader_time: 0.006 (0.005229575724541386)
--> TIME: 2025-05-14 16:12:57 -- STEP: 179/630 -- GLOBAL_STEP: 904900
| > loss_disc: 2.439526081085205 (2.537034424989582)
| > loss_disc_real_0: 0.10929733514785767 (0.16330408725325618)
| > loss_disc_real_1: 0.22899112105369568 (0.20890533116609694)
| > loss_disc_real_2: 0.22828076779842377 (0.22629164733700247)
| > loss_disc_real_3: 0.21172304451465607 (0.22442809846148146)
| > loss_disc_real_4: 0.1975068300962448 (0.2376588145114856)
| > loss_disc_real_5: 0.1629936844110489 (0.22573407943355306)
| > loss_0: 2.439526081085205 (2.537034424989582)
| > grad_norm_0: tensor(12.4685, device='cuda:0') (tensor(24.9029, device='cuda:0'))
| > loss_gen: 2.1264209747314453 (2.291242633451962)
| > loss_kl: 1.446225643157959 (1.583088497875789)
| > loss_feat: 6.908904075622559 (7.091205583604355)
| > loss_mel: 15.822983741760254 (15.504043754918616)
| > loss_duration: 1.4495985507965088 (1.3787768952673376)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.754131317138672 (27.848357344472873)
| > grad_norm_1: tensor(49.7044, device='cuda:0') (tensor(319.8240, device='cuda:0'))
| > current_lr_0: 0.00019890295108318404
| > current_lr_1: 0.00019890295108318404
| > step_time: 0.5668 (0.5511844451201026)
| > loader_time: 0.0064 (0.005807511633334879)
--> TIME: 2025-05-14 16:14:00 -- STEP: 279/630 -- GLOBAL_STEP: 905000
| > loss_disc: 2.601558208465576 (2.5546933485188363)
| > loss_disc_real_0: 0.11773237586021423 (0.16510741551503486)
| > loss_disc_real_1: 0.16413827240467072 (0.21023840684190023)
| > loss_disc_real_2: 0.2201421856880188 (0.22731198867162067)
| > loss_disc_real_3: 0.22039449214935303 (0.2266089807274521)
| > loss_disc_real_4: 0.24308615922927856 (0.23894097680045712)
| > loss_disc_real_5: 0.2286044955253601 (0.22985546023828582)
| > loss_0: 2.601558208465576 (2.5546933485188363)
| > grad_norm_0: tensor(7.9083, device='cuda:0') (tensor(21.0145, device='cuda:0'))
| > loss_gen: 2.0104153156280518 (2.2609994052558795)
| > loss_kl: 1.78037691116333 (1.5976321150325108)
| > loss_feat: 6.365033149719238 (6.958724095402653)
| > loss_mel: 15.118114471435547 (15.483148403919726)
| > loss_duration: 1.4759975671768188 (1.3818838092161336)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.74993896484375 (27.682387806608684)
| > grad_norm_1: tensor(62.4265, device='cuda:0') (tensor(251.2988, device='cuda:0'))
| > current_lr_0: 0.00019890295108318404
| > current_lr_1: 0.00019890295108318404
| > step_time: 0.6356 (0.5743005352635538)
| > loader_time: 0.0086 (0.006319301530024484)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_905000.pth
--> TIME: 2025-05-14 16:15:12 -- STEP: 379/630 -- GLOBAL_STEP: 905100
| > loss_disc: 2.493732452392578 (2.5622336820436318)
| > loss_disc_real_0: 0.2745824456214905 (0.16512371963356914)
| > loss_disc_real_1: 0.16166923940181732 (0.21084913517051132)
| > loss_disc_real_2: 0.2302941232919693 (0.22880053921236526)
| > loss_disc_real_3: 0.2049994170665741 (0.22757391525447213)
| > loss_disc_real_4: 0.2383309155702591 (0.2388986243342976)
| > loss_disc_real_5: 0.20407076179981232 (0.23091374990336183)
| > loss_0: 2.493732452392578 (2.5622336820436318)
| > grad_norm_0: tensor(28.6172, device='cuda:0') (tensor(19.1646, device='cuda:0'))
| > loss_gen: 2.3210830688476562 (2.2415630785959673)
| > loss_kl: 1.608771562576294 (1.6087124523827145)
| > loss_feat: 7.340764999389648 (6.85168913612265)
| > loss_mel: 15.997674942016602 (15.447238516996277)
| > loss_duration: 1.4568095207214355 (1.401123056940165)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.72510528564453 (27.550326234117975)
| > grad_norm_1: tensor(122.3058, device='cuda:0') (tensor(221.6454, device='cuda:0'))
| > current_lr_0: 0.00019890295108318404
| > current_lr_1: 0.00019890295108318404
| > step_time: 0.6851 (0.5999369426264298)
| > loader_time: 0.0088 (0.006883921283530685)
--> TIME: 2025-05-14 16:16:26 -- STEP: 479/630 -- GLOBAL_STEP: 905200
| > loss_disc: 2.722883701324463 (2.5601760440181325)
| > loss_disc_real_0: 0.15025044977664948 (0.16557635597122483)
| > loss_disc_real_1: 0.20817196369171143 (0.21062856853506012)
| > loss_disc_real_2: 0.28055432438850403 (0.2286713368148545)
| > loss_disc_real_3: 0.25696638226509094 (0.22839444642400442)
| > loss_disc_real_4: 0.27828657627105713 (0.23919116573443244)
| > loss_disc_real_5: 0.23460093140602112 (0.22870786295181028)
| > loss_0: 2.722883701324463 (2.5601760440181325)
| > grad_norm_0: tensor(10.4160, device='cuda:0') (tensor(20.2527, device='cuda:0'))
| > loss_gen: 2.3251559734344482 (2.2491575643762416)
| > loss_kl: 1.6746571063995361 (1.6147058326167705)
| > loss_feat: 6.628537178039551 (6.837342762996856)
| > loss_mel: 16.30409049987793 (15.448312170072487)
| > loss_duration: 1.4448950290679932 (1.4034054025478806)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.377334594726562 (27.552923708220863)
| > grad_norm_1: tensor(189.2550, device='cuda:0') (tensor(241.0621, device='cuda:0'))
| > current_lr_0: 0.00019890295108318404
| > current_lr_1: 0.00019890295108318404
| > step_time: 0.7355 (0.625561457337318)
| > loader_time: 0.0095 (0.007480225134990907)
--> TIME: 2025-05-14 16:17:46 -- STEP: 579/630 -- GLOBAL_STEP: 905300
| > loss_disc: 2.6032814979553223 (2.5612132557521408)
| > loss_disc_real_0: 0.13671919703483582 (0.16599899060728224)
| > loss_disc_real_1: 0.22749751806259155 (0.2106730002839125)
| > loss_disc_real_2: 0.1706048548221588 (0.22855887625089788)
| > loss_disc_real_3: 0.1680649220943451 (0.22872618489314855)
| > loss_disc_real_4: 0.1938702017068863 (0.23932535411059752)
| > loss_disc_real_5: 0.20271176099777222 (0.227688325051096)
| > loss_0: 2.6032814979553223 (2.5612132557521408)
| > grad_norm_0: tensor(19.1827, device='cuda:0') (tensor(21.3620, device='cuda:0'))
| > loss_gen: 2.1697194576263428 (2.249940763277506)
| > loss_kl: 1.7068116664886475 (1.615640084566436)
| > loss_feat: 6.478245258331299 (6.801452875549105)
| > loss_mel: 15.827506065368652 (15.433365347471879)
| > loss_duration: 1.4966517686843872 (1.4139729104099705)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.67893409729004 (27.51437199053986)
| > grad_norm_1: tensor(161.3223, device='cuda:0') (tensor(250.6563, device='cuda:0'))
| > current_lr_0: 0.00019890295108318404
| > current_lr_1: 0.00019890295108318404
| > step_time: 0.832 (0.6529812326908938)
| > loader_time: 0.0127 (0.008071687760954294)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005208750565846761 (-0.00017128388086954782)
| > avg_loss_disc: 2.5700876116752625 (-0.0024631818135580907)
| > avg_loss_disc_real_0: 0.15161263508101305 (-0.046665299062927545)
| > avg_loss_disc_real_1: 0.17115088924765587 (-0.025080015261967986)
| > avg_loss_disc_real_2: 0.2286906118194262 (+0.0140504737695058)
| > avg_loss_disc_real_3: 0.24866418664654097 (+0.03457039843002957)
| > avg_loss_disc_real_4: 0.27528093010187155 (+0.05886213233073559)
| > avg_loss_disc_real_5: 0.25437356655796367 (+0.06418283656239507)
| > avg_loss_0: 2.5700876116752625 (-0.0024631818135580907)
| > avg_loss_gen: 2.11737268169721 (+0.10357314348220825)
| > avg_loss_kl: 1.7275589406490326 (-0.06916224956512451)
| > avg_loss_feat: 6.1956067482630415 (-0.4695748488108311)
| > avg_loss_mel: 15.455869197845459 (-0.243731578191122)
| > avg_loss_duration: 1.5307957728703816 (-0.0003531475861868749)
| > avg_loss_1: 27.02720324198405 (-0.6792486508687325)
> EPOCH: 45/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 16:18:50)
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 16:19:17 -- STEP: 49/630 -- GLOBAL_STEP: 905400
| > loss_disc: 2.6082401275634766 (2.5740760978387325)
| > loss_disc_real_0: 0.07089465856552124 (0.1709259056619235)
| > loss_disc_real_1: 0.17557816207408905 (0.21121260584617146)
| > loss_disc_real_2: 0.19325175881385803 (0.22858809299614966)
| > loss_disc_real_3: 0.2628137469291687 (0.2313831603648711)
| > loss_disc_real_4: 0.20758232474327087 (0.2347668108283257)
| > loss_disc_real_5: 0.2542676329612732 (0.23283113569629435)
| > loss_0: 2.6082401275634766 (2.5740760978387325)
| > grad_norm_0: tensor(21.1259, device='cuda:0') (tensor(17.9584, device='cuda:0'))
| > loss_gen: 2.0707669258117676 (2.23885783127376)
| > loss_kl: 1.5466399192810059 (1.533362245073124)
| > loss_feat: 7.566462516784668 (6.96098484311785)
| > loss_mel: 15.594261169433594 (15.476647980359136)
| > loss_duration: 1.4374847412109375 (1.4231156986586901)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.215614318847656 (27.63296851333307)
| > grad_norm_1: tensor(39.7969, device='cuda:0') (tensor(192.4112, device='cuda:0'))
| > current_lr_0: 0.00019887808821429862
| > current_lr_1: 0.00019887808821429862
| > step_time: 0.5231 (0.5247726099831718)
| > loader_time: 0.005 (0.0050269146354831)
--> TIME: 2025-05-14 16:20:14 -- STEP: 149/630 -- GLOBAL_STEP: 905500
| > loss_disc: 2.4178574085235596 (2.5715500412371335)
| > loss_disc_real_0: 0.11673969775438309 (0.16463928554682122)
| > loss_disc_real_1: 0.24827350676059723 (0.21170699566402698)
| > loss_disc_real_2: 0.23293988406658173 (0.23108693877322561)
| > loss_disc_real_3: 0.22829699516296387 (0.23041820586127723)
| > loss_disc_real_4: 0.2684765160083771 (0.2399427356735972)
| > loss_disc_real_5: 0.2364753931760788 (0.23279926690879285)
| > loss_0: 2.4178574085235596 (2.5715500412371335)
| > grad_norm_0: tensor(7.3243, device='cuda:0') (tensor(16.9723, device='cuda:0'))
| > loss_gen: 2.4341769218444824 (2.2384506383998284)
| > loss_kl: 1.7979813814163208 (1.6171170609109349)
| > loss_feat: 6.908005237579346 (7.005183226310167)
| > loss_mel: 15.645342826843262 (15.473239559455205)
| > loss_duration: 1.4421374797821045 (1.3609006540887303)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.227643966674805 (27.694891155166115)
| > grad_norm_1: tensor(38.8190, device='cuda:0') (tensor(183.1619, device='cuda:0'))
| > current_lr_0: 0.00019887808821429862
| > current_lr_1: 0.00019887808821429862
| > step_time: 0.5684 (0.5468637383224179)
| > loader_time: 0.006 (0.005658741765374305)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_905500.pth
--> TIME: 2025-05-14 16:21:18 -- STEP: 249/630 -- GLOBAL_STEP: 905600
| > loss_disc: 2.669708728790283 (2.55464370470928)
| > loss_disc_real_0: 0.23332422971725464 (0.1626432178669186)
| > loss_disc_real_1: 0.17527298629283905 (0.2096999281022444)
| > loss_disc_real_2: 0.20248757302761078 (0.22986590186036734)
| > loss_disc_real_3: 0.21025623381137848 (0.23039923584365463)
| > loss_disc_real_4: 0.252818763256073 (0.23970157434662662)
| > loss_disc_real_5: 0.26569390296936035 (0.22696565959348258)
| > loss_0: 2.669708728790283 (2.55464370470928)
| > grad_norm_0: tensor(51.7098, device='cuda:0') (tensor(19.7150, device='cuda:0'))
| > loss_gen: 2.2900242805480957 (2.2574688995698384)
| > loss_kl: 1.6419733762741089 (1.6221775347927962)
| > loss_feat: 7.3883843421936035 (6.992940266927083)
| > loss_mel: 16.055206298828125 (15.496504615109608)
| > loss_duration: 1.4159557819366455 (1.3721832587537033)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.79154396057129 (27.74127458472807)
| > grad_norm_1: tensor(733.1777, device='cuda:0') (tensor(238.8897, device='cuda:0'))
| > current_lr_0: 0.00019887808821429862
| > current_lr_1: 0.00019887808821429862
| > step_time: 0.6248 (0.5691141182160281)
| > loader_time: 0.0074 (0.006208048288123198)
--> TIME: 2025-05-14 16:22:26 -- STEP: 349/630 -- GLOBAL_STEP: 905700
| > loss_disc: 2.6861016750335693 (2.555862026433207)
| > loss_disc_real_0: 0.18773765861988068 (0.16311930952577663)
| > loss_disc_real_1: 0.15421119332313538 (0.20983776855776173)
| > loss_disc_real_2: 0.19638533890247345 (0.22835803595518314)
| > loss_disc_real_3: 0.23615126311779022 (0.22996047668607325)
| > loss_disc_real_4: 0.20275261998176575 (0.23835179572631432)
| > loss_disc_real_5: 0.2439238727092743 (0.2284735559477847)
| > loss_0: 2.6861016750335693 (2.555862026433207)
| > grad_norm_0: tensor(34.2517, device='cuda:0') (tensor(20.5173, device='cuda:0'))
| > loss_gen: 2.3121232986450195 (2.253071995382665)
| > loss_kl: 1.60242760181427 (1.6228421011080374)
| > loss_feat: 7.326186656951904 (6.918640282912377)
| > loss_mel: 15.466581344604492 (15.469745493891587)
| > loss_duration: 1.4181454181671143 (1.3958920428267854)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.125463485717773 (27.660191948570983)
| > grad_norm_1: tensor(115.4961, device='cuda:0') (tensor(240.9099, device='cuda:0'))
| > current_lr_0: 0.00019887808821429862
| > current_lr_1: 0.00019887808821429862
| > step_time: 0.7077 (0.5952830027714155)
| > loader_time: 0.0082 (0.006736776548675274)
--> TIME: 2025-05-14 16:23:41 -- STEP: 449/630 -- GLOBAL_STEP: 905800
| > loss_disc: 2.6148247718811035 (2.565761063305997)
| > loss_disc_real_0: 0.10886061191558838 (0.166156656392964)
| > loss_disc_real_1: 0.24071013927459717 (0.21017241773334544)
| > loss_disc_real_2: 0.21383431553840637 (0.228453636501308)
| > loss_disc_real_3: 0.23159128427505493 (0.22982298952832253)
| > loss_disc_real_4: 0.2229686677455902 (0.23905753146832132)
| > loss_disc_real_5: 0.2029062658548355 (0.22913674250211907)
| > loss_0: 2.6148247718811035 (2.565761063305997)
| > grad_norm_0: tensor(13.7612, device='cuda:0') (tensor(21.9335, device='cuda:0'))
| > loss_gen: 2.0874552726745605 (2.247297144945055)
| > loss_kl: 1.318244457244873 (1.6212283399428982)
| > loss_feat: 5.872823715209961 (6.875183365658291)
| > loss_mel: 14.542522430419922 (15.479582376628782)
| > loss_duration: 1.4461426734924316 (1.3995625449713716)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.267189025878906 (27.622853795244865)
| > grad_norm_1: tensor(93.5411, device='cuda:0') (tensor(251.5825, device='cuda:0'))
| > current_lr_0: 0.00019887808821429862
| > current_lr_1: 0.00019887808821429862
| > step_time: 0.7662 (0.6265049617911763)
| > loader_time: 0.0094 (0.007265986737801397)
--> TIME: 2025-05-14 16:25:03 -- STEP: 549/630 -- GLOBAL_STEP: 905900
| > loss_disc: 2.5196545124053955 (2.570347533634234)
| > loss_disc_real_0: 0.15043199062347412 (0.16680570081120627)
| > loss_disc_real_1: 0.25237393379211426 (0.20991276974072223)
| > loss_disc_real_2: 0.2415984570980072 (0.22816530141456964)
| > loss_disc_real_3: 0.2503471374511719 (0.2300664287447278)
| > loss_disc_real_4: 0.24464501440525055 (0.2387751872042272)
| > loss_disc_real_5: 0.1929907351732254 (0.23077498731934526)
| > loss_0: 2.5196545124053955 (2.570347533634234)
| > grad_norm_0: tensor(11.2867, device='cuda:0') (tensor(20.8438, device='cuda:0'))
| > loss_gen: 2.268826723098755 (2.2343865895749007)
| > loss_kl: 1.4663143157958984 (1.6145792541608133)
| > loss_feat: 6.268208980560303 (6.816092742162541)
| > loss_mel: 15.315787315368652 (15.460655024794281)
| > loss_duration: 1.471065878868103 (1.4103321112787348)
| > amp_scaler: 512.0 (276.0510018214936)
| > loss_1: 26.790203094482422 (27.53604573109112)
| > grad_norm_1: tensor(117.3010, device='cuda:0') (tensor(235.4239, device='cuda:0'))
| > current_lr_0: 0.00019887808821429862
| > current_lr_1: 0.00019887808821429862
| > step_time: 0.8611 (0.660065324362944)
| > loader_time: 0.0108 (0.007822131850028951)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004987935225168864 (-0.00022081534067789656)
| > avg_loss_disc: 2.4607336123784385 (-0.10935399929682399)
| > avg_loss_disc_real_0: 0.12913380501170954 (-0.022478830069303513)
| > avg_loss_disc_real_1: 0.15443130085865656 (-0.016719588388999312)
| > avg_loss_disc_real_2: 0.2126805062095324 (-0.0160101056098938)
| > avg_loss_disc_real_3: 0.22931132341424623 (-0.019352863232294737)
| > avg_loss_disc_real_4: 0.250047458956639 (-0.025233471145232556)
| > avg_loss_disc_real_5: 0.25408973172307014 (-0.000283834834893526)
| > avg_loss_0: 2.4607336123784385 (-0.10935399929682399)
| > avg_loss_gen: 2.119618048270543 (+0.002245366573333296)
| > avg_loss_kl: 1.7210847636063893 (-0.006474177042643303)
| > avg_loss_feat: 6.4755859375 (+0.2799791892369585)
| > avg_loss_mel: 15.477304220199585 (+0.021435022354125977)
| > avg_loss_duration: 1.5383084019025166 (+0.00751262903213501)
| > avg_loss_1: 27.33190155029297 (+0.3046983083089181)
> EPOCH: 46/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 16:26:34)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 16:26:45 -- STEP: 19/630 -- GLOBAL_STEP: 906000
| > loss_disc: 2.6466479301452637 (2.577318492688631)
| > loss_disc_real_0: 0.1626051515340805 (0.17639889685731186)
| > loss_disc_real_1: 0.2008684277534485 (0.21073889261797854)
| > loss_disc_real_2: 0.30461597442626953 (0.2273295953085548)
| > loss_disc_real_3: 0.20699448883533478 (0.21884701361781672)
| > loss_disc_real_4: 0.19751155376434326 (0.23784141164076955)
| > loss_disc_real_5: 0.19167570769786835 (0.2302524502340116)
| > loss_0: 2.6466479301452637 (2.577318492688631)
| > grad_norm_0: tensor(22.8168, device='cuda:0') (tensor(22.2460, device='cuda:0'))
| > loss_gen: 2.029331684112549 (2.1584970449146472)
| > loss_kl: 1.323673129081726 (1.4992448499328213)
| > loss_feat: 7.858119487762451 (6.7884745597839355)
| > loss_mel: 15.535990715026855 (15.212515529833341)
| > loss_duration: 1.4055569171905518 (1.420531900305497)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.152671813964844 (27.07926428945441)
| > grad_norm_1: tensor(342.5720, device='cuda:0') (tensor(273.6542, device='cuda:0'))
| > current_lr_0: 0.00019885322845327182
| > current_lr_1: 0.00019885322845327182
| > step_time: 0.5495 (0.519160408722727)
| > loader_time: 0.0051 (0.004831038023296156)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_906000.pth
--> TIME: 2025-05-14 16:27:43 -- STEP: 119/630 -- GLOBAL_STEP: 906100
| > loss_disc: 2.3234660625457764 (2.5586594152851254)
| > loss_disc_real_0: 0.1260722577571869 (0.16396270153903167)
| > loss_disc_real_1: 0.19233325123786926 (0.21069584098182806)
| > loss_disc_real_2: 0.21433453261852264 (0.2252143647740869)
| > loss_disc_real_3: 0.20410087704658508 (0.22778733563022452)
| > loss_disc_real_4: 0.2557752728462219 (0.24008907540505672)
| > loss_disc_real_5: 0.17017322778701782 (0.23120169404174098)
| > loss_0: 2.3234660625457764 (2.5586594152851254)
| > grad_norm_0: tensor(17.6495, device='cuda:0') (tensor(21.9891, device='cuda:0'))
| > loss_gen: 2.4730193614959717 (2.24444933498607)
| > loss_kl: 1.6669564247131348 (1.5634674840614573)
| > loss_feat: 6.83500862121582 (6.959178355561585)
| > loss_mel: 15.236495971679688 (15.449666103395094)
| > loss_duration: 1.4910368919372559 (1.3953775387852132)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.702516555786133 (27.6121390527036)
| > grad_norm_1: tensor(410.2698, device='cuda:0') (tensor(262.4574, device='cuda:0'))
| > current_lr_0: 0.00019885322845327182
| > current_lr_1: 0.00019885322845327182
| > step_time: 0.544 (0.5387141985051772)
| > loader_time: 0.0061 (0.005521495803063658)
--> TIME: 2025-05-14 16:28:44 -- STEP: 219/630 -- GLOBAL_STEP: 906200
| > loss_disc: 2.65667724609375 (2.5496058899518013)
| > loss_disc_real_0: 0.16945724189281464 (0.1623740605499645)
| > loss_disc_real_1: 0.20389947295188904 (0.20933730641728662)
| > loss_disc_real_2: 0.16887511312961578 (0.2261036522856586)
| > loss_disc_real_3: 0.20426437258720398 (0.22677994624936962)
| > loss_disc_real_4: 0.2556861639022827 (0.24000901119894089)
| > loss_disc_real_5: 0.25326770544052124 (0.22844893100871344)
| > loss_0: 2.65667724609375 (2.5496058899518013)
| > grad_norm_0: tensor(10.9709, device='cuda:0') (tensor(23.8183, device='cuda:0'))
| > loss_gen: 2.1811718940734863 (2.256898248576682)
| > loss_kl: 1.40729820728302 (1.5817814338697147)
| > loss_feat: 5.703949928283691 (6.9424478866193935)
| > loss_mel: 15.4270601272583 (15.49130194589972)
| > loss_duration: 1.4716320037841797 (1.3636163941257073)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.191110610961914 (27.636045952365823)
| > grad_norm_1: tensor(184.5296, device='cuda:0') (tensor(287.3689, device='cuda:0'))
| > current_lr_0: 0.00019885322845327182
| > current_lr_1: 0.00019885322845327182
| > step_time: 0.5944 (0.5623140117349147)
| > loader_time: 0.0071 (0.006063865200025307)
--> TIME: 2025-05-14 16:29:48 -- STEP: 319/630 -- GLOBAL_STEP: 906300
| > loss_disc: 2.485516309738159 (2.553867583738225)
| > loss_disc_real_0: 0.22089023888111115 (0.1624560988855585)
| > loss_disc_real_1: 0.1644173413515091 (0.2097653174848766)
| > loss_disc_real_2: 0.25509729981422424 (0.22688544903616173)
| > loss_disc_real_3: 0.24634915590286255 (0.22742886304107954)
| > loss_disc_real_4: 0.3058658540248871 (0.24000083045525986)
| > loss_disc_real_5: 0.2177150696516037 (0.22949647852059063)
| > loss_0: 2.485516309738159 (2.553867583738225)
| > grad_norm_0: tensor(39.7988, device='cuda:0') (tensor(22.0715, device='cuda:0'))
| > loss_gen: 2.389317035675049 (2.2485756989930485)
| > loss_kl: 1.5088616609573364 (1.5862320188818302)
| > loss_feat: 6.972185134887695 (6.9071918266320305)
| > loss_mel: 15.212329864501953 (15.499805274054548)
| > loss_duration: 1.4998867511749268 (1.3934373164251677)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.58258056640625 (27.635242127325842)
| > grad_norm_1: tensor(416.6168, device='cuda:0') (tensor(262.1186, device='cuda:0'))
| > current_lr_0: 0.00019885322845327182
| > current_lr_1: 0.00019885322845327182
| > step_time: 0.6604 (0.5845448425197304)
| > loader_time: 0.0084 (0.006615547550883039)
--> TIME: 2025-05-14 16:31:00 -- STEP: 419/630 -- GLOBAL_STEP: 906400
| > loss_disc: 2.6117935180664062 (2.5566893579851757)
| > loss_disc_real_0: 0.20802024006843567 (0.1636157457967932)
| > loss_disc_real_1: 0.2239830642938614 (0.21110812533726842)
| > loss_disc_real_2: 0.1921502947807312 (0.22674193940967818)
| > loss_disc_real_3: 0.2348308265209198 (0.2270471976629874)
| > loss_disc_real_4: 0.2196788489818573 (0.23988749705664014)
| > loss_disc_real_5: 0.23550023138523102 (0.22905341377548497)
| > loss_0: 2.6117935180664062 (2.5566893579851757)
| > grad_norm_0: tensor(11.7729, device='cuda:0') (tensor(22.2786, device='cuda:0'))
| > loss_gen: 2.0408496856689453 (2.253009575932579)
| > loss_kl: 1.3186272382736206 (1.5954915997805628)
| > loss_feat: 6.573032855987549 (6.889751392218833)
| > loss_mel: 15.518760681152344 (15.5038628293677)
| > loss_duration: 1.4829157590866089 (1.3980869487248064)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.934186935424805 (27.640202337915973)
| > grad_norm_1: tensor(227.7064, device='cuda:0') (tensor(266.7575, device='cuda:0'))
| > current_lr_0: 0.00019885322845327182
| > current_lr_1: 0.00019885322845327182
| > step_time: 0.7419 (0.6130944641222535)
| > loader_time: 0.0105 (0.007149023770716993)
--> TIME: 2025-05-14 16:32:21 -- STEP: 519/630 -- GLOBAL_STEP: 906500
| > loss_disc: 2.5691514015197754 (2.555333518338801)
| > loss_disc_real_0: 0.25294506549835205 (0.16345453278120317)
| > loss_disc_real_1: 0.18784935772418976 (0.210535576721377)
| > loss_disc_real_2: 0.2216593474149704 (0.22702342856079627)
| > loss_disc_real_3: 0.2713010907173157 (0.22711031642780138)
| > loss_disc_real_4: 0.2519499361515045 (0.23940310370255988)
| > loss_disc_real_5: 0.21837176382541656 (0.228635496572952)
| > loss_0: 2.5691514015197754 (2.555333518338801)
| > grad_norm_0: tensor(22.6293, device='cuda:0') (tensor(22.4995, device='cuda:0'))
| > loss_gen: 2.412602663040161 (2.2490767038396786)
| > loss_kl: 1.7379194498062134 (1.5954807742942043)
| > loss_feat: 6.404796123504639 (6.834518606263089)
| > loss_mel: 14.743484497070312 (15.470771914502329)
| > loss_duration: 1.4226861000061035 (1.410763607548841)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.72148895263672 (27.560611555801422)
| > grad_norm_1: tensor(206.6958, device='cuda:0') (tensor(266.2888, device='cuda:0'))
| > current_lr_0: 0.00019885322845327182
| > current_lr_1: 0.00019885322845327182
| > step_time: 0.8305 (0.6480514819452071)
| > loader_time: 0.012 (0.007703140751245164)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_906500.pth
--> TIME: 2025-05-14 16:34:00 -- STEP: 619/630 -- GLOBAL_STEP: 906600
| > loss_disc: 2.453540802001953 (2.558595782913184)
| > loss_disc_real_0: 0.15667027235031128 (0.16460770783834577)
| > loss_disc_real_1: 0.258129745721817 (0.21048500239608361)
| > loss_disc_real_2: 0.21925176680088043 (0.2272878899833305)
| > loss_disc_real_3: 0.23283205926418304 (0.22738286478502104)
| > loss_disc_real_4: 0.26045307517051697 (0.23943749886240828)
| > loss_disc_real_5: 0.19085918366909027 (0.22836373238455696)
| > loss_0: 2.453540802001953 (2.558595782913184)
| > grad_norm_0: tensor(17.6931, device='cuda:0') (tensor(22.6859, device='cuda:0'))
| > loss_gen: 2.4407408237457275 (2.2469025278322534)
| > loss_kl: 1.5995160341262817 (1.6016375771054148)
| > loss_feat: 6.837296962738037 (6.811300326241045)
| > loss_mel: 14.8704833984375 (15.458569569811104)
| > loss_duration: 1.5157597064971924 (1.4210254749304263)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.263797760009766 (27.539435412849087)
| > grad_norm_1: tensor(458.0072, device='cuda:0') (tensor(267.8123, device='cuda:0'))
| > current_lr_0: 0.00019885322845327182
| > current_lr_1: 0.00019885322845327182
| > step_time: 1.1271 (0.6949596031416985)
| > loader_time: 0.0159 (0.00839005803060454)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005071500937143962 (+8.356571197509766e-05)
| > avg_loss_disc: 2.47554878393809 (+0.014815171559651397)
| > avg_loss_disc_real_0: 0.19802567611138025 (+0.06889187109967071)
| > avg_loss_disc_real_1: 0.19235053906838098 (+0.037919238209724426)
| > avg_loss_disc_real_2: 0.24042112131913504 (+0.02774061510960263)
| > avg_loss_disc_real_3: 0.257295864323775 (+0.02798454090952876)
| > avg_loss_disc_real_4: 0.24621331070860228 (-0.0038341482480367117)
| > avg_loss_disc_real_5: 0.22533472503225008 (-0.028755006690820067)
| > avg_loss_0: 2.47554878393809 (+0.014815171559651397)
| > avg_loss_gen: 2.347830792268117 (+0.22821274399757385)
| > avg_loss_kl: 1.7274486124515533 (+0.006363848845164055)
| > avg_loss_feat: 6.42671553293864 (-0.04887040456136038)
| > avg_loss_mel: 15.205394665400187 (-0.2719095547993984)
| > avg_loss_duration: 1.531374603509903 (-0.006933798392613655)
| > avg_loss_1: 27.238763968149822 (-0.0931375821431466)
> EPOCH: 47/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 16:34:22)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 16:35:11 -- STEP: 89/630 -- GLOBAL_STEP: 906700
| > loss_disc: 2.4660253524780273 (2.5635944082495867)
| > loss_disc_real_0: 0.26694273948669434 (0.16624661761053494)
| > loss_disc_real_1: 0.19293087720870972 (0.21170294134134657)
| > loss_disc_real_2: 0.20002765953540802 (0.2293565993228655)
| > loss_disc_real_3: 0.1726279854774475 (0.22523086292020392)
| > loss_disc_real_4: 0.1990397572517395 (0.23724611522106642)
| > loss_disc_real_5: 0.21260838210582733 (0.23243400504749812)
| > loss_0: 2.4660253524780273 (2.5635944082495867)
| > grad_norm_0: tensor(35.1580, device='cuda:0') (tensor(21.0366, device='cuda:0'))
| > loss_gen: 2.4087233543395996 (2.2537150329418405)
| > loss_kl: 1.4122964143753052 (1.5537107640437866)
| > loss_feat: 7.178004741668701 (7.036666146824869)
| > loss_mel: 15.135512351989746 (15.461032213789693)
| > loss_duration: 1.438550591468811 (1.4292470765917489)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.573089599609375 (27.73437127102627)
| > grad_norm_1: tensor(277.1409, device='cuda:0') (tensor(262.0121, device='cuda:0'))
| > current_lr_0: 0.00019882837179971516
| > current_lr_1: 0.00019882837179971516
| > step_time: 0.5352 (0.5293894939208298)
| > loader_time: 0.0056 (0.005359805032108608)
--> TIME: 2025-05-14 16:36:10 -- STEP: 189/630 -- GLOBAL_STEP: 906800
| > loss_disc: 2.433060884475708 (2.5632210824855406)
| > loss_disc_real_0: 0.18311238288879395 (0.16605737702871765)
| > loss_disc_real_1: 0.19642576575279236 (0.2084423372985194)
| > loss_disc_real_2: 0.27093151211738586 (0.2290656246520855)
| > loss_disc_real_3: 0.24384130537509918 (0.22588141995763023)
| > loss_disc_real_4: 0.2509738802909851 (0.2378630514340426)
| > loss_disc_real_5: 0.2175753116607666 (0.23430152623741715)
| > loss_0: 2.433060884475708 (2.5632210824855406)
| > grad_norm_0: tensor(13.1692, device='cuda:0') (tensor(17.5794, device='cuda:0'))
| > loss_gen: 2.5610392093658447 (2.235766961461024)
| > loss_kl: 1.794082760810852 (1.5942960293204695)
| > loss_feat: 6.988674163818359 (6.927162051831604)
| > loss_mel: 16.03472137451172 (15.393576097236108)
| > loss_duration: 1.4486606121063232 (1.3806916002243284)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.827177047729492 (27.531492818600285)
| > grad_norm_1: tensor(199.4626, device='cuda:0') (tensor(210.7130, device='cuda:0'))
| > current_lr_0: 0.00019882837179971516
| > current_lr_1: 0.00019882837179971516
| > step_time: 0.5914 (0.5545484452020552)
| > loader_time: 0.0076 (0.005971145377588022)
--> TIME: 2025-05-14 16:37:14 -- STEP: 289/630 -- GLOBAL_STEP: 906900
| > loss_disc: 2.5208239555358887 (2.5679458400369923)
| > loss_disc_real_0: 0.16224762797355652 (0.16677075784305392)
| > loss_disc_real_1: 0.2289031594991684 (0.20887109766163212)
| > loss_disc_real_2: 0.2685643434524536 (0.2279582808380721)
| > loss_disc_real_3: 0.24267253279685974 (0.22782535185863403)
| > loss_disc_real_4: 0.23226241767406464 (0.238720364224127)
| > loss_disc_real_5: 0.22182691097259521 (0.23302609790567708)
| > loss_0: 2.5208239555358887 (2.5679458400369923)
| > grad_norm_0: tensor(27.2448, device='cuda:0') (tensor(18.8723, device='cuda:0'))
| > loss_gen: 2.367121458053589 (2.238588325292596)
| > loss_kl: 1.6744446754455566 (1.612053232415737)
| > loss_feat: 6.654486179351807 (6.907201163084037)
| > loss_mel: 15.329843521118164 (15.434241344359506)
| > loss_duration: 1.4645180702209473 (1.3859635187267845)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.490413665771484 (27.57804761708401)
| > grad_norm_1: tensor(272.2855, device='cuda:0') (tensor(218.1305, device='cuda:0'))
| > current_lr_0: 0.00019882837179971516
| > current_lr_1: 0.00019882837179971516
| > step_time: 0.6469 (0.5793683594898364)
| > loader_time: 0.008 (0.0065020326924571555)
--> TIME: 2025-05-14 16:38:26 -- STEP: 389/630 -- GLOBAL_STEP: 907000
| > loss_disc: 2.6934499740600586 (2.5691050428964197)
| > loss_disc_real_0: 0.22602680325508118 (0.1674264677271132)
| > loss_disc_real_1: 0.2607561945915222 (0.20966868692467938)
| > loss_disc_real_2: 0.26028767228126526 (0.2275726722414512)
| > loss_disc_real_3: 0.283143550157547 (0.22821418489006307)
| > loss_disc_real_4: 0.3162498474121094 (0.2386686706144583)
| > loss_disc_real_5: 0.22587421536445618 (0.23238290459453906)
| > loss_0: 2.6934499740600586 (2.5691050428964197)
| > grad_norm_0: tensor(14.8210, device='cuda:0') (tensor(19.8621, device='cuda:0'))
| > loss_gen: 2.2019307613372803 (2.2381624639187514)
| > loss_kl: 1.5636399984359741 (1.6121472219881485)
| > loss_feat: 6.345163822174072 (6.877969910982029)
| > loss_mel: 16.694910049438477 (15.451926187255388)
| > loss_duration: 1.4761475324630737 (1.403928182118963)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.28179168701172 (27.584133927803727)
| > grad_norm_1: tensor(184.3196, device='cuda:0') (tensor(237.6870, device='cuda:0'))
| > current_lr_0: 0.00019882837179971516
| > current_lr_1: 0.00019882837179971516
| > step_time: 0.796 (0.6104985736023189)
| > loader_time: 0.0095 (0.0070670043288282415)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_907000.pth
--> TIME: 2025-05-14 16:39:48 -- STEP: 489/630 -- GLOBAL_STEP: 907100
| > loss_disc: 2.601818084716797 (2.574027176527403)
| > loss_disc_real_0: 0.1536385864019394 (0.16788081145237804)
| > loss_disc_real_1: 0.17399926483631134 (0.21003407888982922)
| > loss_disc_real_2: 0.2161354422569275 (0.22771489297197883)
| > loss_disc_real_3: 0.20714060962200165 (0.22832588117059266)
| > loss_disc_real_4: 0.21138975024223328 (0.23890641572407176)
| > loss_disc_real_5: 0.24067173898220062 (0.2327024840382223)
| > loss_0: 2.601818084716797 (2.574027176527403)
| > grad_norm_0: tensor(27.2858, device='cuda:0') (tensor(19.6610, device='cuda:0'))
| > loss_gen: 2.2672762870788574 (2.226431114541973)
| > loss_kl: 1.5111942291259766 (1.6168400913416)
| > loss_feat: 7.123096466064453 (6.8002604667882)
| > loss_mel: 16.14273452758789 (15.437709985822744)
| > loss_duration: 1.4612520933151245 (1.4060391955580454)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.50555419921875 (27.48728085149285)
| > grad_norm_1: tensor(60.7477, device='cuda:0') (tensor(232.4099, device='cuda:0'))
| > current_lr_0: 0.00019882837179971516
| > current_lr_1: 0.00019882837179971516
| > step_time: 0.8051 (0.6451353197936391)
| > loader_time: 0.0097 (0.007614455096316974)
--> TIME: 2025-05-14 16:41:18 -- STEP: 589/630 -- GLOBAL_STEP: 907200
| > loss_disc: 2.460636615753174 (2.577213091842186)
| > loss_disc_real_0: 0.21657803654670715 (0.16892155970751932)
| > loss_disc_real_1: 0.2556830942630768 (0.21022389055006777)
| > loss_disc_real_2: 0.1948137879371643 (0.22769540715298547)
| > loss_disc_real_3: 0.2406429797410965 (0.22902999666530532)
| > loss_disc_real_4: 0.27205902338027954 (0.23937285310748477)
| > loss_disc_real_5: 0.2556823492050171 (0.2330235916811257)
| > loss_0: 2.460636615753174 (2.577213091842186)
| > grad_norm_0: tensor(20.2630, device='cuda:0') (tensor(19.8654, device='cuda:0'))
| > loss_gen: 2.4104676246643066 (2.2220339125404944)
| > loss_kl: 1.7267612218856812 (1.6166027230803552)
| > loss_feat: 6.938033580780029 (6.763370334191312)
| > loss_mel: 16.093528747558594 (15.42704093881293)
| > loss_duration: 1.4810380935668945 (1.4160862454736574)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.649829864501953 (27.445134148330546)
| > grad_norm_1: tensor(465.2372, device='cuda:0') (tensor(230.9328, device='cuda:0'))
| > current_lr_0: 0.00019882837179971516
| > current_lr_1: 0.00019882837179971516
| > step_time: 0.9499 (0.6849569715749225)
| > loader_time: 0.0117 (0.008195416024666289)
> EVALUATION
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.005021293958028157 (-5.0206979115804615e-05)
| > avg_loss_disc: 2.6969982584317527 (+0.2214494744936628)
| > avg_loss_disc_real_0: 0.17665601956347624 (-0.021369656547904015)
| > avg_loss_disc_real_1: 0.23152120411396027 (+0.039170665045579284)
| > avg_loss_disc_real_2: 0.24874108657240868 (+0.008319965253273637)
| > avg_loss_disc_real_3: 0.2639805488288402 (+0.006684684505065208)
| > avg_loss_disc_real_4: 0.2467911976079146 (+0.0005778868993123187)
| > avg_loss_disc_real_5: 0.22728962947924933 (+0.0019549044469992505)
| > avg_loss_0: 2.6969982584317527 (+0.2214494744936628)
| > avg_loss_gen: 2.020670602718989 (-0.32716018954912807)
| > avg_loss_kl: 1.733679622411728 (+0.0062310099601745605)
| > avg_loss_feat: 6.457570393880208 (+0.03085486094156842)
| > avg_loss_mel: 15.539507389068604 (+0.33411272366841693)
| > avg_loss_duration: 1.5345938603083293 (+0.0032192567984263842)
| > avg_loss_1: 27.286022027333576 (+0.04725805918375414)
> EPOCH: 48/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 16:42:14)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 16:42:47 -- STEP: 59/630 -- GLOBAL_STEP: 907300
| > loss_disc: 2.708859443664551 (2.532058998689813)
| > loss_disc_real_0: 0.18269100785255432 (0.1602484134294219)
| > loss_disc_real_1: 0.25057950615882874 (0.20917633605205407)
| > loss_disc_real_2: 0.30012235045433044 (0.22599309985920535)
| > loss_disc_real_3: 0.27515438199043274 (0.22371255922115454)
| > loss_disc_real_4: 0.2985328733921051 (0.2352582829988609)
| > loss_disc_real_5: 0.24439255893230438 (0.22741157321606653)
| > loss_0: 2.708859443664551 (2.532058998689813)
| > grad_norm_0: tensor(19.4765, device='cuda:0') (tensor(15.9373, device='cuda:0'))
| > loss_gen: 2.216700792312622 (2.2578781782570534)
| > loss_kl: 1.3044724464416504 (1.5518962427721186)
| > loss_feat: 7.152626037597656 (7.181845309370655)
| > loss_mel: 15.8108549118042 (15.327422255176609)
| > loss_duration: 1.42124605178833 (1.423167782314753)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.905899047851562 (27.742209644640905)
| > grad_norm_1: tensor(192.8927, device='cuda:0') (tensor(188.3195, device='cuda:0'))
| > current_lr_0: 0.00019880351825324018
| > current_lr_1: 0.00019880351825324018
| > step_time: 0.5398 (0.5291442305354748)
| > loader_time: 0.006 (0.005221944744304076)
--> TIME: 2025-05-14 16:43:44 -- STEP: 159/630 -- GLOBAL_STEP: 907400
| > loss_disc: 2.7449822425842285 (2.5550695515278754)
| > loss_disc_real_0: 0.18663054704666138 (0.1618932599447808)
| > loss_disc_real_1: 0.2805441915988922 (0.20916655425380612)
| > loss_disc_real_2: 0.31488221883773804 (0.22569032528865263)
| > loss_disc_real_3: 0.25800755620002747 (0.2269854724594632)
| > loss_disc_real_4: 0.20022888481616974 (0.23759137393918428)
| > loss_disc_real_5: 0.20526786148548126 (0.23253649482562108)
| > loss_0: 2.7449822425842285 (2.5550695515278754)
| > grad_norm_0: tensor(36.0871, device='cuda:0') (tensor(16.8094, device='cuda:0'))
| > loss_gen: 2.352841377258301 (2.2466041576937315)
| > loss_kl: 1.6024749279022217 (1.5968181547128928)
| > loss_feat: 7.535106658935547 (7.044468168942432)
| > loss_mel: 15.606568336486816 (15.378687456718781)
| > loss_duration: 1.4590716361999512 (1.3632981139908793)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.55606460571289 (27.629876118785937)
| > grad_norm_1: tensor(90.3392, device='cuda:0') (tensor(191.3198, device='cuda:0'))
| > current_lr_0: 0.00019880351825324018
| > current_lr_1: 0.00019880351825324018
| > step_time: 0.5747 (0.5525833675696415)
| > loader_time: 0.0071 (0.005813451682996452)
--> TIME: 2025-05-14 16:44:47 -- STEP: 259/630 -- GLOBAL_STEP: 907500
| > loss_disc: 2.438088893890381 (2.5671602584220268)
| > loss_disc_real_0: 0.24259084463119507 (0.16527028249497575)
| > loss_disc_real_1: 0.1760125309228897 (0.20972836305275847)
| > loss_disc_real_2: 0.20855094492435455 (0.22662068351125164)
| > loss_disc_real_3: 0.1881418079137802 (0.22835149837506785)
| > loss_disc_real_4: 0.21511606872081757 (0.23882324418275974)
| > loss_disc_real_5: 0.18912909924983978 (0.2323563713939954)
| > loss_0: 2.438088893890381 (2.5671602584220268)
| > grad_norm_0: tensor(39.1025, device='cuda:0') (tensor(19.1592, device='cuda:0'))
| > loss_gen: 2.3314297199249268 (2.239511549702943)
| > loss_kl: 1.5879281759262085 (1.595117244941387)
| > loss_feat: 6.0401716232299805 (6.979027617391932)
| > loss_mel: 15.239988327026367 (15.374718585069575)
| > loss_duration: 1.4766249656677246 (1.3738670606870915)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 26.676143646240234 (27.562242080806307)
| > grad_norm_1: tensor(429.0744, device='cuda:0') (tensor(218.2307, device='cuda:0'))
| > current_lr_0: 0.00019880351825324018
| > current_lr_1: 0.00019880351825324018
| > step_time: 0.6501 (0.5744194468936404)
| > loader_time: 0.0075 (0.006333026186379689)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_907500.pth
--> TIME: 2025-05-14 16:45:59 -- STEP: 359/630 -- GLOBAL_STEP: 907600
| > loss_disc: 2.240346908569336 (2.5687744637385723)
| > loss_disc_real_0: 0.17110762000083923 (0.16583651439144073)
| > loss_disc_real_1: 0.1976683884859085 (0.21072206872419394)
| > loss_disc_real_2: 0.21713091433048248 (0.2273532254284139)
| > loss_disc_real_3: 0.19800633192062378 (0.22745405868069374)
| > loss_disc_real_4: 0.201119065284729 (0.23873704165469306)
| > loss_disc_real_5: 0.17890743911266327 (0.2313900028347637)
| > loss_0: 2.240346908569336 (2.5687744637385723)
| > grad_norm_0: tensor(27.7569, device='cuda:0') (tensor(21.2422, device='cuda:0'))
| > loss_gen: 2.4282259941101074 (2.236562570821609)
| > loss_kl: 1.6256834268569946 (1.603032621500552)
| > loss_feat: 7.043108940124512 (6.890523128190744)
| > loss_mel: 16.011600494384766 (15.401534300992747)
| > loss_duration: 1.4799978733062744 (1.396234703595261)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 28.5886173248291 (27.527887291230872)
| > grad_norm_1: tensor(571.7281, device='cuda:0') (tensor(234.7893, device='cuda:0'))
| > current_lr_0: 0.00019880351825324018
| > current_lr_1: 0.00019880351825324018
| > step_time: 0.6905 (0.6006674348145803)
| > loader_time: 0.0079 (0.006888605425948886)
--> TIME: 2025-05-14 16:47:14 -- STEP: 459/630 -- GLOBAL_STEP: 907700
| > loss_disc: 2.615466356277466 (2.5716567210901795)
| > loss_disc_real_0: 0.16766464710235596 (0.16570214222718943)
| > loss_disc_real_1: 0.21686236560344696 (0.21067839558997187)
| > loss_disc_real_2: 0.26104485988616943 (0.22728540363654595)
| > loss_disc_real_3: 0.24461378157138824 (0.22744770568829994)
| > loss_disc_real_4: 0.24639637768268585 (0.23941144814678267)
| > loss_disc_real_5: 0.2547076344490051 (0.232947906442717)
| > loss_0: 2.615466356277466 (2.5716567210901795)
| > grad_norm_0: tensor(8.6621, device='cuda:0') (tensor(19.7662, device='cuda:0'))
| > loss_gen: 2.23606538772583 (2.230616176569906)
| > loss_kl: 1.3665506839752197 (1.6080703548356599)
| > loss_feat: 5.277324676513672 (6.84259166592866)
| > loss_mel: 15.191995620727539 (15.423642513798733)
| > loss_duration: 1.411966323852539 (1.3998707940635609)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 25.483901977539062 (27.50479146338237)
| > grad_norm_1: tensor(95.6202, device='cuda:0') (tensor(217.7020, device='cuda:0'))
| > current_lr_0: 0.00019880351825324018
| > current_lr_1: 0.00019880351825324018
| > step_time: 0.764 (0.630435514553959)
| > loader_time: 0.0099 (0.007396274662225596)
--> TIME: 2025-05-14 16:48:36 -- STEP: 559/630 -- GLOBAL_STEP: 907800
| > loss_disc: 2.706016778945923 (2.5732106292397052)
| > loss_disc_real_0: 0.17809391021728516 (0.1665672348922181)
| > loss_disc_real_1: 0.15877234935760498 (0.20978434501159168)
| > loss_disc_real_2: 0.24142494797706604 (0.2268270801932739)
| > loss_disc_real_3: 0.22433839738368988 (0.2276038812183524)
| > loss_disc_real_4: 0.2296670526266098 (0.23974619317993068)
| > loss_disc_real_5: 0.22133196890354156 (0.23394678002606564)
| > loss_0: 2.706016778945923 (2.5732106292397052)
| > grad_norm_0: tensor(12.8782, device='cuda:0') (tensor(18.9617, device='cuda:0'))
| > loss_gen: 2.098175048828125 (2.2275183672128747)
| > loss_kl: 1.6957305669784546 (1.606139981469443)
| > loss_feat: 6.670124053955078 (6.80454267969285)
| > loss_mel: 15.600085258483887 (15.439225162717651)
| > loss_duration: 1.4829665422439575 (1.4109342737999717)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.547080993652344 (27.48836041691052)
| > grad_norm_1: tensor(53.4120, device='cuda:0') (tensor(205.3052, device='cuda:0'))
| > current_lr_0: 0.00019880351825324018
| > current_lr_1: 0.00019880351825324018
| > step_time: 0.8647 (0.6626149486343843)
| > loader_time: 0.0121 (0.007938297148893901)
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.0050858259201049805 (+6.45319620768232e-05)
| > avg_loss_disc: 2.588302473227183 (-0.1086957852045698)
| > avg_loss_disc_real_0: 0.2451520971953869 (+0.06849607763191065)
| > avg_loss_disc_real_1: 0.17595209926366806 (-0.055569104850292206)
| > avg_loss_disc_real_2: 0.2423033540447553 (-0.006437732527653367)
| > avg_loss_disc_real_3: 0.20747172832489014 (-0.056508820503950064)
| > avg_loss_disc_real_4: 0.22468254839380583 (-0.022108649214108766)
| > avg_loss_disc_real_5: 0.2318303349117438 (+0.004540705432494463)
| > avg_loss_0: 2.588302473227183 (-0.1086957852045698)
| > avg_loss_gen: 2.1615797579288483 (+0.14090915520985936)
| > avg_loss_kl: 1.6583293577035267 (-0.07535026470820116)
| > avg_loss_feat: 6.512588659922282 (+0.05501826604207416)
| > avg_loss_mel: 15.1087646484375 (-0.4307427406311035)
| > avg_loss_duration: 1.540999283393224 (+0.006405423084894668)
| > avg_loss_1: 26.982261339823406 (-0.30376068751017016)
> EPOCH: 49/50
--> /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000
> TRAINING (2025-05-14 16:49:56)
যদি লিভের আবেদন
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পানির উচিত কর্মীদের জন্য লি
[!] Character '\n' not found in the vocabulary. Discarding it.
কোম্পেনসেটরি লিভ কিভাবে কাজ করে
[!] Character '\n' not found in the vocabulary. Discarding it.
আমি এই বছর স্ট্রীরোগ বিশেষজ্ঞের কাছে যাব।
[!] Character '\n' not found in the vocabulary. Discarding it.
--> TIME: 2025-05-14 16:50:13 -- STEP: 29/630 -- GLOBAL_STEP: 907900
| > loss_disc: 2.6616249084472656 (2.5744836577053727)
| > loss_disc_real_0: 0.2214498519897461 (0.15732754741249416)
| > loss_disc_real_1: 0.2451103925704956 (0.20944388416306725)
| > loss_disc_real_2: 0.24719074368476868 (0.23665636726494493)
| > loss_disc_real_3: 0.23956458270549774 (0.22852862446472563)
| > loss_disc_real_4: 0.19871793687343597 (0.238756633524237)
| > loss_disc_real_5: 0.22923749685287476 (0.23294839571262227)
| > loss_0: 2.6616249084472656 (2.5744836577053727)
| > grad_norm_0: tensor(10.3587, device='cuda:0') (tensor(26.1478, device='cuda:0'))
| > loss_gen: 2.289095401763916 (2.2760600385994745)
| > loss_kl: 1.6088107824325562 (1.4861159900139118)
| > loss_feat: 6.842335224151611 (7.017549794295738)
| > loss_mel: 15.437192916870117 (15.611165079577216)
| > loss_duration: 1.4022531509399414 (1.41692381891711)
| > amp_scaler: 256.0 (256.0)
| > loss_1: 27.579689025878906 (27.807814828280744)
| > grad_norm_1: tensor(270.8441, device='cuda:0') (tensor(294.0019, device='cuda:0'))
| > current_lr_0: 0.00019877866781345852
| > current_lr_1: 0.00019877866781345852
| > step_time: 0.536 (0.521903605296694)
| > loader_time: 0.0052 (0.0048648653359248725)
--> TIME: 2025-05-14 16:51:08 -- STEP: 129/630 -- GLOBAL_STEP: 908000
| > loss_disc: 2.6096696853637695 (2.553782577662506)
| > loss_disc_real_0: 0.0923655554652214 (0.16104750161947207)
| > loss_disc_real_1: 0.18637090921401978 (0.20962314261484516)
| > loss_disc_real_2: 0.18162381649017334 (0.23047140644964323)
| > loss_disc_real_3: 0.2030901312828064 (0.224264749145323)
| > loss_disc_real_4: 0.22550131380558014 (0.23949343266413192)
| > loss_disc_real_5: 0.20229755342006683 (0.22651280069998067)
| > loss_0: 2.6096696853637695 (2.553782577662506)
| > grad_norm_0: tensor(19.0482, device='cuda:0') (tensor(24.5262, device='cuda:0'))
| > loss_gen: 2.18103289604187 (2.279563036999962)
| > loss_kl: 1.4165462255477905 (1.525559712750043)
| > loss_feat: 7.27138090133667 (7.048503616983576)
| > loss_mel: 15.12784481048584 (15.519334002058635)
| > loss_duration: 1.4758307933807373 (1.401184073714323)
| > amp_scaler: 256.0 (273.860465116279)
| > loss_1: 27.47263526916504 (27.774144579273784)
| > grad_norm_1: tensor(378.8158, device='cuda:0') (tensor(293.5519, device='cuda:0'))
| > current_lr_0: 0.00019877866781345852
| > current_lr_1: 0.00019877866781345852
| > step_time: 0.5504 (0.5384116856626762)
| > loader_time: 0.0064 (0.005491284436957781)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_908000.pth
--> TIME: 2025-05-14 16:52:13 -- STEP: 229/630 -- GLOBAL_STEP: 908100
| > loss_disc: 2.5444839000701904 (2.5659493338072665)
| > loss_disc_real_0: 0.15850293636322021 (0.16396256861598216)
| > loss_disc_real_1: 0.17794261872768402 (0.21024383884329984)
| > loss_disc_real_2: 0.2212647944688797 (0.23057467539237575)
| > loss_disc_real_3: 0.23973438143730164 (0.225254214942195)
| > loss_disc_real_4: 0.2374771386384964 (0.24030208542097084)
| > loss_disc_real_5: 0.22883963584899902 (0.23027954247320584)
| > loss_0: 2.5444839000701904 (2.5659493338072665)
| > grad_norm_0: tensor(7.5723, device='cuda:0') (tensor(23.4954, device='cuda:0'))
| > loss_gen: 2.2465503215789795 (2.260780594234386)
| > loss_kl: 1.5368551015853882 (1.56851503474223)
| > loss_feat: 6.6572465896606445 (6.945921843749467)
| > loss_mel: 15.342655181884766 (15.499920028786471)
| > loss_duration: 1.4689538478851318 (1.3642879131058943)
| > amp_scaler: 256.0 (266.0611353711789)
| > loss_1: 27.252260208129883 (27.639425385987394)
| > grad_norm_1: tensor(135.6610, device='cuda:0') (tensor(277.8966, device='cuda:0'))
| > current_lr_0: 0.00019877866781345852
| > current_lr_1: 0.00019877866781345852
| > step_time: 0.6072 (0.5680048767656223)
| > loader_time: 0.0074 (0.006083529068392958)
--> TIME: 2025-05-14 16:53:18 -- STEP: 329/630 -- GLOBAL_STEP: 908200
| > loss_disc: 2.657395362854004 (2.567549917110918)
| > loss_disc_real_0: 0.1810968816280365 (0.16415706809077957)
| > loss_disc_real_1: 0.1859029233455658 (0.21052782450403487)
| > loss_disc_real_2: 0.24176613986492157 (0.22927875078557836)
| > loss_disc_real_3: 0.2481638491153717 (0.22577877329113274)
| > loss_disc_real_4: 0.2538553476333618 (0.2387663405445209)
| > loss_disc_real_5: 0.23463012278079987 (0.23155608188961052)
| > loss_0: 2.657395362854004 (2.567549917110918)
| > grad_norm_0: tensor(9.5226, device='cuda:0') (tensor(22.5779, device='cuda:0'))
| > loss_gen: 2.1824142932891846 (2.2524814993414863)
| > loss_kl: 1.7615606784820557 (1.5814765883796476)
| > loss_feat: 6.4736833572387695 (6.898788050677639)
| > loss_mel: 15.720820426940918 (15.46991304496139)
| > loss_duration: 1.4529811143875122 (1.3921287835187823)
| > amp_scaler: 256.0 (263.0030395136776)
| > loss_1: 27.591461181640625 (27.59478794550098)
| > grad_norm_1: tensor(41.7319, device='cuda:0') (tensor(261.0721, device='cuda:0'))
| > current_lr_0: 0.00019877866781345852
| > current_lr_1: 0.00019877866781345852
| > step_time: 0.679 (0.5904733062152809)
| > loader_time: 0.0095 (0.006604835255167767)
--> TIME: 2025-05-14 16:54:32 -- STEP: 429/630 -- GLOBAL_STEP: 908300
| > loss_disc: 2.760556697845459 (2.5740168428087538)
| > loss_disc_real_0: 0.2756688892841339 (0.1654080960439359)
| > loss_disc_real_1: 0.19150292873382568 (0.2109230135704254)
| > loss_disc_real_2: 0.2149345576763153 (0.22980664885822155)
| > loss_disc_real_3: 0.24183772504329681 (0.22717410749766653)
| > loss_disc_real_4: 0.2631058990955353 (0.23964117220787456)
| > loss_disc_real_5: 0.27418962121009827 (0.2315788538931133)
| > loss_0: 2.760556697845459 (2.5740168428087538)
| > grad_norm_0: tensor(12.7767, device='cuda:0') (tensor(22.5345, device='cuda:0'))
| > loss_gen: 2.099001169204712 (2.245793495978509)
| > loss_kl: 1.52912437915802 (1.5890724289389473)
| > loss_feat: 5.857060432434082 (6.853464297759227)
| > loss_mel: 15.514841079711914 (15.491784255821388)
| > loss_duration: 1.446942687034607 (1.3965461998830582)
| > amp_scaler: 256.0 (261.37062937062933)
| > loss_1: 26.446969985961914 (27.57666065865185)
| > grad_norm_1: tensor(121.0548, device='cuda:0') (tensor(264.2182, device='cuda:0'))
| > current_lr_0: 0.00019877866781345852
| > current_lr_1: 0.00019877866781345852
| > step_time: 0.7548 (0.6206197438540165)
| > loader_time: 0.0104 (0.007180495139880058)
--> TIME: 2025-05-14 16:55:52 -- STEP: 529/630 -- GLOBAL_STEP: 908400
| > loss_disc: 2.743053913116455 (2.575979536106994)
| > loss_disc_real_0: 0.20175021886825562 (0.1653653229454741)
| > loss_disc_real_1: 0.22764872014522552 (0.21137121277517992)
| > loss_disc_real_2: 0.2436574399471283 (0.2291393125665661)
| > loss_disc_real_3: 0.15880562365055084 (0.22721415006032739)
| > loss_disc_real_4: 0.2100616842508316 (0.23972337731003535)
| > loss_disc_real_5: 0.2016935795545578 (0.23183794913986006)
| > loss_0: 2.743053913116455 (2.575979536106994)
| > grad_norm_0: tensor(23.5072, device='cuda:0') (tensor(22.0251, device='cuda:0'))
| > loss_gen: 2.08036470413208 (2.237293578275887)
| > loss_kl: 1.5579745769500732 (1.5905111530102038)
| > loss_feat: 6.498382091522217 (6.797157258753065)
| > loss_mel: 15.206754684448242 (15.476862673047359)
| > loss_duration: 1.4613685607910156 (1.40897888722627)
| > amp_scaler: 256.0 (260.35538752362925)
| > loss_1: 26.80484390258789 (27.510803529130037)
| > grad_norm_1: tensor(267.5166, device='cuda:0') (tensor(254.8337, device='cuda:0'))
| > current_lr_0: 0.00019877866781345852
| > current_lr_1: 0.00019877866781345852
| > step_time: 0.8295 (0.652828571251075)
| > loader_time: 0.011 (0.007709061941712926)
--> TIME: 2025-05-14 16:57:34 -- STEP: 629/630 -- GLOBAL_STEP: 908500
| > loss_disc: 2.690427541732788 (2.5768167021164614)
| > loss_disc_real_0: 0.12850241363048553 (0.16586506691286046)
| > loss_disc_real_1: 0.2358187735080719 (0.21146432394443132)
| > loss_disc_real_2: 0.24538667500019073 (0.2289161060260097)
| > loss_disc_real_3: 0.22198206186294556 (0.22767085666118253)
| > loss_disc_real_4: 0.22647352516651154 (0.23981761870778423)
| > loss_disc_real_5: 0.2541733384132385 (0.2314493991612251)
| > loss_0: 2.690427541732788 (2.5768167021164614)
| > grad_norm_0: tensor(28.9038, device='cuda:0') (tensor(21.8210, device='cuda:0'))
| > loss_gen: 2.114532470703125 (2.2330803005039597)
| > loss_kl: 1.5152922868728638 (1.595832685218896)
| > loss_feat: 6.263685703277588 (6.768927214066064)
| > loss_mel: 15.707995414733887 (15.477037625396195)
| > loss_duration: 1.500966191291809 (1.4188346127447908)
| > amp_scaler: 256.0 (259.66295707472176)
| > loss_1: 27.10247230529785 (27.493712438877512)
| > grad_norm_1: tensor(153.5322, device='cuda:0') (tensor(251.8459, device='cuda:0'))
| > current_lr_0: 0.00019877866781345852
| > current_lr_1: 0.00019877866781345852
| > step_time: 1.5655 (0.7087607952293803)
| > loader_time: 0.0162 (0.008369630774178074)
> CHECKPOINT : /kaggle/working/vits_4_nov-May-14-2025_10+28AM-0000000/checkpoint_908500.pth
> EVALUATION
উইকলি হলিডে কিভাবে নির্ধারিত হয়
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রতি সপ্তাহে দুই দিনের উইকলি হলিডে এমপ্লয়ীদের প্রাপ্য।
[!] Character '\n' not found in the vocabulary. Discarding it.
প্রেগন্যান্ট নারী কর্মচারীদের চার মাসের মেটারনিটি লিভ প্রদান করা হয়।
[!] Character '\n' not found in the vocabulary. Discarding it.
উইকলি হলিডে কর্মীদের মানসিক এবং শারীরিক স্বাস্থ্যের জন্য খুবই জরুরি।
[!] Character '\n' not found in the vocabulary. Discarding it.
| > Synthesizing test sentences.
--> EVAL PERFORMANCE
| > avg_loader_time: 0.004988551139831543 (-9.72747802734375e-05)
| > avg_loss_disc: 2.5385541717211404 (-0.04974830150604248)
| > avg_loss_disc_real_0: 0.14499463451405367 (-0.10015746268133321)
| > avg_loss_disc_real_1: 0.22765343263745308 (+0.05170133337378502)
| > avg_loss_disc_real_2: 0.21781828999519348 (-0.024485064049561828)
| > avg_loss_disc_real_3: 0.2322657642265161 (+0.02479403590162596)
| > avg_loss_disc_real_4: 0.24615220725536346 (+0.021469658861557633)
| > avg_loss_disc_real_5: 0.2334055888156096 (+0.0015752539038658142)
| > avg_loss_0: 2.5385541717211404 (-0.04974830150604248)
| > avg_loss_gen: 2.102485458056132 (-0.059094299872716416)
| > avg_loss_kl: 1.6893857717514038 (+0.031056414047877068)
| > avg_loss_feat: 6.298617959022522 (-0.21397070089976022)
| > avg_loss_mel: 15.427426973978678 (+0.3186623255411778)
| > avg_loss_duration: 1.5267953872680664 (-0.0142038961251576)
| > avg_loss_1: 27.044711430867512 (+0.062450091044105704)
```

---
*Converted from ODT format for GitHub compatibility*
