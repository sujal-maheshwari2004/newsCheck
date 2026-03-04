export default function YoutubeForm({
  youtubeLink,
  setYoutubeLink,
  submitClicked,
  submitYtLink
}) {

  return (
    <div className='min-h-[95vh] flex flex-col items-center justify-center'>
      
      <h1 className='text-foreground text-3xl font-semibold text-center'>
        News Check
      </h1>

      <p className='text-muted-foreground text-md text-center m-4 w-[90%] md:max-w-[80%] lg:max-w-[50%]'>
        Hours of news in a matter of lines
      </p>

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