# -*- coding: utf-8 -*-
""" Module for parsing different media type by extensions (copy/paste from Wikipedia).
Module returns one of media type as list of extensions. Module used in main_script.py.
"""
import re


class Extension(object):
    """ Base class for getting file extensions. Built in files extensions for video, audio and image"""
    raw_video_formats = """.flv.f4v.f4p.f4a.f4b.nsv.roq.mxf.3g2.3gp.svi.m4v.mpg.mpeg
            .m2v.mpg.mp2.mpeg.mpe.mpv.mp4.m4p.m4v.amv.asf.rmvb.rm.yuv
            .wmv.mov.qt.avi.mng.gifv.drc.ogv.ogg.vob.mkv.webm"""

    raw_audio_formats = """AA AAC AC3 ADX AHX AIFF APE ASF AU AUD DMF DTS DXD FLAC
            MIDI MMF MOD MP1 MP2 MP3 MPC Ogg Opu RA TTA VOC VOX VQF WAV WMA XM """

    raw_image_formats = """ ANI ANIM APNG ART BMP BPG BSAVE CAL CIN CPC CPT DDS DPX ECW EXR FITS
            FLIC FLIF FPX GIF HDRi HEVC ICER ICNS ICO ICS ILBM JBIG JBIG2 JNG JPG JPEG
            JP2 JPEG-LS JPEG XR KRA MNG MIFF NRRD ORA PAM PBM PGM PPM PNM PCX
            PGF PICtor PNG PSD PSB PSP QTVR RAS RBE JPEG-HDR Logluv TIFF SGI TGA TIFF
            TIFF UFO UFP WBMP WebP XBM XCF XPM XWD
            CIFF DNG AI CDR CGM DXF EVA EMF Gerber HVIF IGES PGML SVG VML WMF Xar
            CDF DjVu EPS PDF PICT PS SWF XAML"""

    @staticmethod
    def get_extensions(raw_format):
        """ Return list of file extensions with dot"""
        raw_extensions = re.findall("\w+", raw_format, re.MULTILINE)
        extensions = ['.' + extension.lower() for extension in raw_extensions]
        return extensions

    @property
    def video(self):
        return self.get_extensions(self.raw_video_formats)

    @property
    def audio(self):
        return self.get_extensions(self.raw_audio_formats)

    @property
    def image(self):
        return self.get_extensions(self.raw_image_formats)


if __name__ == "__main__":
    extension = Extension()
    print("Found next extension types:\n{}\n{}\n{}\n".format(extension.video,
                                                             extension.audio,
                                                             extension.image))
    print(extension.get_extensions(".any .other Format needed"))
