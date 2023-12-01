namespace GUIdemo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DialogResult Close_program = MessageBox.Show("Do you want to close this window", "Confirm", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (Close_program == DialogResult.Yes)
                this.Close();


        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            // create file open close instance
            OpenFileDialog openFileDialog = new OpenFileDialog();

            // set the title
            openFileDialog.Title = "Select a File";

            // Set the initial dir
            openFileDialog.InitialDirectory = @"C:\Users\mj.j\OneDrive - PBA Systems Pte. Ltd\Malith - R&D\Thermal_compensation";

            // Filter file type
            openFileDialog.Filter = "Text Files|*.txt|All Files|*.*";

            // Show the dialog and get the result
            DialogResult result = openFileDialog.ShowDialog();
            if (result == DialogResult.OK)
            {
                // get the selected file name
                string selectedFileName = openFileDialog.FileName;

                MessageBox.Show("Selected File: " + selectedFileName);

            }
        }
    }
}
