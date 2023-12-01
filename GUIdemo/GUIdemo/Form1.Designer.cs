namespace GUIdemo
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            button1 = new Button();
            button2_select_file = new Button();
            label1 = new Label();
            textBox1 = new TextBox();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new Point(821, 451);
            button1.Name = "button1";
            button1.Size = new Size(75, 23);
            button1.TabIndex = 0;
            button1.Text = "Close";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2_select_file
            // 
            button2_select_file.Location = new Point(586, 33);
            button2_select_file.Name = "button2_select_file";
            button2_select_file.Size = new Size(81, 23);
            button2_select_file.TabIndex = 1;
            button2_select_file.Text = "Select file";
            button2_select_file.UseVisualStyleBackColor = true;
            button2_select_file.Click += button2_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(23, 41);
            label1.Name = "label1";
            label1.Size = new Size(71, 15);
            label1.TabIndex = 2;
            label1.Text = "File location";
            label1.Click += label1_Click;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(109, 34);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(471, 23);
            textBox1.TabIndex = 3;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(908, 486);
            Controls.Add(textBox1);
            Controls.Add(label1);
            Controls.Add(button2_select_file);
            Controls.Add(button1);
            Name = "Form1";
            Text = "GUI DEMO";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button1;
        private Button button2_select_file;
        private Label label1;
        private TextBox textBox1;
    }
}
