scalable multiple tts识别

plan1:

1. 收集多平台tts单个字符发音文件，放置到同一文件夹下，命名规则：char.platform.otherinfo.mp3, 例如A.google.monica.mp3
  1.1. 统计已经有的tts资源，找出缺失资源并补充
  1.2. 按照命名规则对下载到的资源进行格式化
2. 编写合并音频脚本，脚本能够指定输出文件夹，生成音频总数
3. 编写shell脚本（为了防止每个人训练方法不同导致最后model不能互用），包含
  3.1. 调用生成音频脚本
  3.2. sox生成频谱图
  3.3. 调用train.py训练model
  3.4. 压缩生成的model文件
  3.5. 上传model文件，每个人就有多个model可用
4. 使用方法：选择一个model进行classify，上传submitty后拿出错误的再经过第二个model，一直到使用过所有model


plan2: *训练单个字符的model*


1. 针对单个字符进行model训练（利用plan1的tts资源）
2. 编写classify脚本，传入音频文件（8个字符的），可以实现
  2.1. 静音切割
  2.2. 切割后音频转频谱图并识别
  2.3. 合并识别结果并输出
3. 上传model文件和classify脚本
