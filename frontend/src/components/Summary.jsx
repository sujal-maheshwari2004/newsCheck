export default function Summary({ summaryPoints, resetContent }) {

  return (
    <div className='min-h-[95vh] flex flex-col items-center justify-center py-8'>
      
      <h1 className='text-foreground text-3xl font-semibold text-center mb-6'>
        Summary
      </h1>
      
      <div className='w-[92%] md:max-w-[80%] lg:max-w-[60%] border-border border rounded-lg p-4'>
        {
          summaryPoints.map((i, ind) => {
            return (
              <li
                key={ind}
                className={`${ind==0?'':'mt-6'} md:text-lg text-muted-foreground`}
              >
                {i}
              </li>
            );
          })
        }
      </div>

      <button
        className='bg-foreground text-background border-foreground border rounded-md py-[8px] w-36 font-semibold hover:bg-background hover:text-foreground transition duration-300 mt-6'
        onClick={resetContent}
      >
        Reset
      </button>

    </div>
  );

}