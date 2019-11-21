using IToolbox.Combiner;
using System;
using System.Diagnostics;

namespace toolbox_unit_testing
{
    public class Ut_toolbox
    {
        private static void ut_1()
        {
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();
            //================

#if false
#endif
            int[,] a = new int[2, 2]
                {
                { 1, 2 },
                { 1, 2 }
                };
            a.DeepPrint();

            //================
            stopwatch.Stop();
            Console.WriteLine($"phase 1 took: {stopwatch.Elapsed}");
        }

        private static void Main(string[] args)
        {
            //intro
            Console.WriteLine($"<<<Unit_Test Run toolbox>>> {System.DateTime.Now}");
            ut_1();
            Toolbox.MainFrame.start();
        }//end-func Main
    }//end-class ut_toolbox
}
