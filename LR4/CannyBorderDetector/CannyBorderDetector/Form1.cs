using GaussianBlur;
using MyGradientBorder;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace CannyBorderDetector
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            Bitmap originalImage = new Bitmap("C:\\Users\\AlmaZ\\PycharmProjects\\acom\\resources\\balls.jpg");

            List<List<int>> bwImage = new List<List<int>>();

            for (int y = 0; y < originalImage.Height; y++)
            {
                List<int> row = new List<int>();
                for (int x = 0; x < originalImage.Width; x++)
                {
                    Color pixel = originalImage.GetPixel(x, y);
                    int brightness = (int)(pixel.R * 0.3 + pixel.G * 0.59 + pixel.B * 0.11);
                    row.Add(brightness);
                    originalImage.SetPixel(x, y, Color.FromArgb(255, brightness, brightness, brightness));
                }
                bwImage.Add(row);
            }
            pictureBox1.Image = originalImage;

            var list = MyGauss.GaussianBlur(bwImage, 11, 1);

            GradientBorder gb = new GradientBorder(list);
            var borders = gb.GetBorder(30, 10, true);

            Bitmap brd = new Bitmap(originalImage);
            for (int y = 0; y < borders.Count; y++)
            {
                for (int x = 0; x < borders[y].Count; x++)
                {
                    brd.SetPixel(x, y, Color.FromArgb(255, borders[y][x], borders[y][x], borders[y][x]));
                }
            }
            pictureBox2.Image = brd;
        }
    }
}