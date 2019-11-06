using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Drawing.Imaging;

namespace Recept
{
    public partial class Form1 : Form
    {
        List<string> peoples = new List<string>();
        int deputyCount = 0, prosecutorCount = 0, deputyCountExt = 0, prosecutorCountExt = 0;

        public Form1()
        {
            InitializeComponent();
        }

        public static void Test()
        {
            using (var image = Properties.Resources.PIVO_1)
            using (var newImage = ScaleImage(image, 100, 100))
            {
                newImage.Save(@"C:\Users\chuch\Documents\Code\Recept\Recept\Resources\PIVO_2.png", ImageFormat.Png);
            }
        }

        public static Image ScaleImage(Image image, int maxWidth, int maxHeight)
        {
            var ratioX = (double)maxWidth / image.Width;
            var ratioY = (double)maxHeight / image.Height;
            var ratio = Math.Min(ratioX, ratioY);

            var newWidth = (int)(image.Width * ratio);
            var newHeight = (int)(image.Height * ratio);

            var newImage = new Bitmap(newWidth, newHeight);

            using (var graphics = Graphics.FromImage(newImage))
                graphics.DrawImage(image, 0, 0, newWidth, newHeight);

            return newImage;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                string pathFile = "Peoples.txt";
                
                if (System.IO.File.Exists(pathFile))
                {
                    // Read peoples from file
                    string line;
                    StreamReader file = new StreamReader(pathFile, Encoding.Default);
                    while ((line = file.ReadLine()) != null)
                    {
                        peoples.Add(line);
                    }
                    file.Close();


                    // Out from file to lists
                    listBoxDeputy.Items.Clear();
                    listBoxProsecutor.Items.Clear();

                    listBoxDeputy.Items.Add("Прокурор");
                    listBoxProsecutor.Items.Add("Заместитель");

                    foreach (string people in peoples)
                    {
                        listBoxDeputy.Items.Add(people);
                        listBoxProsecutor.Items.Add(people);
                    }
                }
                else
                {
                    MessageBox.Show("Файл Peoples.txt не найден, применен встроенный в программу список, чтобы создать собственный список необходимо создать файл [Peoples.txt в директории вместе с исполнительным файлом (.exe)] с фамилиями начиная каждую с новой строки.");
                }
            }
            catch (Exception exc)
            {
                MessageBox.Show(exc + "");
            }
        }

        private void ListBoxDeputy_DrawItem(object sender, DrawItemEventArgs e)
        {
            e.DrawBackground();

            bool isItemSelected = ((e.State & DrawItemState.Selected) == DrawItemState.Selected);
            int itemIndex = e.Index;
            if (itemIndex >= 0 && itemIndex < listBoxDeputy.Items.Count)
            {
                Graphics g = e.Graphics;

                // Background Color
                SolidBrush backgroundColorBrush = new SolidBrush((isItemSelected) ? Color.FromArgb(25, 187, 155) : Color.DimGray);
                g.FillRectangle(backgroundColorBrush, e.Bounds);

                // Set text color
                string itemText = listBoxDeputy.Items[itemIndex].ToString();

                SolidBrush itemTextColorBrush = isItemSelected ? new SolidBrush(Color.Black) : new SolidBrush(Color.White);
                g.DrawString(itemText, e.Font, itemTextColorBrush, listBoxDeputy.GetItemRectangle(itemIndex).Location);

                // Clean up
                backgroundColorBrush.Dispose();
                itemTextColorBrush.Dispose();
            }

            e.DrawFocusRectangle();

            UpdateDeputyCount();
        }

        private void ListBoxProsecutor_DrawItem(object sender, DrawItemEventArgs e)
        {
            e.DrawBackground();

            bool isItemSelected = ((e.State & DrawItemState.Selected) == DrawItemState.Selected);
            int itemIndex = e.Index;
            if (itemIndex >= 0 && itemIndex < listBoxProsecutor.Items.Count)
            {
                Graphics g = e.Graphics;

                // Background Color
                SolidBrush backgroundColorBrush = new SolidBrush((isItemSelected) ? Color.FromArgb(25, 187, 155) : Color.DimGray);
                g.FillRectangle(backgroundColorBrush, e.Bounds);

                // Set text color
                string itemText = listBoxProsecutor.Items[itemIndex].ToString();

                SolidBrush itemTextColorBrush = (isItemSelected) ? new SolidBrush(Color.Black) : new SolidBrush(Color.White);
                g.DrawString(itemText, e.Font, itemTextColorBrush, listBoxProsecutor.GetItemRectangle(itemIndex).Location);

                // Clean up
                backgroundColorBrush.Dispose();
                itemTextColorBrush.Dispose();
            }

            e.DrawFocusRectangle();

            updateProsecutorCount();
        }

        private void DeputyIsHere_CheckedChanged(object sender, EventArgs e)
        {
            if (deputyIsHere.Checked)
            {
                deputyIsHere.ForeColor = Color.Black;
                deputyIsHere.BackColor = Color.FromArgb(25, 187, 155);
            }
            else
            {
                deputyIsHere.ForeColor = Color.FromArgb(25, 187, 155);
                deputyIsHere.BackColor = Color.FromArgb(64, 64, 64);
            }

            if (deputyIsHere.Checked)
            {
                listBoxProsecutor.SetSelected(0, false);
            }
        }

        private void prosecutorIsHere_CheckedChanged(object sender, EventArgs e)
        {
            if (prosecutorIsHere.Checked)
            {
                prosecutorIsHere.ForeColor = Color.Black;
                prosecutorIsHere.BackColor = Color.FromArgb(25, 187, 155);
            }
            else
            {
                prosecutorIsHere.ForeColor = Color.FromArgb(25, 187, 155);
                prosecutorIsHere.BackColor = Color.FromArgb(64, 64, 64);
            }


            if (prosecutorIsHere.Checked)
            {
                listBoxDeputy.SetSelected(0, false);
            }
        }

        private void deputyAtDinner_CheckedChanged(object sender, EventArgs e)
        {
            if (deputyAtDinner.Checked)
            {
                deputyAtDinner.ForeColor = Color.Black;
                deputyAtDinner.BackColor = Color.LawnGreen;
            }
            else
            {
                deputyAtDinner.ForeColor = Color.LawnGreen;
                deputyAtDinner.BackColor = Color.FromArgb(64, 64, 64);
            }

        }

        private void prosecutorAtDinner_CheckedChanged(object sender, EventArgs e)
        {
            if (prosecutorAtDinner.Checked)
            {
                prosecutorAtDinner.ForeColor = Color.Black;
                prosecutorAtDinner.BackColor = Color.LawnGreen;
            }
            else
            {
                prosecutorAtDinner.ForeColor = Color.LawnGreen;
                prosecutorAtDinner.BackColor = Color.FromArgb(64, 64, 64);
            }

        }

        // TextBox count (+1)

        private void RichTextBoxDeputy_TextChanged(object sender, EventArgs e)
        {
            string source = richTextBoxDeputy.Text;
            string substring = "+";
            int c = 0;
            int index = source.IndexOf(substring, 0);
            deputyCountExt = 0;
            while (index > -1)
            {
                int i = 1;
                while ((source.Length > index + i) && (source.Substring(index + i, 1) != " ") && (source.Substring(index + i, 1) != "\n"))
                {
                    int.TryParse(source.Substring(index + 1, i), out c);
                    i +=1;
                }
                deputyCountExt += c;
                index = source.IndexOf(substring, index + 1);
                
            }
            
            UpdateDeputyCount();
        }

        private void RichTextBoxProsecutor_TextChanged(object sender, EventArgs e)
        {
            string source = richTextBoxProsecutor.Text;
            string substring = "+";
            int c = 0;
            int index = source.IndexOf(substring, 0);
            prosecutorCountExt = 0;
            while (index > -1)
            {
                int i = 1;
                while ((source.Length > index + i) && (source.Substring(index + i, 1) != " ") && (source.Substring(index + i, 1) != "\n"))
                {
                    int.TryParse(source.Substring(index + 1, i), out c);
                    i += 1;
                }
                prosecutorCountExt += c;
                index = source.IndexOf(substring, index + 1);

            }
            updateProsecutorCount();
        }

        // Count
        void UpdateDeputyCount()
        {
            deputyCount = listBoxDeputy.SelectedItems.Count;

            labelDeputyCount.Text = (deputyCount + deputyCountExt) + " чел";

            if ((deputyCount + deputyCountExt) > 0)
            {
                labelDeputyCount.ForeColor = Color.Black;
                labelDeputyCount.BackColor = Color.FromArgb(25, 187, 155);
            }
            else
            {
                labelDeputyCount.ForeColor = Color.FromArgb(25, 187, 155);
                labelDeputyCount.BackColor = Color.FromArgb(64, 64, 64);
            }
        }

        void updateProsecutorCount()
        {
            prosecutorCount = listBoxProsecutor.SelectedItems.Count;

            labelProsecutorCount.Text = (prosecutorCount + prosecutorCountExt) + " чел";
            if ((prosecutorCount + prosecutorCountExt) > 0)
            {
                labelProsecutorCount.ForeColor = Color.Black;
                labelProsecutorCount.BackColor = Color.FromArgb(25, 187, 155);
            }
            else
            {
                labelProsecutorCount.ForeColor = Color.FromArgb(25, 187, 155);
                labelProsecutorCount.BackColor = Color.FromArgb(64, 64, 64);
            }
        }

        // Check for intersect
        private void listBoxDeputy_SelectedIndexChanged(object sender, EventArgs e)
        {
            for (int i = 0; i < listBoxDeputy.Items.Count; i++)
            {
                if (i == 0 && listBoxDeputy.GetSelected(i))
                {
                    prosecutorIsHere.Checked = false;
                }
                if (listBoxDeputy.GetSelected(i) && listBoxProsecutor.GetSelected(i) && i != 0)
                {
                    listBoxProsecutor.SetSelected(i, false);
                }
            }
        }

        private void listBoxProsecutor_SelectedIndexChanged(object sender, EventArgs e)
        {
            for (int i = 0; i < listBoxDeputy.Items.Count; i++)
            {
                if (i == 0 && listBoxProsecutor.GetSelected(i))
                {
                    deputyIsHere.Checked = false;
                }
                if (listBoxDeputy.GetSelected(i) && listBoxProsecutor.GetSelected(i) && i != 0)
                {
                    listBoxDeputy.SetSelected(i, false);
                }
            }
        }

    }
}
