using System;
using ACS.SPiiPlusNET;
using System.Net.NetworkInformation;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;


namespace ACSWpfApp1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        

        public MainWindow()
        {
            InitializeComponent();
        }

        

        // Globle ref
        // create communication object
        //Api channel = new Api();

        Api Ch = new Api();
        int connection_button_status = 0;

        private void btn_connect_Click(object sender, RoutedEventArgs e)
        {
            //Connection_status_textbox.Text = " ";
            // page 39
            // Open Ethernet with TCP protocol communication with the controller 
            // IP address: 10.0.0.100
            if (connection_button_status == 0)
            {
                try
                {
                    int port = (int)EthernetCommOption.ACSC_SOCKET_STREAM_PORT;
                    Ch.OpenCommEthernetTCP("10.0.0.100", port);

                    textBoxToUpdate.Text = "Connection establisthed";
                    btn_connect.Content = "Disconnect";
                    connection_button_status = 2;

                }
                catch (Exception ex)
                {
                    textBoxToUpdate.Text = ex.Message;
                }
            }
            else
            {
                try
                {
                    Ch.CloseComm();

                    textBoxToUpdate.Text = "Disconnected";
                    btn_connect.Content = "Connect";
                    connection_button_status = 0;

                }
                catch (Exception ex)
                {
                    textBoxToUpdate.Text = ex.Message;
                }
            }


        }
    }
}