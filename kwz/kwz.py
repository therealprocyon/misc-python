#!/usr/bin/env python3


# Copyright 2018 TheRealProcyon (Cecillia)

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import struct
import datetime


def main():

    with open("./files/test.kwz", "rb") as file:
        magic, length = struct.unpack("<4sI", file.read(8))

        # the following is uint32
        checksum_crc32 = struct.unpack("<I", file.read(4))[0]
        print(f"\nThe CRC32 Checksum is: {checksum_crc32}")
        creation_timestamp = struct.unpack("<I", file.read(4))[0]

        time_since_date = datetime.datetime(2000, 1, 1, 0, 0, 0)
        time_since_date += datetime.timedelta(seconds=creation_timestamp)
        time_since_date = time_since_date.strftime('%Y-%m-%d %H:%M:%S')

        print(f"\n\nThe Creation Timestamp is: {creation_timestamp}" +
               "\n\nThis indicates the seconds " +
               "since midnight 2000-01-01.\n" +
               "In this instance it states the creation time.\n" +
               "The same applies to the edit timestamp.\n\n" +
               "The date the file got created is:\n" +
               f"{time_since_date}\n\n\n")

        edit_timestamp = struct.unpack("<I", file.read(4))[0]
        time_since_date = datetime.datetime(2000, 1, 1, 0, 0, 0)
        time_since_date += datetime.timedelta(seconds=edit_timestamp)
        time_since_date = time_since_date.strftime('%Y-%m-%d %H:%M:%S')

        print(f"The Last Edit Timestamp is: {edit_timestamp}." +
               "\nFor an explanation " +
               "see the Creation Timestamp section\n\n" +
               "The date the file got created is:\n" +
               f"{time_since_date}\n\n")

        app_version = struct.unpack("<I", file.read(4))[0]
        print("The Version of the app used to create the file" +
              f" is: {app_version}")

        # the following is hex[10]
        d = file.read(10).hex()
        root_author_id = '-'.join([d[:4], d[4:8], d[8:12], d[12:18]])
        print(f"\n\n\nThe Root Author ID is: {root_author_id}")
        d = file.read(10).hex()
        parent_author_id = '-'.join([d[:4], d[4:8], d[8:12], d[12:18]])
        print(f"The Parent Author ID is: {parent_author_id}")
        d = file.read(10).hex()
        current_author_id = '-'.join([d[:4], d[4:8], d[8:12], d[12:18]])
        print(f"The Current Author ID is: {current_author_id}")

        # the following is actually an uint16[11] UTF16-LE
        # null-terminated null-padded string
        root_author_name = file.read(22).decode("utf-16le")
        print(f"\n\nThe Root Author's Name is: {root_author_name}")
        parent_author_name = file.read(22).decode("utf-16le")
        print(f"The Parent Author's Name is: {parent_author_name}")
        current_author_name = file.read(22).decode("utf-16le")
        print(f"The Current Author's Name is: {current_author_name}\n\n")

        # the following is char[28]
        root_filename = file.read(28).decode("utf-8")
        print(f"The Root Filename is: {root_filename}")
        parent_filename = file.read(28).decode("utf-8")
        print(f"The Parent Filename is: {parent_filename}")
        current_filename = file.read(28).decode("utf-8")
        print(f"The Current Filename is: {current_filename}\n\n")

        # the following is uint16
        frame_count = struct.unpack("<H", file.read(2))[0]
        print(f"\nThe Frame Count is: {frame_count}")
        thumbnail_frame_index = struct.unpack("<H", file.read(2))[0]
        print(f"The Thumbnail Frame Index is: {thumbnail_frame_index}\n")

        # the following reads the flags bitwise, and then checks
        # if the flags are set or unset
        kfh_flags = int(bin(struct.unpack("<H", file.read(2))[0])
                        [2:].zfill(8), 2)

        # See: https://bit.ly/2PJwPnP for the docs
        if (kfh_flags >> 0) & 0x01:
            lock_flag = "The Lock Flag is set"
        elif (kfh_flags >> 0) & 0x01 == 0:
            lock_flag = "The Lock Flag isn't set"

        if (kfh_flags >> 1) & 0x01:
            loop_playback_flag = "The Loop Playback Flag is set"
        elif (kfh_flags >> 1) & 0x01 == 0:
            loop_playback_flag = "The Loop Playback Flag isn't set"

        if (kfh_flags >> 4) & 0x01:
            toolset_flag = "the Toolset Flag is set"
        elif (kfh_flags >> 4) & 0x01 == 0:
            toolset_flag = "the Toolset Flag isn't set"

        print("\nThese are the flag states:\n\n" +
              f"{lock_flag};\n{loop_playback_flag};\n" +
              f"And {toolset_flag}.\n\n")

        # the following is uint8
        frame_speed = struct.unpack("<B", file.read(1))[0]

        # See: https://bit.ly/2QSJRM2 for the docs
        if frame_speed == 0:
            frame_speed = "1 frame every 5 seconds"
        elif frame_speed == 1:
            frame_speed = "1 frame every 2 seconds"
        elif frame_speed == 2:
            frame_speed = "1 frame per second"
        elif frame_speed == 3:
            frame_speed = "2 frames per second"
        elif frame_speed == 4:
            frame_speed = "4 frames per second"
        elif frame_speed == 5:
            frame_speed = "6 frames per second"
        elif frame_speed == 6:
            frame_speed = "8 frames per second"
        elif frame_speed == 7:
            frame_speed = "12 frames per second"
        elif frame_speed == 8:
            frame_speed = "20 frames per second"
        elif frame_speed == 9:
            frame_speed = "24 frames per second"
        elif frame_speed == 10:
            frame_speed = "30 frames per second"

        print(f"The Frame Speed is: {frame_speed}.\n\n\n")

        layer_visibility_flags = int(bin(struct.unpack("<B",
                                     file.read(1))[0])[2:].zfill(8),
                                     2)

        # See: https://bit.ly/2Q6QiOC for the docs
        if (layer_visibility_flags >> 0) & 0x01:
            layer_a_flag = "Layer A is invisible"
        elif (layer_visibility_flags >> 0) & 0x01 == 0:
            layer_a_flag = "Layer A is visible"

        if (layer_visibility_flags >> 1) & 0x01:
            layer_b_flag = "Layer B is invisible"
        elif (layer_visibility_flags >> 1) & 0x01 == 0:
            layer_b_flag = "Layer B is visible"

        if (layer_visibility_flags >> 2) & 0x01:
            layer_c_flag = "Layer C is invisible"
        elif (layer_visibility_flags >> 2) & 0x01 == 0:
            layer_c_flag = "Layer C is visible"

        print("The Layer Visibility Flag data is:\n\n" +
              f"{layer_a_flag};\n{layer_b_flag};\n{layer_c_flag}.\n")


if __name__ == '__main__':
    main()
