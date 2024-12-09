from PIL import Image
from ultralytics import YOLO
import argparse


def main():
    print ("joh")
    parser = argparse.ArgumentParser(description="Running MalAI inference.")
    parser.add_argument(
        "--model", required=True, help="Path to the model checkpoint (.pt file)"
    )
    parser.add_argument(
        "--image", required=True, help="Path to the image file to run inference on (JPG format)"
    )
    parser.add_argument(
        "--result", required=False, help="Path to the image file to save inference results (JPG format)", default='./results.jpg'
    )
    args = parser.parse_args()

    # Load model
    model = YOLO(args.model)

    # Run inference on image
    results = model(args.image)  # results list

    # Show the results
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        # im.show()  # show image
        im.save(args.result)  # save image

if __name__ == "__main__":
    main()



