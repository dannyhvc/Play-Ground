using System;
using System.Collections;

namespace IToolbox
{
    namespace Combiner
    {
        public static class DeepArry
        {
            public static void DeepPrint(this Array arr)
            {
                IEnumerator myEnumerator = arr.GetEnumerator();
                int i = 0, cols = arr.GetLength(arr.Rank - 1);
                while (myEnumerator.MoveNext())
                {
                    if (i < cols)
                        i++;
                    else
                    {
                        Console.WriteLine();
                        i = 1;
                    }
                    Console.Write("\t{0}", myEnumerator.Current);
                }//end-while
                Console.WriteLine();
            }//end-extension deepPrint()

            public static void foo()
            {

            }
        }//end-method DeepArray

    }//end-namespace Combiner

}//end-namespace IToolbox
