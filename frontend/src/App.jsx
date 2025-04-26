import { useState } from 'react';

export default function App() {
  const [youtubeLink, setYoutubeLink] = useState('');
  const [submitClicked, setSubmitClicked] = useState(false);
  const [summaryPoints, setSummaryPoints] = useState([]);

  async function submitYtLink() {
    setSubmitClicked(true)

    try {

      let res = await fetch('/process/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          youtube_link: youtubeLink,
        }),
      });

      if(!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.detail || 'Something went wrong.')
      }

      const data = await res.json();

      if(data?.summary_points?.length > 0) {
        setSummaryPoints(data.summary_points);
      }

    } catch(err) {
      console.log(err);
      alert(err);
    }
  }

  async function resetContent() {
    setYoutubeLink('');
    setSubmitClicked(false);
    setSummaryPoints([]);
  }

  if(summaryPoints.length > 0) return (
    <div className='min-h-[95vh] flex flex-col items-center justify-center py-8'>
      
      <h1 className='text-foreground text-3xl font-semibold text-center mb-6'>Summary</h1>
      
      <div className='w-[92%] md:max-w-[80%] lg:max-w-[60%] border-border border rounded-lg p-4'>
        {
          summaryPoints.map((i, ind) => {
            return (
              <li className={`${ind==0?'':'mt-6'} md:text-lg text-muted-foreground`}>{i}</li>
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

  return (
    <div className='min-h-[95vh] flex flex-col items-center justify-center'>
      
      <h1 className='text-foreground text-3xl font-semibold text-center'>News Check</h1>

      <p className='text-muted-foreground text-md text-center m-4 w-[90%] md:max-w-[80%] lg:max-w-[50%]'>Lorem Ipsum dolor sit amet lorem duro wingarium leviosar Lorem Ipsum dolor sit amet lorem duro wingarium leviosar Lorem Ipsum dolor sit amet lorem duro wingarium leviosar</p>

      <input
        className='bg-background border-border border rounded-md text-foreground placeholder-muted-foreground p-3 mt-7 mb-7 w-[90%] md:max-w-[70%] lg:max-w-[40%]'
        placeholder='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        value={youtubeLink}
        onChange={e => setYoutubeLink(e.target.value)}
      />

      <button
        className={`${submitClicked?'bg-muted-foreground':'bg-foreground'} text-background ${submitClicked?'border-muted-foreground':'border-foreground'} border rounded-md py-[10px] w-36 font-semibold ${submitClicked?'':'hover:bg-background hover:text-foreground'} transition duration-300`}
        onClick={submitYtLink}
        disabled={submitClicked}
      >
        {submitClicked?'Loading...':'Submit'}
      </button>

    </div>
  );
}
