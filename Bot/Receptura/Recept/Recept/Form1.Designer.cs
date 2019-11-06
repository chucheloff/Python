namespace Recept
{
    partial class Form1
    {
        /// <summary>
        /// Требуется переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Обязательный метод для поддержки конструктора - не изменяйте
        /// содержимое данного метода при помощи редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.listBoxDeputy = new System.Windows.Forms.ListBox();
            this.richTextBoxDeputy = new System.Windows.Forms.RichTextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.richTextBoxProsecutor = new System.Windows.Forms.RichTextBox();
            this.listBoxProsecutor = new System.Windows.Forms.ListBox();
            this.deputyIsHere = new System.Windows.Forms.CheckBox();
            this.prosecutorIsHere = new System.Windows.Forms.CheckBox();
            this.deputyAtDinner = new System.Windows.Forms.CheckBox();
            this.prosecutorAtDinner = new System.Windows.Forms.CheckBox();
            this.labelDeputyCount = new System.Windows.Forms.Label();
            this.labelProsecutorCount = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // listBoxDeputy
            // 
            this.listBoxDeputy.BackColor = System.Drawing.Color.DimGray;
            this.listBoxDeputy.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.listBoxDeputy.Cursor = System.Windows.Forms.Cursors.Hand;
            this.listBoxDeputy.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.listBoxDeputy.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.listBoxDeputy.ForeColor = System.Drawing.Color.White;
            this.listBoxDeputy.FormattingEnabled = true;
            this.listBoxDeputy.ItemHeight = 30;
            this.listBoxDeputy.Items.AddRange(new object[] {
            "Прокурор",
            "Трепилов",
            "Токарев",
            "Сапожников",
            "Решетов",
            "Стыров",
            "Калугин",
            "Крылов",
            "Иванов",
            "",
            "Кочергина",
            "Каташова",
            "Завьялова",
            "Тарабарина"});
            this.listBoxDeputy.Location = new System.Drawing.Point(14, 63);
            this.listBoxDeputy.Name = "listBoxDeputy";
            this.listBoxDeputy.SelectionMode = System.Windows.Forms.SelectionMode.MultiSimple;
            this.listBoxDeputy.Size = new System.Drawing.Size(206, 360);
            this.listBoxDeputy.TabIndex = 1;
            this.listBoxDeputy.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.ListBoxDeputy_DrawItem);
            this.listBoxDeputy.SelectedIndexChanged += new System.EventHandler(this.listBoxDeputy_SelectedIndexChanged);
            // 
            // richTextBoxDeputy
            // 
            this.richTextBoxDeputy.BackColor = System.Drawing.Color.DimGray;
            this.richTextBoxDeputy.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.richTextBoxDeputy.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.richTextBoxDeputy.ForeColor = System.Drawing.Color.Aquamarine;
            this.richTextBoxDeputy.Location = new System.Drawing.Point(14, 431);
            this.richTextBoxDeputy.Name = "richTextBoxDeputy";
            this.richTextBoxDeputy.Size = new System.Drawing.Size(206, 176);
            this.richTextBoxDeputy.TabIndex = 3;
            this.richTextBoxDeputy.Text = "";
            this.richTextBoxDeputy.TextChanged += new System.EventHandler(this.RichTextBoxDeputy_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.ForeColor = System.Drawing.Color.White;
            this.label1.Location = new System.Drawing.Point(11, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(105, 16);
            this.label1.TabIndex = 7;
            this.label1.Text = "Заместитель";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.ForeColor = System.Drawing.Color.White;
            this.label2.Location = new System.Drawing.Point(258, 9);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(81, 16);
            this.label2.TabIndex = 8;
            this.label2.Text = "Прокурор";
            // 
            // richTextBoxProsecutor
            // 
            this.richTextBoxProsecutor.BackColor = System.Drawing.Color.DimGray;
            this.richTextBoxProsecutor.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.richTextBoxProsecutor.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.richTextBoxProsecutor.ForeColor = System.Drawing.Color.Aquamarine;
            this.richTextBoxProsecutor.Location = new System.Drawing.Point(261, 431);
            this.richTextBoxProsecutor.Name = "richTextBoxProsecutor";
            this.richTextBoxProsecutor.Size = new System.Drawing.Size(206, 176);
            this.richTextBoxProsecutor.TabIndex = 10;
            this.richTextBoxProsecutor.Text = "";
            this.richTextBoxProsecutor.TextChanged += new System.EventHandler(this.RichTextBoxProsecutor_TextChanged);
            // 
            // listBoxProsecutor
            // 
            this.listBoxProsecutor.BackColor = System.Drawing.Color.DimGray;
            this.listBoxProsecutor.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.listBoxProsecutor.Cursor = System.Windows.Forms.Cursors.Hand;
            this.listBoxProsecutor.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.listBoxProsecutor.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.listBoxProsecutor.ForeColor = System.Drawing.Color.White;
            this.listBoxProsecutor.FormattingEnabled = true;
            this.listBoxProsecutor.ItemHeight = 30;
            this.listBoxProsecutor.Items.AddRange(new object[] {
            "Заместитель",
            "Трепилов",
            "Токарев",
            "Сапожников",
            "Решетов",
            "Стыров",
            "Калугин",
            "Крылов",
            "Иванов",
            "",
            "Кочергина",
            "Каташова",
            "Завьялова",
            "Тарабарина"});
            this.listBoxProsecutor.Location = new System.Drawing.Point(261, 63);
            this.listBoxProsecutor.Name = "listBoxProsecutor";
            this.listBoxProsecutor.SelectionMode = System.Windows.Forms.SelectionMode.MultiSimple;
            this.listBoxProsecutor.Size = new System.Drawing.Size(206, 360);
            this.listBoxProsecutor.TabIndex = 9;
            this.listBoxProsecutor.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.ListBoxProsecutor_DrawItem);
            this.listBoxProsecutor.SelectedIndexChanged += new System.EventHandler(this.listBoxProsecutor_SelectedIndexChanged);
            // 
            // deputyIsHere
            // 
            this.deputyIsHere.AutoSize = true;
            this.deputyIsHere.Cursor = System.Windows.Forms.Cursors.Hand;
            this.deputyIsHere.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.deputyIsHere.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.deputyIsHere.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(25)))), ((int)(((byte)(187)))), ((int)(((byte)(155)))));
            this.deputyIsHere.Location = new System.Drawing.Point(14, 33);
            this.deputyIsHere.Name = "deputyIsHere";
            this.deputyIsHere.Padding = new System.Windows.Forms.Padding(4, 2, 2, 2);
            this.deputyIsHere.Size = new System.Drawing.Size(102, 28);
            this.deputyIsHere.TabIndex = 11;
            this.deputyIsHere.Text = "На месте";
            this.deputyIsHere.UseVisualStyleBackColor = true;
            this.deputyIsHere.CheckedChanged += new System.EventHandler(this.DeputyIsHere_CheckedChanged);
            // 
            // prosecutorIsHere
            // 
            this.prosecutorIsHere.AutoSize = true;
            this.prosecutorIsHere.Cursor = System.Windows.Forms.Cursors.Hand;
            this.prosecutorIsHere.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.prosecutorIsHere.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.prosecutorIsHere.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(25)))), ((int)(((byte)(187)))), ((int)(((byte)(155)))));
            this.prosecutorIsHere.Location = new System.Drawing.Point(261, 33);
            this.prosecutorIsHere.Name = "prosecutorIsHere";
            this.prosecutorIsHere.Padding = new System.Windows.Forms.Padding(4, 2, 2, 2);
            this.prosecutorIsHere.Size = new System.Drawing.Size(102, 28);
            this.prosecutorIsHere.TabIndex = 12;
            this.prosecutorIsHere.Text = "На месте";
            this.prosecutorIsHere.UseVisualStyleBackColor = true;
            this.prosecutorIsHere.CheckedChanged += new System.EventHandler(this.prosecutorIsHere_CheckedChanged);
            // 
            // deputyAtDinner
            // 
            this.deputyAtDinner.AutoSize = true;
            this.deputyAtDinner.Cursor = System.Windows.Forms.Cursors.Hand;
            this.deputyAtDinner.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.deputyAtDinner.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.deputyAtDinner.ForeColor = System.Drawing.Color.LawnGreen;
            this.deputyAtDinner.Location = new System.Drawing.Point(151, 33);
            this.deputyAtDinner.Name = "deputyAtDinner";
            this.deputyAtDinner.Padding = new System.Windows.Forms.Padding(4, 2, 2, 2);
            this.deputyAtDinner.Size = new System.Drawing.Size(72, 28);
            this.deputyAtDinner.TabIndex = 13;
            this.deputyAtDinner.Text = "Обед";
            this.deputyAtDinner.UseVisualStyleBackColor = true;
            this.deputyAtDinner.CheckedChanged += new System.EventHandler(this.deputyAtDinner_CheckedChanged);
            // 
            // prosecutorAtDinner
            // 
            this.prosecutorAtDinner.AutoSize = true;
            this.prosecutorAtDinner.Cursor = System.Windows.Forms.Cursors.Hand;
            this.prosecutorAtDinner.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.prosecutorAtDinner.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.prosecutorAtDinner.ForeColor = System.Drawing.Color.LawnGreen;
            this.prosecutorAtDinner.Location = new System.Drawing.Point(398, 33);
            this.prosecutorAtDinner.Name = "prosecutorAtDinner";
            this.prosecutorAtDinner.Padding = new System.Windows.Forms.Padding(4, 2, 2, 2);
            this.prosecutorAtDinner.Size = new System.Drawing.Size(72, 28);
            this.prosecutorAtDinner.TabIndex = 14;
            this.prosecutorAtDinner.Text = "Обед";
            this.prosecutorAtDinner.UseVisualStyleBackColor = true;
            this.prosecutorAtDinner.CheckedChanged += new System.EventHandler(this.prosecutorAtDinner_CheckedChanged);
            // 
            // labelDeputyCount
            // 
            this.labelDeputyCount.AutoSize = true;
            this.labelDeputyCount.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelDeputyCount.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(25)))), ((int)(((byte)(187)))), ((int)(((byte)(155)))));
            this.labelDeputyCount.Location = new System.Drawing.Point(165, 5);
            this.labelDeputyCount.Name = "labelDeputyCount";
            this.labelDeputyCount.Padding = new System.Windows.Forms.Padding(4);
            this.labelDeputyCount.Size = new System.Drawing.Size(55, 24);
            this.labelDeputyCount.TabIndex = 15;
            this.labelDeputyCount.Text = "0 чел";
            this.labelDeputyCount.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // labelProsecutorCount
            // 
            this.labelProsecutorCount.AutoSize = true;
            this.labelProsecutorCount.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelProsecutorCount.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(25)))), ((int)(((byte)(187)))), ((int)(((byte)(155)))));
            this.labelProsecutorCount.Location = new System.Drawing.Point(412, 5);
            this.labelProsecutorCount.Name = "labelProsecutorCount";
            this.labelProsecutorCount.Padding = new System.Windows.Forms.Padding(4);
            this.labelProsecutorCount.Size = new System.Drawing.Size(55, 24);
            this.labelProsecutorCount.TabIndex = 16;
            this.labelProsecutorCount.Text = "0 чел";
            this.labelProsecutorCount.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.ClientSize = new System.Drawing.Size(479, 619);
            this.Controls.Add(this.labelProsecutorCount);
            this.Controls.Add(this.labelDeputyCount);
            this.Controls.Add(this.prosecutorAtDinner);
            this.Controls.Add(this.deputyAtDinner);
            this.Controls.Add(this.prosecutorIsHere);
            this.Controls.Add(this.deputyIsHere);
            this.Controls.Add(this.richTextBoxProsecutor);
            this.Controls.Add(this.listBoxProsecutor);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.richTextBoxDeputy);
            this.Controls.Add(this.listBoxDeputy);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Рецепт";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox listBoxDeputy;
        private System.Windows.Forms.RichTextBox richTextBoxDeputy;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox richTextBoxProsecutor;
        private System.Windows.Forms.ListBox listBoxProsecutor;
        private System.Windows.Forms.CheckBox deputyIsHere;
        private System.Windows.Forms.CheckBox prosecutorIsHere;
        private System.Windows.Forms.CheckBox deputyAtDinner;
        private System.Windows.Forms.CheckBox prosecutorAtDinner;
        private System.Windows.Forms.Label labelDeputyCount;
        private System.Windows.Forms.Label labelProsecutorCount;

    }
}

