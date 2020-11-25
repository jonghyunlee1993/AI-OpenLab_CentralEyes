import cv2
import argparse

parser = argparse.ArgumentParser(description='python Implementation')
parser.add_argument('--input_file', type=str, default=None, help='input_file_name')
parser.add_argument('--destination', type=str, default='obj_train_data', help='destination_dir')

args = parser.parse_args()

def read_video_file(path):
	vidcap = cv2.VideoCapture(path)

	return vidcap

def extract_frames(vidcap, destination, step=1):
	count = 0
	total = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

	while vidcap.isOpened():
		try:
			vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)
			ret, frame = vidcap.read()

			if count % 100 == 0:
				print(f"{(count / total) * 100:2.2f}%")

			cv2.imwrite(f"{destination}/frame_{count:06}.jpg", frame)
			count += 1
		except:
			break

	print("Done!")

if __name__ == "__main__":
	vidcap = read_video_file(args.input_file)
	extract_frames(vidcap, destination=args.destination)
