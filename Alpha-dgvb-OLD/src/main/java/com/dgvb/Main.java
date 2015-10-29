package com.dgvb;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfRect;
import org.opencv.core.Point;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.objdetect.CascadeClassifier;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        System.out.print("Enter the full path of image file: ");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String path = br.readLine();

        String parsedPath = detectFace(path);
        if (parsedPath != "") {
            System.out.printf("Image successfully parsed: %s\n", parsedPath);
        }
    }

    public static String detectFace(String path) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        CascadeClassifier faceDetector = new CascadeClassifier(Main.class.getResource("haarcascade_frontalface_alt.xml").getPath());
        Mat img = Imgcodecs.imread(path);
        MatOfRect faceDetections = new MatOfRect();
        faceDetector.detectMultiScale(img, faceDetections);

        for (Rect rect : faceDetections.toArray()) {
            Imgproc.rectangle(
                    img,
                    new Point(rect.x, rect.y),
                    new Point(rect.x + rect.width, rect.y + rect.height),
                    new Scalar(0, 255, 0)
            );
        }
        String[] splitPath = path.split("/");
        String filename = "out-" + splitPath[splitPath.length - 1];
        Imgcodecs.imwrite(filename, img);

        return filename;
    }
}
