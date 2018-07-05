{
  'targets': [{
    'target_name': 'audioMixer',
    'sources': [
      'addon.cc',
      'AudioMixerWrapper.cc',
      'AudioMixer.cpp',
      'AcmmFrameMixer.cpp',
      'AcmmParticipant.cpp',
      'AcmDecoder.cpp',
      'FfDecoder.cpp',
      'AcmEncoder.cpp',
      'PcmEncoder.cpp',
      'FfEncoder.cpp',
      '../../addons/common/NodeEventRegistry.cc',
      '../../../core/woogeen_base/MediaFramePipeline.cpp',
      '../../../core/woogeen_base/AudioUtilities.cpp',
    ],
    'cflags_cc': [
        '-Wall',
        '-O$(OPTIMIZATION_LEVEL)',
        '-g',
        '-std=c++11',
        '-DWEBRTC_POSIX',
    ],
    'cflags_cc!': [
        '-fno-exceptions',
    ],
    'include_dirs': [ '$(CORE_HOME)/common',
                      '$(CORE_HOME)/woogeen_base',
                      '$(CORE_HOME)/../../third_party/webrtc/src',
                      '$(CORE_HOME)/../../build/libdeps/build/include',
    ],
    'libraries': [
      '-L$(CORE_HOME)/../../third_party/webrtc', '-lwebrtc',
      '-lboost_thread',
      '-llog4cxx',
      '<!@(pkg-config --libs libavcodec)',
      '<!@(pkg-config --libs libavformat)',
      '<!@(pkg-config --libs libavutil)',
    ],
  }]
}
