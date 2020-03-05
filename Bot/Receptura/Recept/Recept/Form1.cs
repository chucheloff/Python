using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace Recept
{
    public partial class Form1 : Form
    {
        List<string> peoples = new List<string>();
        int deputyCount = 0, prosecutorCount = 0, deputyCountExt = 0, prosecutorCountExt = 0;
        string[] deputy_info = new string[3];
        string[] prosecutor_info = new string[3];
        List<string> deputy_list_box = new List<string>();
        List<string> prosecutor_list_box = new List<string>();
        List<string> deputy_text_box = new List<string>();
        List<string> prosecutor_text_box = new List<string>();


        public Form1()
        {
            InitializeComponent();
        }

        private void getResult(string s)
        {
            DialogResult result = MessageBox.Show("Доложить?", "Что делать?", MessageBoxButtons.YesNo);
            if (result == DialogResult.Yes)
            {
                WriteMoves(s);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                deputy_info[0] = "зам";
                deputy_info[1] = "-";
                prosecutor_info[0] = "шеф";
                prosecutor_info[1] = "-";
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

            UpdateProsecutorCount();
        }


        private void DeputyIsHere_CheckedChanged(object sender, EventArgs e)
        {
            UpdateDeputyString(deputyIsHere.Checked);
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

        private void ProsecutorIsHere_CheckedChanged(object sender, EventArgs e)
        {
            UpdateProsecutorString(prosecutorIsHere.Checked);
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


        // now those two are for arriving and leaving office, like, full-time

        private void DeputyAtDinner_CheckedChanged(object sender, EventArgs e)
        {
            if (deputyAtDinner.Checked)
            {
                deputyAtDinner.ForeColor = Color.Black;
                deputyAtDinner.BackColor = Color.LawnGreen;
                getResult("Заместитель приехал");
            }
            else
            {
                deputyAtDinner.ForeColor = Color.LawnGreen;
                deputyAtDinner.BackColor = Color.FromArgb(64, 64, 64);
                getResult("Заместитель уехал");
            }

        }

        
        private void ProsecutorAtDinner_CheckedChanged(object sender, EventArgs e)
        {
            if (prosecutorAtDinner.Checked)
            {
                prosecutorAtDinner.ForeColor = Color.Black;
                prosecutorAtDinner.BackColor = Color.LawnGreen;
                getResult("Прокурор приехал");
            }
            else
            {
                prosecutorAtDinner.ForeColor = Color.LawnGreen;
                prosecutorAtDinner.BackColor = Color.FromArgb(64, 64, 64);
                getResult("Прокурор уехал");
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
            int n;
            deputy_text_box = new List<string>();
            string[] lines = source.Split('\n');
            foreach (string line in lines)
            {
                string new_line = line.Replace("+", "");
                if (new_line.Length > 0) {
                    while ((new_line[0] == ' ') || (int.TryParse(new_line[0].ToString(), out n) == true))
                    {
                        new_line = new_line.Substring(1);
                        if (new_line.Length == 0)
                        {
                            break;
                        }
                    }
                }
                
                deputy_text_box.Add(new_line);
            }
            WriteFile();
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

            prosecutor_text_box = new List<string>();
            string[] lines = source.Split('\n');
            int n;
            foreach (string line in lines)
            {
                string new_line = line.Replace("+", "");
                if (new_line.Length > 0)
                {
                    while ((new_line[0] == ' ')  || (int.TryParse(new_line[0].ToString(), out n) == true))
                    {
                        new_line = new_line.Substring(1);
                        if (new_line.Length == 0)
                        {
                            break;
                        }
                    }
                }
                prosecutor_text_box.Add(new_line);
            }
            WriteFile();

            UpdateProsecutorCount();
        }

        
        // Count
        void UpdateDeputyCount()
        {
            deputyCount = listBoxDeputy.SelectedItems.Count;

            // removing empty strings from count
            int updatedDeputyCount = deputyCount;
            for ( int i = 0; i < deputyCount; i++)
            {
                if (listBoxDeputy.SelectedItems[i].ToString() == "")
                {
                    updatedDeputyCount -= 1;
                }
            }
            deputyCount = updatedDeputyCount;

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
            deputy_info[2] = (deputyCount + deputyCountExt).ToString();
            WriteFile();
        }

        void UpdateProsecutorCount()
        {
            prosecutorCount = listBoxProsecutor.SelectedItems.Count;

            // removing empty strings from count
            int updatedProsecutorCount = prosecutorCount;
            for ( int i = 0; i< prosecutorCount; i++)
            {
                if (listBoxProsecutor.SelectedItems[i].ToString() == "")
                {
                    updatedProsecutorCount -= 1;
                }
            }

            prosecutorCount = updatedProsecutorCount;

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
            prosecutor_info[2] = (prosecutorCount + prosecutorCountExt).ToString();
            WriteFile();
        }

        
        // Check for intersect
        private void ListBoxDeputy_SelectedIndexChanged(object sender, EventArgs e)
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
            deputy_list_box = new List<string>();
            for (int i = 0; i < listBoxDeputy.SelectedItems.Count; i++)
            {
                deputy_list_box.Add(listBoxDeputy.SelectedItems[i].ToString());
            }
            WriteFile();
        }

        private void ListBoxProsecutor_SelectedIndexChanged(object sender, EventArgs e)
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
            prosecutor_list_box = new List<string>();
            for (int i = 0; i < listBoxProsecutor.SelectedItems.Count; i++)
            {
               prosecutor_list_box.Add(listBoxProsecutor.SelectedItems[i].ToString());
            }
            WriteFile();
        }

        private void UpdateDeputyString(bool v)
        {
            if (v)
            {
                deputy_info[1] = "+";
            }
            else
            {
                deputy_info[1] = "-";
            }
            WriteFile();
        }
        private void UpdateProsecutorString(bool v)
        {
            if (v)
            {
                prosecutor_info[1] = "+";
            }
            else
            {
                prosecutor_info[1] = "-";
            }
            WriteFile();
        }


        // compiles and writes to recept_info.txt updated 
        // string from @deputy_info and @prosecutor_info arrays
        // first (index = 0) element of arrays is "шеф" or "зам"
        // second (index=1) element of arrays is "+" or "-" for checking if they're
        // present on theirs' working places

        // WriteMoves gets @info parameter which is either of four:
        // - Заместитель уехал  - Заместитель уехал
        // - Прокурор уехал     - Прокурор приехал
        // and checks if it's already been written to the moves file, which is on
        // 120 sec read delay in bot, after each reading it's being erased, so
        // it's unlikely 

        private void WriteMoves(string info)
        {
            string reader = File.ReadAllText("moves_info.txt");
            reader += info + '\n';
            File.WriteAllText("moves_info.txt", reader);
        }

        private void WriteFile()
        {
            string final_string = "";
            foreach (string word in deputy_info)
            {
                final_string += word + "\n";
            }
            foreach (string word in deputy_list_box)
            {
                final_string += word + "\n";
            }
            foreach (string word in deputy_text_box)
            {
                final_string += word + "\n";
            }

            foreach (string word in prosecutor_info)
            {
                final_string += word + "\n";
            }
            foreach (string word in prosecutor_list_box)
            {
                final_string += word + "\n";
            }
            foreach (string word in prosecutor_text_box)
            {
                final_string += word + "\n";
            }
            File.WriteAllText("recept_info.txt", final_string);
        }

    }
}
